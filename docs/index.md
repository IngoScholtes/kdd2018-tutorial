---
title: KDD 2018 - Hands-on Tutorial on Higher-Order Data Analytics
permalink: /
---
# Tutorial Outline

On this companion page you can find accompanying software, data, and `jupyter` notebooks for the KDD2018 Hands-on Tutorial [Beyond Graph Mining: Higher-Order Data Analytics for Temporal Network Data](). The detailed program of this tutorial is as follows:

**Session 1: Introduction to Higher-Order Network Analytics **
* 08:30 - 10:00 *

Higher-Order Models of Causal Topologies in Time Series Network Data (30 minutes) [download slides](http://...)
- Network analytics for time series data
- Non-Markovian paths in temporal data streams
- From graphs to higher-order generative models for paths 
- Higher-order representation learning

*Hands-on Coding Session* (60 minutes)
- Task 1: Getting started with Visual Studio Code, `jupyter` and `pathpy` [download notebook](http://...)
- Task 2: Working with path data in `pathpy` [download notebook](http://...)
- Task 3: Multi-order representation learning [download notebook](http://...)
- Task 4: Visualising higher-order network models and non-Markovian paths [download notebook](http://...)

*Data sets*
- flight itinerary data of a major US airline [download](http://...)
- passenger itineraries in the London Tube metro network [download](http://...)
- clickstreams of Wikipedia users [download](http://...)

** Coffee break **
* 10:00 - 10:30 *

**Session 2: Higher-Order Temporal Network Analysis**
* 10:30 - 10:00 *

Introduction to Temporal Network Analysis (30 minutes) [download slides](http://...)
- Causal paths in time-stamped network data
- Inference of inherent time scales in temporal networks
- Causal paths and temporal centrality measures
- Higher-order generalisations of centrality measures

*Hands-on Coding Session* (60 minutes)
- Task 1: Working with temporal network data in `pathpy` [download notebook](http://...)
- Task 2: Interactive visualisation of temporal networks in `pathpy` [download notebook](http://...)
- Task 3: Calculating causal paths in temporal networks [download notebook](http://...)
- Task 4: Higher-order node ranking in dynamic social networks [download notebook](http://...)

*Data sets* 
- Time-stamped developer communication in an OpenSource community [download data](http://...)
- Time-stamped proximity relations of hospital staff [download data](http://...)
- Time-stamped E-Mail communication in a company [download data](http://...)

** Lunch break **
* 12:00 - 13:30 *

**Session 3: Graph Clustering with InfoMap**
* 13:30 - 15:00 *

*Introduction to Flow Compression with the MapEquation* (30 minutes) [download slides](http://...)
- Introduction to graph clustering
- Flow Compression: The MapEquation
- Minimisation of Modular Description Length
- Second-order Flow Compression in trigram data

*Hands-on Coding Session* (60 minutes)
- Getting started with `InfoMap` [download notebook](http://...)
- Community detection in first-order models [download notebook](http://...)
- ... [download notebook](http://...)
- ... [download notebook](http://...)

*Data Sets*
- ...

**Session 4: Higher-order Graph Clustering and Visualisation**

* Introduction to HigherOrder Community Detection with InfoMap (30 minutes) [download slides](http://...)
- Memory Networks and the Higher-Order MapEquation
- State Lumping Algorithms
- ... 
- ... 

* Hands-on Coding Session* (60 minutes)
- Task 1: ... [download notebook](http://...)
- Task 2: ... [download notebook](http://...)
- Task 3: ... [download notebook](http://...)
- Task 4: Interactive Visualisation with InfoBaleen [download notebook](http://...)

*Data Sets*
- ...

# Setting up the environment

To complete the hands-on exercises, you will need a working `python 3.x` environment, installed under the operating system of your choice. For Windows, macOS, and Linux users we recommend using the latest [Anaconda 5.2](https://www.anaconda.com/download/) installation. 

To complete the exercises, we highly recommend using the development environment [Visual Studio Code](https://code.visualstudio.com/Download), an OpenSource code editor available for Windows, macOS, and Linux. Once you have installed Visual Studio Code, please install the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter](https://marketplace.visualstudio.com/items?itemName=donjayamanne.jupyter) extensions, which are available free of charge via Visual Studio Code's integrated extension marketplace.

To apply higher-order data analytics to real data, we finally need to set up two additional software packages, which can be installed via gitHub.

[pathpy](http://www.pathpy.net) is a python package for the analysis of time-stamped and sequential data on complex networks. [InfoMap](http://www.mapequation.org) provides code to reveal overlapping modular patterns in higher-order network flows through complex systems. In the following, we explain how you can set up these two packages: 

## Setting up InfoMap

...

## Setting up pathpy

`pathpy` is pure python code. It has no platform-specific dependencies and should thus work on all platforms. It builds on `numpy` and `scipy` which come preinstalled in the Anaconda 5.2 environment. Assuming that a `python 3.x` environment has been successfully installed as described above, the latest version of `pathpy` can be installed in either of the following ways, both of which are identical for the sake of this tutorial.

The first method uses the latest version available via the [python package index pypi](https://pypi.org/). For this, you should open a termin window on your machine and type:

`> pip install pathpy`

The second method installs the latest development version directly from the `pathpy` gitHub repository. For this you should type 

`> pip install git+git://github.com/IngoScholtes/pathpy.git`

