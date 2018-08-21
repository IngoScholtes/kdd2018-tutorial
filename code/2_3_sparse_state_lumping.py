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

In this view, we may note that some rows have similar probability distributions. We can measure how much information we lose when merging two state nodes with the [Jensen-Shannon Distance](https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence).

The idea behind sparse state networks is that we can lump state nodes (within each physical node) that constrain the network flow in a similar way without losing (much) information.
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

#%% In [1]
# TODO: Fill code here


#%% In [2]
# TODO: Fill code here


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

#%% In [3]
# TODO: Fill code here


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

#%% In [4]
# TODO: Fill code here


#%%
md("""
### Cluster with scikit-learn

Now we can use general [scikit-learn clustering algorithm](http://scikit-learn.org/stable/modules/clustering.html) that takes a custom pairwise distance function as a metric, like [Agglomerative Clustering](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering). We can also use for example `cosine` instead with similar result. Many take as input the number of clusters you want. For the example feature matrix, it's two.

**TODO:**
- Create a AgglomerativeClustering model and find two clusters based on the Jensen-Shannon distance
- Use the row-to-stateId map to check which state nodes are clustered together (the red left ones are state node 1 and 2, the blue right ones are state node 7 and 8).
""")

#%% In [5]
# TODO: Fill code here


#%% In [6]
# TODO: Fill code here


#%%
md("""
### Lump whole network
Now we are ready to run this on the whole network. For convenience, `StateNetwork` provides a method `clusterStateNodes` that takes an argument `clusterFeatureMatrix` where you can send in a custom clustering function. This function gets a feature matrix as input argument and expects an array of cluster labels back.

**TODO:**
- Write a clustering method that takes a feature matrix as input, tries to cluster it in a certain number of clusters (half the number of state nodes would fit this toy network), using the Jensen-Shannon distance, and returns an array of cluster labels.
- Cluster the whole state network using the method above
""")

#%% In [7]
# TODO: Fill code here


#%%
md("""
## Did we lose any information?
The state network has two methods `calcEntropyRate()` and `calcLumpedEntropyRate()` to calculate the average number of bits required to encode the random walk on each physical node.

**TODO:**
- Run the methods above and check that the entropy rates stayed the same
- Write lumped state network to file with `writeLumpedStateNetwork(filename)` and check that it matches the sparse network in the figure below
""")

#%% In [8]
# TODO: Fill code here


#%% In [9]
# TODO: Fill code here


#%%
md("""
### Now we have generated the sparse network (with lossless compression)
![toy_states](../figures/toy_states_full.png)
![toy_states](../figures/toy_states_sparse.png)

To the left, the original second-order network. To the right, the sparse network formed by lumping similar state nodes within each physical node.
""")

