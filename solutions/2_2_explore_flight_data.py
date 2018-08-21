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

#%% In [1]
!head data/air2015_1_paths.net

#%%
md("""
## Generate state networks of first and second order

**TODO:**
- Import infomap
- Write a function to generate a state network of specified Markov order from path data and write to output dir
- Generate first and second order state networks for all four quarters
""")

#%% In [2]
import infomap

#%% In [11]
def generateStateNetworkFromPaths(inputFilename, outputFilename, markovOrder):
    network = infomap.Network(infomap.Config("--directed --path-markov-order {}".format(markovOrder)))
    network.readInputData(inputFilename)
    network.writeStateNetwork(outputFilename)
    print("State network of order {} written to {}".format(markovOrder, outputFilename))

#%% In [12]
for quarter in [1,2,3,4]:
    inputFilename = "data/air2015_{}_paths.net".format(quarter)
    for order in [1,2]:
        outputFilename = "output/air2015_{}_order_{}.net".format(quarter, order)
        generateStateNetworkFromPaths(inputFilename, outputFilename, order)

#%%
md("""
## Mapping change in first-order networks with Alluvial Diagram

![alluvial-diagram](http://www.mapequation.org/assets/img/neuroAlluvial2001-2007.svg)


**TODO:**
- Write a function that takes an input network filename, clusters the network and writes a `.map` file
- Generate `.map` files for all four first-order state networks
- Load the `.map` files into the [Alluvial Generator](http://www.mapequation.org/apps/MapGenerator.html) and explore the modular structure over time
""")

#%% In [5]
def createMap(inputFilename, flags = "--directed"):
    print("Cluster '{}'...".format(inputFilename))
    name = inputFilename.rsplit(".", maxsplit=1)[0].split('/')[-1]
    infomap1 = infomap.Infomap(flags)
    infomap1.network().readInputData(inputFilename)
    infomap1.run()
    print(" -> Found {} top modules with codelength {}".format(infomap1.numTopModules(), infomap1.codelength()))
    mapFilename = "output/{}.map".format(name)
    infomap1.writeMap(mapFilename)
    print(" -> Wrote .map file to '{}'".format(mapFilename))

#%% In [6]
for quarter in [1,2,3,4]:
    inputFilename = "output/air2015_{}_order_1.net".format(quarter)
    createMap(inputFilename)

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

#%% In [7]
for quarter in [1,2,3,4]:
    inputFilename = "output/air2015_{}_order_1.net".format(quarter)
    createMap(inputFilename, flags="--directed --markov-time 0.8")

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

#%% In [8]
def createFlowTree(inputFilename, flags = "--directed"):
    print("Cluster '{}'...".format(inputFilename))
    name = inputFilename.rsplit(".", maxsplit=1)[0].split('/')[-1]
    infomap2 = infomap.Infomap(flags)
    infomap2.network().readInputData(inputFilename)
    infomap2.run()
    print(" -> Found {} top modules with codelength {}".format(infomap2.numTopModules(), infomap2.codelength()))
    ftreeFilename = "output/{}.ftree".format(name)
    infomap2.writeFlowTree(ftreeFilename)
    print(" -> Wrote .ftree file to '{}'".format(ftreeFilename))

#%% In [9]
for quarter in [1,2,3,4]:
    inputFilename = "output/air2015_{}_order_2.net".format(quarter)
    createFlowTree(inputFilename)

