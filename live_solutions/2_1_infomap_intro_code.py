#%% In [1]
import infomap
print(infomap.Infomap().version)

#%% In [2]
!infomap data/ninetriangles.net output/ -N5

#%% In [3]
from pathlib import Path
print(Path('data/ninetriangles.net').read_text())

#%% In [4]
print(Path('output/ninetriangles.tree').read_text())

#%% In [5]
infomapFileIO = infomap.Infomap("-N5")

# Read from file
infomapFileIO.network().readInputData("data/ninetriangles.net")

infomapFileIO.run()

print("Clustered in {} levels with codelength {}".format(infomapFileIO.maxTreeDepth(), infomapFileIO.codelength()))

print("Writing result to file...")
infomapFileIO.writeClu("output/ninetriangles.clu")
infomapFileIO.writeFlowTree("output/ninetriangles.ftree")
print("Done!")

print("\n.ftree file:")
print(Path('output/ninetriangles.ftree').read_text())

#%% In [6]
infomap1 = infomap.Infomap("--directed")

# Use the default network, which got configured as directed by Infomap
network = infomap1.network()

# Add link weight as an optional third argument
network.addLink(0, 1)
network.addLink(0, 2)
network.addLink(0, 3)
network.addLink(1, 0)
network.addLink(1, 2)
network.addLink(2, 1)
network.addLink(2, 0)
network.addLink(3, 0)
network.addLink(3, 4)
network.addLink(3, 5)
network.addLink(4, 3)
network.addLink(4, 5)
network.addLink(5, 4)
network.addLink(5, 3)

infomap1.run()

print("Found {} top modules with codelength {}".format(infomap1.numTopModules(), infomap1.codelength()))

print("\nResult tree:\n#path flow [nodeId]")
for node in infomap1.iterTree():
    if node.isLeaf():
        print("{} {} {}".format(node.path(), node.data.flow, node.stateId))
    else:
        print("{} {}".format(node.path(), node.data.flow))

#%% In [7]
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as colors

#%% In [8]
def findCommunities(G):
    """
    Partition network with the Infomap algorithm.
    Annotates nodes with 'community' id and return number of communities found.
    """
    infomapX = infomap.Infomap("--two-level")

    print("Building Infomap network from a NetworkX graph...")
    for e in G.edges():
        infomapX.network().addLink(*e)

    print("Find communities with Infomap...")
    infomapX.run();

    print("Found {} modules with codelength: {}".format(infomapX.numTopModules(), infomapX.codelength()))

    communities = {}
    for node in infomapX.iterLeafNodes():
        communities[node.physicalId] = node.moduleIndex()

    nx.set_node_attributes(G, values=communities, name='community')

def drawNetwork(G):
    # position map
    pos = nx.spring_layout(G)
    # community ids
    communities = [v for k,v in nx.get_node_attributes(G, 'community').items()]
    numCommunities = max(communities) + 1
    # color map from http://colorbrewer2.org/
    cmapLight = colors.ListedColormap(['#a6cee3', '#b2df8a', '#fb9a99', '#fdbf6f', '#cab2d6'], 'indexed', numCommunities)
    cmapDark = colors.ListedColormap(['#1f78b4', '#33a02c', '#e31a1c', '#ff7f00', '#6a3d9a'], 'indexed', numCommunities)

    # Draw edges
    nx.draw_networkx_edges(G, pos)

    # Draw nodes
    nodeCollection = nx.draw_networkx_nodes(G,
        pos = pos,
        node_color = communities,
        cmap = cmapLight
    )
    # Set node border color to the darker shade
    darkColors = [cmapDark(v) for v in communities]
    nodeCollection.set_edgecolor(darkColors)

    # Draw node labels
    for n in G.nodes():
        plt.annotate(n,
            xy = pos[n],
            textcoords = 'offset points',
            horizontalalignment = 'center',
            verticalalignment = 'center',
            xytext = [0, 0],
            color = cmapDark(communities[n])
        )

    plt.axis('off')
    # plt.savefig("karate.png")
    plt.show()

G=nx.karate_club_graph()

findCommunities(G)

drawNetwork(G)

#%% In [9]
infomapStates = infomap.Infomap("")

network = infomapStates.network()

# network.readInputData(filename)

network.addPhysicalNode(1, "PRE")
network.addPhysicalNode(2, "SCIENCE")
network.addPhysicalNode(3, "PRL")
network.addPhysicalNode(4, "BIO")

network.addStateNode(1, 2)
network.addStateNode(2, 3)
network.addStateNode(3, 2)
network.addStateNode(4, 2)
network.addStateNode(5, 4)

network.addLink(1, 2)
network.addLink(3, 2)
network.addLink(4, 5)

infomapStates.run()

print("Found {} top modules with codelength: {}".format(infomapStates.numTopModules(), infomapStates.codelength()))

print("\n#stateId physicalId moduleIndex flow")
for node in infomapStates.iterTree():
    if node.isLeaf():
        print("{} {} {} {}".format(node.stateId, node.physicalId, node.moduleIndex(), node.data.flow))

print("\nIterate over physical nodes to get the overlapping physical module structure:")
print("#physicalId moduleIndex flow")
for node in infomapStates.iterTreePhysical():
    if node.isLeaf():
        print("{} {} {}".format(node.physicalId, node.moduleIndex(), node.data.flow))

print("\nNote that state nodes 1 and 3 within module 0 is part of the same physical node 2 and merged above")

#%% In [10]
infomapPaths = infomap.Infomap("")

network = infomapPaths.network()

markovOrder = 2
network.addPath([1, 2, 3], markovOrder, 1.0)
network.addPath([1, 2, 3, 4, 5], markovOrder, 1.0)
network.addPath([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], markovOrder, 2.0)
network.addPath([4, 3, 2, 1], markovOrder, 3.0)
network.addPath([1, 2, 3], markovOrder, 1.0)
network.addPath([3, 2, 1], markovOrder, 1.0)

# Write state network that can be loaded more efficiently later instead of the paths data
network.writeStateNetwork("output/paths_states.net")

print("Generated state network with {} nodes and {} links".format(network.numNodes(), network.numLinks()))

print("Run Infomap on network...")
infomapPaths.run()

print("Found {} top modules with codelength: {}".format(infomapPaths.numTopModules(), infomapPaths.codelength()))

print("\n#physicalId moduleIndex flow")
for node in infomapPaths.iterTreePhysical():
    if node.isLeaf():
        print("{} {} {}".format(node.physicalId, node.moduleIndex(), node.data.flow))

print("\nHere physical nodes 2 and 3 have overlapping modules")

#%% In [11]
infomapStates2 = infomap.Infomap("")

infomapStates2.network().readInputData("output/paths_states.net")
infomapStates2.run()

print("Found {} top modules with codelength: {}".format(infomapPaths.numTopModules(), infomapPaths.codelength()))

print("\n#physicalId moduleIndex flow")
for node in infomapStates2.iterTreePhysical():
    if node.isLeaf():
        print("{} {} {}".format(node.physicalId, node.moduleIndex(), node.data.flow))

