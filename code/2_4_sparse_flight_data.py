#%%
import markdown
from IPython.core.display import display, HTML
def md(str):
    display(HTML(markdown.markdown(str + "<br />")))

#%%
md("""
## Sparse flight data

A key question for the generation of sparse state networks is _how_ sparse. If we lump all state nodes with each physical node, we lose all higher-order information and may underfit. On the other hand, keeping all second-order state nodes may overfit.

In this tutorial we will generate second-order state networks from path data and from there generate multiple sparse networks with different number of (lumped) state nodes and evaluate the result with Infomap
""")

#%%
md("""
### Generate training and validation sets
To get a bigger network, we can merge the flight path data from the four quarters (`"data/air2015_{q}_paths.net" for q in [1,2,3,4]`). But to evaluate the goodness of fit, we can split each path randomly in either a _training_ or a _validation_ set and write a path data file for each of the data set.

**TODO:**
- Write a function that merges all paths of the year and writes it to a _training_ paths file with 50% chance and to a _validation_ paths file otherwise. Skip the '*vertices' section
""")

#%% In [5]
# TODO: Fill code here


#%%
md("""
#### Generate state networks from paths

**TODO:**
- Use Infomap to generate second-order state networks from the two paths data files.
""")

#%% In [6]
# TODO: Fill code here


#%%
md("""
### Generate _sparse_ state networks

Here we will generate multiple lumped state networks with different amount of state nodes. A simple way is to parameterise this with a cluster rate $r$ going from 0.1 to 1, where `n_clusters = max(1, int(r * numStateNodes)`. For convenience, you can just send in the argument `clusterRate` to `clusterStateNodes` to achieve this, instead of the cluster function in the previous tutorial.

**TODO:**
- Read in the training network with `StateNetwork`
- Calculate entropy rate
- Cluster the network for all cluster rates $r$ in for example `np.linspace(0.1, 1, 10)`.
- Save the number of lumped state nodes and the lumped entropy rate
""")

#%% In [11]
# TODO: Fill code here


#%%
md("""
#### How much information do we lose as we reduce the number of state nodes?

**TODO:**
- Plot the entropy rate against the number of state nodes
- Check that the entropy rates approaches the original one and coincides at cluster rate $r = 1$
""")

#%% In [13]
# TODO: Fill code here


#%%
md("""
Note that the original number of state nodes can be much larger than the maximum in the lumped state networks due to dangling nodes which are lumped implicitly.
""")

#%%
md("""
### Validate with Infomap
The goal here is to calculate the codelength for the validation network, given the different partitions found on the lumped training networks.

**TODO:**
- Run Infomap on all lumped state networks and write a `.tree` file for each and store codelength
- Run Infomap on the validation network but with cluster data from external file for all `.tree` files generated from the lumped networks and store the codelength
- Plot the training and validation codelengths against the number of state nodes and check if there is an optimum that balances underfit and overfit
""")

