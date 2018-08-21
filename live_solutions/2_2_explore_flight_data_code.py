#%%
import markdown
from IPython.core.display import display, HTML
def md(str):
    display(HTML(markdown.markdown(str + "<br />")))

#%% In [1]
!head data/air2015_1_paths.net

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

#%% In [7]
for quarter in [1,2,3,4]:
    inputFilename = "output/air2015_{}_order_1.net".format(quarter)
    createMap(inputFilename, flags="--directed --markov-time 0.8")

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

