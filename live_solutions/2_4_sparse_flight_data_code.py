#%%
import markdown
from IPython.core.display import display, HTML
def md(str):
    display(HTML(markdown.markdown(str + "<br />")))

#%% In [1]
from random import random

def generateData(inputFilenames):
    """Merge path data from inputFilenames and write to two path data files
    for training and validation. Each path in the input data is selected by
    random to be written to either the training or validation data file"""
    data = { 'training': [], 'validation': [] }
    # Read path data
    for filename in inputFilenames:
        print("Parsing paths from '{}'...".format(filename))
        with open(filename, mode='r') as infile:
            # Skip heading
            next(infile)
            for row in infile:
                if random() < 0.5:
                    data['validation'].append(row)
                else:
                    data['training'].append(row)
    # Write path data
    for name, paths in data.items():
        outFilename = "output/paths_{}.net".format(name)
        print("Writing {} paths to {}...".format(len(paths), outFilename))
        with open(outFilename, mode='w') as outfile:
            outfile.write("*paths\n")
            for p in paths:
                outfile.write(p)

inputFilenames = ["data/air2015_{}_paths.net".format(quarter) for quarter in [1,2,3,4]]
generateData(inputFilenames)

#%% In [2]
import infomap

def generateStateNetworkFromPaths(inputFilename, outputFilename, markovOrder):
    network = infomap.Network(infomap.Config("--directed --path-markov-order {}".format(markovOrder)))
    network.readInputData(inputFilename)
    network.writeStateNetwork(outputFilename)

generateStateNetworkFromPaths("output/paths_training.net", "output/states_training_order_2.net", 2)
generateStateNetworkFromPaths("output/paths_validation.net", "output/states_validation_order_2.net", 2)

#%% In [3]
import matplotlib.pyplot as plt
import numpy as np
from state_lumping_network import StateNetwork

sparseNet = StateNetwork()
sparseNet.readFromFile("output/states_training_order_2.net")

h0 = sparseNet.calcEntropyRate()
print("Original average entropy rate:", h0)

clusterRates = np.linspace(0.1, 1, 10)
# clusterRates = [0.25, 0.5, 0.75]
# clusterRates = [0.5]
numStates = []
entropyRate = []

for i, clusterRate in enumerate(clusterRates):
    sparseNet.clusterStateNodes(clusterRate=clusterRate)
    s = sparseNet.numLumpedStateNodes()
    h = sparseNet.calcLumpedEntropyRate()
    sparseNet.writeLumpedStateNetwork("output/states_training_lumped_{}.net".format(i))
    numStates.append(s)
    entropyRate.append(h)

#%% In [4]
plt.plot(numStates, entropyRate, marker='o')
plt.xlabel("number of lumped states")
plt.ylabel("entropy rate")
plt.axhline(y=h0, color='r', linestyle='-')
# plt.axvline(x=sparseNet.numStateNodes(), color='r')
plt.show()

