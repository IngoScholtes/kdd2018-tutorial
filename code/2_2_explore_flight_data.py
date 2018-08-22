#%%
import markdown
from IPython.core.display import display, HTML
def md(str):
    display(HTML(markdown.markdown(str + "<br />")))

#%%
md("""
# Mapping quarterly flight path data
Here we make use public data from the Airline Origin and Destination Survey (DB1B) from Bureau of Transportation Statistics (transtats.bts.gov). See https://github.com/mapequation/airline-data for scripts to download and generate this data.

Path data for this tutorial is available on `data/air2015_{q}_paths.net` for each q in [1,2,3,4] and looks like this:

```
*vertices 345
11618 "Newark, NJ: Newark Liberty International"
11057 "Charlotte, NC: Charlotte Douglas International"
11617 "New Bern/Morehead/Beaufort, NC: Coastal Carolina Regional"
...
*paths
11618 11618 11057 11617 11057 22
11618 11618 11057 10994 11057 47
11618 11618 11057 12323 11057 52
11618 11618 11057 13495 11057 82
...
```
The last column is assumed to be the weight of the path, unless `--unweighted-paths` is provided to Infomap.
""")

#%%
md("""
## Generate state networks of first and second order

**TODO:**

- Import infomap
- Write a function to generate a state network of specified Markov order from path data and write to output dir
- Generate first and second order state networks for all four quarters
""")

#%% In [1]
# TODO: Fill code here


#%% In [2]
# TODO: Fill code here


#%% In [3]
# TODO: Fill code here


#%%
md("""
## Mapping change in first-order networks with Alluvial Diagram

![alluvial-diagram](http://www.mapequation.org/assets/img/neuroAlluvial2001-2007.svg)


**TODO:**

- Write a function that takes an input network filename, clusters the network and writes a `.map` file
- Generate `.map` files for all four first-order state networks
- Load the `.map` files into the [Alluvial Generator](http://www.mapequation.org/apps/MapGenerator.html) and explore the modular structure over time
""")

#%% In [4]
# TODO: Fill code here


#%% In [5]
# TODO: Fill code here


#%%
md("""
### No structure in first-order networks?
In first-order, the network appears too well connected for any modular structure to be revealed. That can be solved in the second-order networks where physical nodes can have overlapping modules. But we may uncover some modular structure even in the first-order networks by scaling down the markov-time to increase the cost of moving between clusters.

#### Reveal first-order structure in tightly connected networks using Markov time

**TODO:**

- Modify the `.map` generating method above to take Infomap flags as input
- Re-run with `--markov-time 0.75`
- Checkout the changes in the Alluvial Generator, any interesting stories?
""")

#%% In [6]
# TODO: Fill code here


#%%
md("""
## Mapping second-order networks
The current Alluvial Generator doesn't support overlapping or multi-level modular structure. However, we can explore such networks individually using the [Network Navigator](http://navigator.mapequation.org). It uses the `.ftree` format as input.

![Network Navigator](http://www.mapequation.org/assets/img/InfomapNetworkNavigator.png)

**TODO:**

- Write a function that takes an input network filename, clusters the network and writes a `.ftree` file
- Generate `.ftree` files for at least one second-order state networks
- Load an `.ftree` file into the [Network Navigator](http://navigator.mapequation.org) and explore the second-order hierarchical structure interactively.
""")

#%% In [7]
# TODO: Fill code here


#%% In [8]
# TODO: Fill code here


