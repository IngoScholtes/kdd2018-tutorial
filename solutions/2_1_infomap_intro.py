#%%
import markdown
from IPython.core.display import display, HTML
def md(str):
    display(HTML(markdown.markdown(str + "<br />")))

#%%
md("""
# Infomap
Infomap is a stochastic network clustering algorithm based on minimizing the [Map equation](http://www.mapequation.org/publications.html#Rosvall-Axelsson-Bergstrom-2009-Map-equation).


### The Map Equation

\begin{equation*}
    L(M) = q_\curvearrowright H(\mathcal{Q}) + \sum_{i = 1}^{m}{p_{\circlearrowright}^i H(\mathcal{P}^i)}
\end{equation*}

$L(M)$ measures the amount of information it takes to describe a random walk on a network given a partition of the network into modules $M$. It is a sum of the amount of information needed to describe the movements _between_ and _within_ the modules, which balances the goodness of fit with the complexity of the model. For more information, see [www.mapequation.org](http://www.mapequation.org).

### Features

Infomap supports
* Unweighted and weighted links
* Undirected and directed links
* Two-level and multi-level solutions
* First-order and second-order dynamics
* Hard partitions and overlapping partitions
* Single- and multi-layer networks
""")

#%%
md("""
## Getting started
See https://mapequation.github.io/infomap/ for a simple example and python API to get started with Infomap in python
""")

#%%
md("""
### Install Infomap

The v1.0 beta release is available on the PyPI, install it with
```
pip install infomap
```
or upgrade with
```
pip install --upgrade infomap
```
""")

#%%
md("""
**TODO:** Import infomap. Show the version by running `infomap.Infomap().version` if infomap is imported as `infomap` and check that it is at least `1.0.0-beta.14`.
""")

#%% In [1]
import infomap
print(infomap.Infomap().version)

#%%
md("""
The above should be at least `1.0.0-beta.11`.
""")

#%%
md("""
### Output
Write all files during the tutorials to the `../output` folder, where git will ignore them.
""")

#%%
md("""
## Basic command line use
The installation of the python package also installs a binary for command line use, exemplified below.
See http://www.mapequation.org/code.html#Options for available input flags to `Infomap`
""")

#%%
md("""
**TODO:** Try run the command line version of Infomap installed with the python package. Command line programs can be called directly from jupyter by adding `!` in front, like `!ls`. Run Infomap on the `ninetriangles.net` network in the `data` folder and direct output to the `output` folder. Run it with `5` trials to see the effect of the stochastic nature of Infomap.
""")

#%% In [2]
!infomap data/ninetriangles.net output/ -N5

#%%
md("""
### Input network
The input network above was formed as nine triangles clustered in three levels, which was also recovered with the Infomap clustering algorithm after some trials.

![triangle-network](http://www.mapequation.org/assets/img/triangle-network-levels_3.svg)
""")

#%%
md("""
**TODO:**

- Print the input network from above to see the standard input format for Infomap. (Hint: `pathlib.Path(dir)` has a method `read_text()` to give back the whole string.)
""")

#%% In [3]
from pathlib import Path
print(Path('data/ninetriangles.net').read_text())

#%%
md("""
### Output format
By default on command line, Infomap writes an output file with the same name as the input by with the `.tree` extension. This file contains the multi-level modular structure of the input network.

**TODO:** Print the result from running Infomap above.
""")

#%% In [4]
print(Path('output/ninetriangles.tree').read_text())

#%%
md("""
## From Python
The python API gives more flexibility, but we can still work with files in a similar way as the cli use above.

**TODO:** 

- Cluster the same network as above but through the Infomap python interface.
- Print the number of levels found and the codelength
- Let Infomap write a [flow tree](http://www.mapequation.org/code.html#FTree-format) file to `ninetriangles.ftree` in the output folder and print the result.
""")

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

#%%
md("""
## Basic programmatic use

**TODO:**

- Create an Infomap instance and add some links programmatically
- Run the clustering and iterate over the result and print the tree path to the node, the flow and, if a leaf node, the node id. (Hint: All leaf nodes has a unique `stateId` property and a `physicalId` property, that is identical on first-order networks)
""")

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

#%%
md("""
## Infomap + NetworkX
Generate and draw a network with NetworkX, colored
according to the community structure found by Infomap.

**TODO:**

- Create a networkx graph (Hint: `karate_club_graph()` is available on `networkx`)
- Write a function that takes a networkx graph as input, runs a two-level Infomap clustering and sets clusters as node attributes on the networkx graph, mapped by the node id (physicalId).
- Render the networkx graph with nodes colored by the Infomap clustering
""")

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

#%%
md("""
## Higher-order networks
""")

#%%
md("""
### General state networks
The [state format](http://www.mapequation.org/code.html#State-format) describes the exact network used internally by Infomap. It can model both ordinary networks and memory networks (of variable order).

#### Example
```
*Vertices 4
1 "PRE"
2 "SCIENCE"
3 "PRL"
4 "BIO"
# *ngrams
# 1 2 3
# 1 2 2 3
# 4 2 4
*States
#stateId physicalId [name]
1 2 "1 2"
2 3 "2 3"
3 2 "1 2 2"
4 2 "4 2"
5 4 "2 4"
*Links
1 2
3 2
4 5
```
Here some ngrams are represented by ordinary links between a set of state nodes.
""")

#%%
md("""
#### Programmatically creating a state network

**TODO**:

- Create the above network programmatically with Infomap
- Run the clustering and iterate over the underlying state network to print out space separated list of `#stateId physicalId moduleIndex flow` for each leaf node.
- Iterate over the physical network and print `#physicalId moduleIndex flow` for each node
- What happened to state node 1 and 3?
""")

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

#%%
md("""
### paths

Infomap can generate a higher-order state network from path data, specifying a certain markov order. Markov order 1 corresponds to an ordinary network where the memory is discarded.

**TODO:**

- Programmatically create a state network of certain order from path data
- Write the state network to file
- Partition the state network and print the codelength and the physical tree as above
- Did you get any overlapping modules on the physical nodes?
""")

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

#%%
md("""
#### Running on the generated state network will give the same result

**TODO:**

- Run Infomap on the generated state network from above
- Check that the codelength is the same
""")

#%% In [11]
infomapStates2 = infomap.Infomap("")

infomapStates2.network().readInputData("output/paths_states.net")
infomapStates2.run()

print("Found {} top modules with codelength: {}".format(infomapPaths.numTopModules(), infomapPaths.codelength()))

print("\n#physicalId moduleIndex flow")
for node in infomapStates2.iterTreePhysical():
    if node.isLeaf():
        print("{} {} {}".format(node.physicalId, node.moduleIndex(), node.data.flow))

#%%
md("""
### Visualising the multi-level modular network

**TODO:**

- Use the [Network Navigator](http://navigator.mapequation.org) to load the `.ftree` file generated earlier from the triangular network.
""")

