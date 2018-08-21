#%%
import markdown
from IPython.core.display import display, HTML
def md(str):
    display(HTML(markdown.markdown(str + "<br />")))

#%%
md("""
## Sparse state networks 
Second-order dynamics on a physical network can be described by first-order dynamics on a second-order state network.

We can represent this second-order network by it's _state transition matrix_ $P_{ij}$ with the probabilities for the random walker to transition from state node $i$ to state node $j$.

In this view, we may note that some rows have similar probability distributions. We can measure how similar two probability distributions are with the [Jensen-Shannon Distance](https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence).

The idea behind sparse state networks is that we can lump state nodes (within each physical node) that constrain the network flow in a similar way without loosing (much) information.
""")

#%%
md("""
### Transforms to a general machine learning problem
We will here solve the problem using standard [clustering algorithms](http://scikit-learn.org/stable/modules/clustering.html#clustering) from the [scikit-learn](http://scikit-learn.org/) package.

In order to do that, we have to transform the state network into features usable for machine learning. We can do this with the help of the code in [state_lumping_network.py](./state_lumping_network.py).

**TODO:**
- import StateNetwork from state_lumping_network
- Create a new StateNetwork
- use the `.readFromFile(filename)` method to read in `data/toy_states.net`
""")

#%% In [2]
from state_lumping_network import StateNetwork

#%% In [3]
net = StateNetwork()
net.readFromFile("data/toy_states.net")

#%%
md("""
![toy_states](../figures/toy_states_full.png)

Figure 1: Second-order state network in `data/toy_states.net`
""")

#%%
md("""
## Feature matrix

The feature matrix for a physical node is simply the rows of the state transition matrix for the state nodes belonging to that physical node.
To simplify, there is a `getFeatureMatrix` method that removes all all-zero rows and columns in the feature matrix and provides a mapping back to the original state network. It takes the physical node id as input parameter and returns a tuple `(X, T)`, where `X` is the feature matrix (np.array) of size (numNonDanglingStateNodes, numLinkedNodes) and `T` is a dictionary transforming row index in the feature matrix to state node id.

**TODO:**
- Use the method above and get the feature matrix and rowToStateId map
- Print the two items
""")

#%% In [4]
X, rowToStateId = net.getFeatureMatrix(1)
print("Feature matrix for the central physical node: \n{}\n rowToStateId: {}".format(X, rowToStateId))

#%%
md("""
### Measure pairwise similarity
Now we can compare rows pairwise and cluster the most similar rows together. The Jensen-Shannon distance is unfortunately not implemented in scikit-learn (though it exist in a [pull request](https://github.com/scikit-learn/scikit-learn/pull/4191)), so let's create it.

**TODO:**
- Write a function that takes two equally sized arrays of probabilities as input and returns the Jensen-Shannon distance between them
- Write a function that takes a vector array as input and returns a [pairwise_distances](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_distances.html) from sklearn.metrics with your Jensen-Shannon distance function as metric
- Compute the Jensen-Shannon distance between the two different rows of the feature matrix, and check that at gives zero for same input

Tips, using numpy:
- Work with `np.asarray(x)` in the function to allow for both a numpy array and an ordinary python list as input
- `np.log2(x)` can be modified to `np.log2(x, where = x>0)` to handle zeros
""")

#%% In [19]
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

#%%
md("""
### Cluster with scikit-learn

Now we can use general [scikit-learn clustering algorithm](http://scikit-learn.org/stable/modules/clustering.html) that takes a custom pairwise distance function as a metric, like [Agglomerative Clustering](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering). We can also use for example `cosine` instead with similar result. Many take as input the number of clusters you want. For the example feature matrix, it's two.

**TODO:**
- Create a AgglomerativeClustering model and find two clusters based on the Jensen-Shannon distance
- Use the row-to-stateId map to check which state nodes are clustered together (the red left ones are state node 1 and 2, the blue right ones are state node 7 and 8).
""")

#%% In [11]
from sklearn import cluster

#%% In [12]
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

#%%
md("""
### Lump whole network
Now we are ready to run this on the whole network. For convenience, `StateNetwork` provides a method `clusterStateNodes` that takes an argument `clusterFeatureMatrix` where you can send in a custom clustering function. This function gets a feature matrix as input argument and expects an array of cluster labels back.

**TODO:**
- Write a clustering method that takes a feature matrix as input, tries to cluster it in a certain number of clusters (half the number of state nodes would fit this toy network), using the Jensen-Shannon distance, and returns an array of cluster labels.
- Cluster the whole state network using the method above
""")

#%% In [20]
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

#%%
md("""
## Did we loose any information?
The state network has two methods `calcEntropyRate()` and `calcLumpedEntropyRate()` to calculate the average number of bits required to encode the random walk on each physical node.

**TODO:**
- Run the methods above and check that the entropy rates stayed the same
- Write lumped state network to file with `writeLumpedStateNetwork(filename)` and check that it matches the sparse network in the figure below
""")

#%% In [21]
h1 = net.calcEntropyRate()
h2 = net.calcLumpedEntropyRate()
print("Entropy rate before: {}, after: {}".format(h1, h2))

#%% In [22]
from pathlib import Path
net.writeLumpedStateNetwork("output/toy_lumped.net")
print(Path('output/toy_lumped.net').read_text())

#%%
md("""
### Now we have generated the sparse network (with lossless compression)
![toy_states](../figures/toy_states_full.png)
![toy_states](../figures/toy_states_sparse.png)

To the left, the original second-order network. To the right, the sparse network formed by lumping similar state nodes within each physical node.
""")

