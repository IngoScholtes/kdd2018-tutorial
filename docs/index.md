---
title: KDD 2018 - Hands-on Tutorial on Higher-Order Data Analytics
permalink: /
---
# Tutorial Outline

On this companion page you can find accompanying software, data, and `jupyter` notebooks for the KDD2018 Hands-on Tutorial [Beyond Graph Mining: Higher-Order Data Analytics for Temporal Network Data](). the tutorial will follow the following outline: 

**Session 1: Introduction to Higher-Order Network Models**
- *Lecture:* Higher-order Models of Temporal Network Data (45 minutes)
- *Tutorial:* Learning Optimal Network Models in Time Series Data (45 minutes)

**Session 2: Higher-Order Graph Clustering**
- *Lecture:* Higher-order Graph Clustering with the MapEquation (45 minutes)
- *Tutorial:* Clustering Citation Flows using InfoMap (45 minutes)

**Session 3: Higher-Order Node Ranking**
- *Lecture:* Higher-order Centrality Measures (45 minutes)
- *Tutorial:* Predicting click rates with Higher-order PageRank (45 minutes)

**Session 4: Higher-order Network Visualisation**
- *Tutorial:* Higher-order network visualisation in d3js (45 minutes)
- *Tutorial:* Alluvial diagrams with d3js (45 minutes)

# Setting up the environment

To complete the hands-on exercises, you will need a working `python 3.x` environment, installed under the operating system of your choice. For Windows, macOS, and Linux users we recommend using the latest [Anaconda 5.2](https://www.anaconda.com/download/) installation. To complete the exercises, we further highly recommend using the development environment [Visual Studio Code](https://code.visualstudio.com/Download), an OpenSource code editor available for Windows, macOS, and Linux. Once you have installed Visual Studio Code, please additionally install the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter](https://marketplace.visualstudio.com/items?itemName=donjayamanne.jupyter) extensions, which are available free of charge via Visual Studio Code's integrated extension marketplace.

To apply higher-order data analytics to real data, we finally need to set up two additional software packages, which can be installed via gitHub.

[pathpy](http://www.pathpy.net) is a python package for the analysis of time-stamped and sequential data on complex networks. [InfoMap](http://www.mapequation.org) provides code to reveal overlapping modular patterns in higher-order network flows through complex systems. In the following, we explain how you can set up these two packages: 

## Setting up InfoMap

...

## Setting up pathpy

`pathpy` is pure python code. It has no platform-specific dependencies and should thus work on all platforms. It builds on `numpy` and `scipy` which come preinstalled in the Anaconda 5.2 environment. The latest version of `pathpy` can be installed by typing:

`> pip install git+git://github.com/IngoScholtes/pathpy.git`