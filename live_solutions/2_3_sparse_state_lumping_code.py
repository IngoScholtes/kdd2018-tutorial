#%%
import markdown
from IPython.core.display import display, HTML
def md(str):
    display(HTML(markdown.markdown(str + "<br />")))

#%% In [1]
from state_lumping_network import StateNetwork

#%% In [2]
net = StateNetwork()
net.readFromFile("data/toy_states.net")

#%% In [3]
X, rowToStateId = net.getFeatureMatrix(1)
print("Feature matrix for the central physical node: \n{}\n rowToStateId: {}".format(X, rowToStateId))

#%% In [4]
import numpy as np
from sklearn.metrics import pairwise_distances

def plogp(x):
    x = np.asarray(x)
    return x * np.log2(x, where = x>0)

def entropy(x):
    return -np.sum(plogp(x))

def jensen_shannon_distance(x1, x2):
    x1 = np.asarray(x1)
    x2 = np.asarray(x2)
    mix = (x1 + x2) / 2
    return np.sqrt(entropy(mix) - (entropy(x1) + entropy(x2)) / 2)

def jensen_shannon_distances(X):
    return pairwise_distances(X, metric=jensen_shannon_distance)

print(jensen_shannon_distance(X[0], X[1]))
print(jensen_shannon_distance(X[1], X[2]))

#%% In [5]
from sklearn import cluster

#%% In [6]
model = cluster.AgglomerativeClustering(
    linkage="complete",
    # affinity=jensen_shannon_distances,
    affinity="cosine",
    n_clusters=2
)

labels = model.fit_predict(X)
print("Cluster labels in feature matrix space: {}\nCluster labels in state node space: {}".format(
    labels,
    {rowToStateId[i]:clusterId for i,clusterId in enumerate(labels)}
))

#%% In [7]
def getFeatureClusterFunction(clusterRate=0.5):
    def calcClusters(X):
        numStates, numFeatures = X.shape
        if numStates < 2 or numFeatures < 2:
            # Don't cluster if too small
            return list(range(numStates))

        # Can be an adaptive number of clusters based on entropy reduction
        n_clusters = max(1, int(clusterRate * numStates))
        model = cluster.AgglomerativeClustering(
            linkage="complete",
            affinity=jensen_shannon_distances,
#             affinity="cosine",
            n_clusters=n_clusters
        )

        labels = model.fit_predict(X)
        return labels
    return calcClusters

net.clusterStateNodes(clusterFeatureMatrix=getFeatureClusterFunction())

#%% In [8]
h1 = net.calcEntropyRate()
h2 = net.calcLumpedEntropyRate()
print("Entropy rate before: {}, after: {}".format(h1, h2))

#%% In [9]
from pathlib import Path
net.writeLumpedStateNetwork("output/toy_lumped.net")
print(Path('output/toy_lumped.net').read_text())

