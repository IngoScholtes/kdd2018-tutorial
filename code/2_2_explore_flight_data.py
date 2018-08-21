#%%
import markdown
from IPython.core.display import display, HTML
def md(str):
    display(HTML(markdown.markdown(str + "<br />")))

#%%
md("""
# Mapping quarterly flight path data
Here we make use public data from the Airline Origin and Destination Survey (DB1B) from Bureau of Transportation Statistics (transtats.bts.gov). See https://github.com/mapequation/airline-data for scripts to download and generate this data.

Path data for this tutorial is available on `data/air2015_{q}_paths.net` for each q in [1,2,3,4].
**TODO:**
- Check how one of those files look like (Hint: Use can use `!head [file]` to list the first rows of a file)
""")

#%% In [2]
# TODO: Fill code here


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


#%% In [3]
# TODO: Fill code here


#%% In [4]
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

#%% In [12]
# TODO: Fill code here


#%% In [13]
# TODO: Fill code here


#%%
md("""
### No structure in first-order networks?
In first-order, the network appears too well connected for any modular structure to be revealed. That can be solved in the second-order networks where physical nodes can have overlapping modules. But we may uncover some modular structure even in the first-order networks by scaling down the markov-time to increase the cost of moving between clusters.

#### Reveal first-order structure in tightly connected networks using Markov time
**TODO:**
- Modify the `.map` generating method above to take Infomap flags as input
- Re-run with `--markov-time 0.8`
- Checkout the changes in the Alluvial Generator
""")

#%% In [14]
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

#%% In [21]
# TODO: Fill code here


#%% In [22]
# TODO: Fill code here


