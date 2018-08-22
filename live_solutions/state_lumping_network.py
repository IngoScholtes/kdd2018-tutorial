from collections import namedtuple, defaultdict
import re
import numpy as np
from sklearn import preprocessing
from sklearn import cluster
import time
from pathlib import Path

Link = namedtuple('Link', 'source, target, weight')


class StateNode(object):
    def __init__(self, stateId, physicalId, name):
        self.stateId = stateId
        self.physicalId = physicalId
        self.name = name
        self.outWeight = 0
        self.weight = 1.0
        self.stateLinks = defaultdict(float)

    def __str__(self):
        return "stateId: {}, physicalId: {}, name: {}, outWeight: {}, #stateLinks: {}".format(self.stateId, self.physicalId, self.name, self.outWeight, len(self.stateLinks))

    def addStateLink(self, stateTarget, weight):
        self.stateLinks[stateTarget] += weight
        self.outWeight += weight

    def isDangling(self):
        return len(self.stateLinks) == 0


class LumpedStateNode(object):
    def __init__(self, physicalId=-1, lumpedStateId=-1):
        self.lumpedStateId = lumpedStateId
        self.physicalId = physicalId
        self.stateIds = []
        self.outWeight = 0
        self.stateLinks = defaultdict(float)
        self.stateLinkMultiplicity = defaultdict(int)

    def __str__(self):
        return "LumpedStateNode (physicalId: {}, stateIds: {}, #links: {}".format(self.physicalId, self.stateIds, len(self.stateLinks))

    def addLumpedStateLink(self, lumpedStateTarget, weight):
        numLinksBefore = len(self.stateLinks)
        self.stateLinks[lumpedStateTarget] += weight
        self.stateLinkMultiplicity[lumpedStateTarget] += 1
        self.outWeight += weight
        numLinksAfter = len(self.stateLinks)
        return numLinksAfter - numLinksBefore

    def averageLumpedStateLinkWeights(self):
        totalOutWeight = 0.0
        for linkTarget in self.stateLinks.keys():
            weight = self.stateLinks[linkTarget]
            averageLinkWeight = weight / self.stateLinkMultiplicity[linkTarget]
            self.stateLinks[linkTarget] = averageLinkWeight
            totalOutWeight += averageLinkWeight
        self.outWeight = totalOutWeight

    def isDangling(self):
        return len(self.stateLinks) == 0


class PhysNode(object):
    def __init__(self, physicalId=-1, name=None):
        self.physicalId = physicalId
        self.name = name
        self.stateNodes = []
        self.clusters = {}  # stateId -> clusterIndex
        self.numClusters = 0
        self.lumpedStateNodes = []
        self.haveDanglingNodes = False
        self.danglingStateNodes = []
        # self.outWeight = 0.0

    def __str__(self):
        return "Physical node {} ({} stateNodes)".format(self.stateNodes[0].physicalId if len(self.stateNodes) > 0 else '-', len(self.stateNodes))

    def numStateNodes(self):
        return len(self.stateNodes)

    def numDanglingStateNodes(self):
        return len(self.danglingStateNodes)

    def getName(self):
        return self.name or self.physicalId

    def addStateNode(self, node):
        self.stateNodes.append(node)

    def getLumpedNodeFromStateNodeId(self, stateId):
        clusterIndex = self.clusters[stateId]
        lumpedNode = self.lumpedStateNodes[clusterIndex]
        return lumpedNode

    def createLumpedStateNodesFromClustering(self):
        numLumpedNodes = self.numClusters
        self.lumpedStateNodes = [LumpedStateNode(
            self.physicalId) for i in range(numLumpedNodes)]
        for stateNode in self.stateNodes:
            clusterIndex = self.clusters[stateNode.stateId]
            lumpedNode = self.lumpedStateNodes[clusterIndex]
            lumpedNode.stateIds.append(stateNode.stateId)


class StateNetwork(object):
    def __init__(self):
        self.physNodes = defaultdict(PhysNode)
        self.stateNodes = defaultdict(StateNode)
        self.links = []
        self.totalWeight = 0.0
        self.lumpedStateNodes = defaultdict(LumpedStateNode)
        self.numClusters = 0

    def __str__(self):
        return "StateNetwork ({} physical nodes, {} state nodes and {} links)".format(len(self.physNodes), len(self.stateNodes), len(self.links))

    def numPhysicalNodes(self):
        return len(self.physNodes)

    def numStateNodes(self):
        return len(self.stateNodes)

    def numLumpedStateNodes(self):
        return len(self.lumpedStateNodes)

    def addPhysicalNode(self, physicalId, name=None):
        physNode = self.physNodes[physicalId]
        physNode.physicalId = physicalId
        physNode.name = name
        return physNode

    def addStateNode(self, node):
        physNode = self.addPhysicalNode(node.physicalId)
        physNode.addStateNode(node)
        self.stateNodes[node.stateId] = node

    def addStateLink(self, link):
        self.links.append(link)
        # physTarget = self.stateNodes[link.target].physicalId
        # self.stateNodes[link.source].addPhysLink(physTarget, link.weight)
        self.stateNodes[link.source].addStateLink(link.target, link.weight)
        self.totalWeight += link.weight
        # physSource = self.stateNodes[link.source].physicalId
        # if physSource != physTarget:
        #   self.physNodes[physSource].outWeight += link.weight

    def addLumpedStateNode(self, lumpedStateNode):
        lumpedStateId = len(self.lumpedStateNodes) + 1
        lumpedStateNode.lumpedStateId = lumpedStateId
        self.lumpedStateNodes[lumpedStateId] = lumpedStateNode

    def clearLumpedNodes(self):
        self.lumpedStateNodes.clear()
        for physNode in self.physNodes.values():
            physNode.lumpedStateNodes = []
    # def getLumpedNodeFromStateNodeId(self, stateId):
    #   physId = self.stateNodes[stateId].physicalId
    #   return self.physNodes[physId].getLumpedNodeFromStateNodeId(stateId)

    def readFromFile(self, filename):
        context = None
        print("Read state network from file '{}'...".format(filename))
        with open(filename, 'r') as fp:
            for line in fp:
                if line.startswith('#'):
                    continue
                if line.startswith('*'):
                    l = line.lower()
                    if l.startswith('*states'):
                        context = 'States'
                    elif l.startswith('*links'):
                        context = 'Links'
                    elif l.startswith('*arcs'):
                        context = 'Links'
                if context == 'States':
                    m = re.match(r'(\d+) (\d+)(?: \"(.+)\")?', line)
                    if m:
                        [stateId, physicalId, name] = m.groups()
                        # self.stateNodes.append(StateNode(int(stateId), int(physicalId), name))
                        node = StateNode(int(stateId), int(physicalId), name)
                        self.addStateNode(node)
                if context == 'Links':
                    m = re.match(r'(\d+) (\d+) ([\d\.]+)', line)
                    if m:
                        [source, target, weight] = m.groups()
                        link = Link(int(source), int(target), float(weight))
                        self.addStateLink(link)
        print(" -> {}".format(self))

    def writeLumpedStateNetwork(self, filename):
        print("Writing lumped state network to file '{}'...".format(filename))
        with open(filename, 'w') as fp:
            fp.write("# physical nodes: {}\n".format(self.numPhysicalNodes()))
            fp.write("# state nodes: {}\n".format(self.numStateNodes()))
            fp.write("# lumped state nodes: {}\n".format(
                self.numLumpedStateNodes()))
            # vertices
            fp.write("*Vertices\n")
            for physId, physNode in self.physNodes.items():
                fp.write("{} \"{}\"\n".format(physId, physNode.getName()))
            # states
            fp.write("*States\n")
            fp.write("#lumpedStateId physicalId lumpedStateIds\n")
            for lumpedStateId, lumpedStateNode in self.lumpedStateNodes.items():
                fp.write("{} {} \"{}\"\n".format(lumpedStateId,
                                                 lumpedStateNode.physicalId, lumpedStateNode.stateIds))
            # links
            fp.write("*Links\n")
            for sourceId, lumpedStateNode in self.lumpedStateNodes.items():
                for targetId, weight in lumpedStateNode.stateLinks.items():
                    fp.write("{} {} {}\n".format(sourceId, targetId, weight))
        

    def calcEntropyRate(self):
        h = 0.0
        for stateNode in self.stateNodes.values():
            H = 0.0
            for w in stateNode.stateLinks.values():
                p = w / stateNode.outWeight
                H -= p * np.log2(p)
            h += stateNode.outWeight * H / self.totalWeight
        return h

    def calcLumpedEntropyRate(self):
        h = 0.0
        totalWeight = 0.0
        for stateNode in self.lumpedStateNodes.values():
            totalWeight += stateNode.outWeight
        for stateNode in self.lumpedStateNodes.values():
            H = 0.0
            for w in stateNode.stateLinks.values():
                p = w / stateNode.outWeight
                H -= p * np.log2(p)
            h += stateNode.outWeight * H / totalWeight
        return h

    def getFeatureMatrix(self, physicalId, normalizeRows=True,
                         physicalFeatures=False):
        """Generate a feature matrix of outgoing link weight
        distributions per state node.
        Rows are state nodes, columns are linked target nodes

        @param physicalId : int, get feature matrix for the selected physical node
        @param normalizeRows : bool, normalize outgoing weights to a probability 
        distribution for each state node (l1-norm) (default: True)
        @param physicalFeatures : bool, aggregate outgoing links to different 
        physical nodes (reduces feature space)

        @return (X, T), where
        X is the feature matrix (np.array) of size
        (numNonDanglingStateNodes, numLinkedNodes)
        T a dictionary transforming row index to state node id
        """
        stateIdToRowIndex = defaultdict(int)
        targetIdToFeatureIndex = defaultdict(int)
        rowIndexToStateId = {}
        denseLinks = []
        physNode = self.physNodes[physicalId]
        for stateNode in physNode.stateNodes:
            # Skip dangling nodes
            if stateNode.isDangling():
                physNode.danglingStateNodes.append(stateNode)
                continue
            # row mapping: stateId to dense row index
            rowIndex = len(stateIdToRowIndex)
            if stateNode.stateId in stateIdToRowIndex:
                rowIndex = stateIdToRowIndex[stateNode.stateId]
            else:
                stateIdToRowIndex[stateNode.stateId] = rowIndex
            rowIndexToStateId[rowIndex] = stateNode.stateId

            for targetId, weight in stateNode.stateLinks.items():
                if physicalFeatures:
                    targetId = self.stateNodes[targetId].physicalId
                # feature mapping: physical link target to dense column index
                featureIndex = len(targetIdToFeatureIndex)
                if targetId in targetIdToFeatureIndex:
                    featureIndex = targetIdToFeatureIndex[targetId]
                else:
                    targetIdToFeatureIndex[targetId] = featureIndex
                denseLinks.append((rowIndex, featureIndex, weight))
        numRows, numFeatures = (len(stateIdToRowIndex),
                                len(targetIdToFeatureIndex))
        X = np.zeros((numRows, numFeatures))
        if numFeatures is 0:
            return X, {}
        for (rowIndex, featureIndex, weight) in denseLinks:
            X[rowIndex][featureIndex] += weight

        if normalizeRows:
            preprocessing.normalize(X, axis=1, norm='l1', copy=False)

        return X, rowIndexToStateId

    def clusterStateNodes(self, physicalNodeIds=None,
                          physicalFeatures=False, clusterFeatureMatrix=None,
                          clusterRate=0.5, getNumClusters=None,
                          mergeDanglingNodes=True,
                          skipLumping=False):
        """Generate a cluster map for all state nodes that is used when lumping them

        """
        print("Cluster state nodes...")
        totNumClusters = 0
        physNodeIds = physicalNodeIds or self.physNodes.keys()
        for physId in physNodeIds:
            physNode = self.physNodes[physId]
            X, rowIndexToStateId = self.getFeatureMatrix(
                physId, physicalFeatures=physicalFeatures)
            (numStates, numFeatures) = X.shape

            labels = list(range(numStates))
            if callable(clusterFeatureMatrix):
                labels = clusterFeatureMatrix(X)
            else:
                if numStates < 2 or numFeatures < 2:
                    labels = list(range(numStates))
                else:
                    n_clusters = getNumClusters(numStates) if callable(
                        getNumClusters) else max(1, int(clusterRate * numStates))
                    model = cluster.AgglomerativeClustering(
                        linkage="complete",
                        affinity="cosine",
                        n_clusters=n_clusters
                    )
                    labels = model.fit_predict(X)

            clusters = {}
            maxClusterIndex = -1
            for rowIndex, clusterIndex in enumerate(labels):
                clusters[rowIndexToStateId[rowIndex]] = clusterIndex
                if clusterIndex > maxClusterIndex:
                    maxClusterIndex = clusterIndex
            if physNode.numDanglingStateNodes() > 0:
                if mergeDanglingNodes:
                    # add dangling nodes to a separate last cluster
                    maxClusterIndex += 1
                    danglingClusterIndex = maxClusterIndex
                    for danglingStateNode in physNode.danglingStateNodes:
                        clusters[danglingStateNode.stateId] = danglingClusterIndex
                else:
                    # add dangling nodes to their own cluster
                    clusterIndex = maxClusterIndex + 1
                    maxClusterIndex += physNode.numDanglingStateNodes()
                    for danglingStateNode in physNode.danglingStateNodes:
                        clusters[danglingStateNode.stateId] = clusterIndex
                        clusterIndex += 1

            physNode.clusters = clusters
            numClusters = maxClusterIndex + 1
            physNode.numClusters = numClusters
            totNumClusters += numClusters

        self.numClusters = totNumClusters
        if skipLumping:
            print("Done!")
        else:
            self.generateLumpedNetwork()

    def generateLumpedNetwork(self):
        """Generate lumped state network from clustering
        """
        if self.numClusters == 0:
            raise RuntimeError(
                "No clusters, did you forgot to run clustering before?")
        print("Generate lumped state network from clustering...")
        self.clearLumpedNodes()
        # First generate all lumped state nodes
        for physId, physNode in self.physNodes.items():
            physNode.createLumpedStateNodesFromClustering()
            for lumpedNode in physNode.lumpedStateNodes:
                self.addLumpedStateNode(lumpedNode)
        numLumpedStateLinks = 0
        # Aggregate state links to lumped state nodes
        for physId, physNode in self.physNodes.items():
            for stateNode in physNode.stateNodes:
                lumpedSourceNode = physNode.getLumpedNodeFromStateNodeId(
                    stateNode.stateId)
                for targetStateId, weight in stateNode.stateLinks.items():
                    targetPhysId = self.stateNodes[targetStateId].physicalId
                    targetPhysNode = physNode if targetPhysId == physId else self.physNodes[
                        targetPhysId]
                    lumpedTargetNode = targetPhysNode.getLumpedNodeFromStateNodeId(
                        targetStateId)
                    lumpedTargetId = lumpedTargetNode.lumpedStateId
                    numLumpedStateLinks += lumpedSourceNode.addLumpedStateLink(lumpedTargetId, weight)
        # Average instead of sum link weights
        # for stateNode in self.lumpedStateNodes.values():
        #     stateNode.averageLumpedStateLinkWeights()
        print(" -> {} state nodes and {} links in lumped network.".format(self.numLumpedStateNodes(), numLumpedStateLinks))


def calcClusters(X):
    numStates, numFeatures = X.shape
    if numStates < 2 or numFeatures < 2:
        # Don't cluster if too small
        return list(range(numStates))

    # Can be an adaptive number of clusters based on entropy reduction
    n_clusters = max(1, int(0.5 * numStates))
    model = cluster.AgglomerativeClustering(
        linkage="complete",
        # affinity=jensen_shannon_distances,
        affinity="cosine",
        n_clusters=n_clusters
    )

    labels = model.fit_predict(X)
    return labels


def test():
    start = time.clock()
    
    sparseNet = StateNetwork()
    sparseNet.readFromFile("../output/air2015_1_order_2.net")
    
    sparseNet.clusterStateNodes(clusterFeatureMatrix=calcClusters)

    h1 = sparseNet.calcEntropyRate()
    h2 = sparseNet.calcLumpedEntropyRate()
    print("Entropy rate original: {}, lumped: {}".format(h1, h2))
    
    sparseNet.writeLumpedStateNetwork("../output/air2015_1_order_lumped.net")
    
    print("Elapsed time: {}s".format(time.clock() - start))

if __name__ == '__main__':
    test()
