---
title: KDD 2018 - Hands-on Tutorial on Higher-Order Data Analytics
permalink: /
---

# Tutorial Outline

Network-based data mining techniques such as graph mining, (social) network analysis, link prediction and graph clustering form an important foundation for data science applications in computer science, computational social science, and the life sciences. They help to detect patterns in large data sets that capture dyadic relations between pairs of genes, species, humans, or documents and they have improved our understanding of complex networks.

While the potential of analysing graph or network representations of relational data is undisputed, we increasingly have access to data on networks that contain more than just dyadic relations. Consider, e.g., data on user click streams in the Web, time-stamped social networks, gene regulatory pathways, or time-stamped financial transactions. These are examples for time-resolved or sequential data that not only tell us who is related to whom but also when and in which order relations occur. Recent works have exposed that the timing and ordering of relations in such data can introduce higher-order, non-dyadic dependencies that are not captured by state-of-the-art graph representations. This oversimplification questions the validity of graph mining techniques in time series data and poses a threat for interdisciplinary applications of network analytics.


To address this challenge, researchers have developed advanced graph modelling and representation techniques based on higher- and variable-order Markov models, which enable us to model non-Markovian characteristics in time series data on networks. Introducing this exciting research field, the goal of this tutorial is to give an overview of cutting-edge higher-order data analytics techniques. Key takeaways for attendees will be (i) a solid understanding of higher-order network modelling and representation learning techniques, (ii) hands-on experience with state-of-the-art higher-order network analytics and visualisation packages, and (iii) a clear demonstration of the benefits of higher-order data analytics in real-world time series data on technical, social, and ecological systems.

A detailed summary of the topics, literature, and tools covered in this hands-on tutorial can be found in the [tutorial paper](https://www.researchgate.net/publication/325168357_Beyond_Graph_Mining_Higher-Order_Data_Analytics_for_Temporal_Network_Data).

# When and where

The tutorial will take place on **Wednesday August 22, 2018** in ICC Capital Suite Room 2+3+4 of the [ExCel London](https://www.excel.london/organiser/venue-map), 1 Western Gateway, Royal Victoria Dock, London, E16 1FR.

# Schedule

The schedule of the tutorial is as follows:

## Session 1: Introduction to Higher-Order Network Analytics
*08:30 - 10:00*

Tutor: [Ingo Scholtes, Data Analytics Group, University of Zurich](http://ifi.uzh.ch/dag)

**Pitch:** Higher-Order Network Analytics for Temporal Network Data (20 min) | [slides](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/talks/)
- Welcome note and Tutorial Overview
- Higher-order dependencies and Non-Markovian paths in temporal network data
- From graphs to higher-order generative models for paths
- Higher-order network analytics for time series data

**Live Coding** (75 min)  

Unit | Topic | Notebook | Live Solution
----|----|----|----
1.1 | Data science with `python` and `jupyter` in `VSCode` (15 min) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/1_1_vscode_jupyter.py) | N/A
1.2 | Analysis and visualisation of path statistics in [`pathpy`](http://www.pathpy.net) (15 min) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/1_2_pathpy.py), [.ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/1_2_pathpy.ipynb) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/live_solutions/1_2_pathpy.py)  
1.3 | Fitting and visualising Higher-order network models (15 min) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/1_3_higher_order.py),  [.ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/1_3_higher_order.ipynb) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/live_solutions/1_3_higher_order.py)
1.4 | Exploration: Higher-order analysis of [real-world pathway data](https://github.com/IngoScholtes/kdd2018-tutorial/tree/master/data) (30 min) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/1_4_exploration.py), [.ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/1_4_exploration.ipynb) | N/A

### Coffee break
*10:00 - 10:30*

## Session 2: Multi-order Representation Learning
*10:30 - 12:00*

Tutor: [Ingo Scholtes, Data Analytics Group, University of Zurich](http://ifi.uzh.ch/dag)

**Pitch:** Representation Learning: From Higher- to Optimal Multi-Order Models (15 min) | [slides](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/talks/)
- Higher- vs. multi-order graphical models
- Representation learning in temporal network data
- Cross-validation of multi-order models

**Live Coding** (75 min)

Unit | Topic | Notebook | Live Solution
----|----|----|----
2.1 | Higher-order analysis of time-stamped network data in [`pathpy`](http://www.pathpy.net) (15 min) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/2_1_temporal_networks.py), [.ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/2_1_temporal_networks.ipynb) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/live_solutions/2_1_temporal_networks.py)  
2.2 | Multi-order representation learning with [`pathpy`](http://www.pathpy.net) (15 min) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/2_2_multi_order.py), [.ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/2_2_multi_order.ipynb) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/live_solutions/2_2_multi_order.py)  
2.3 | Optimal node ranking in dynamic social networks (15 min) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/2_3_cross_validation.py), [.ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/2_3_cross_validation.ipynb) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/live_solutions/2_3_cross_validation.py)
2.4 | Exploration: Multi-order representation learning in [time-stamped social networks](https://github.com/IngoScholtes/kdd2018-tutorial/tree/master/data) (30 min) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/2_4_exploration.py),  [.ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/2_4_exploration.ipynb) | N/A

### Lunch break
*12:00 - 13:30*

## Session 3: Variable-order Models with BuildHON and HONViz
*13:30 - 14:30*

Tutor: [Nitesh Chawla, University of Notre Dame](https://www3.nd.edu/~nchawla/)

### Coffee break
*14:30 - 15:00*

## Session 4: Graph Clustering with InfoMap
*15:00 - 16:30*

Tutor: [Daniel Edler, Ume&aring; University](https://www.umu.se/en/staff/daniel-edler/)

*Introduction to Flow Compression with the MapEquation* (30 minutes) | [slides](http://...)
- Introduction to graph clustering
- Flow Compression: The MapEquation
- Minimisation of Modular Description Length
- Second-order Flow Compression in trigram data

*Hands-on Coding Session* (60 minutes) | [notebook](http://...)
- Getting started with `InfoMap`
- Community detection in first-order models
- Community detection in higher-order models
- Exploration: ... 

### Coffee break
*16:30 - 17:00*

## Session 5: Higher-order Graph Clustering and Visualisation
*17:00 - 18:30*

Tutor: [Daniel Edler, Ume&aring; University](https://www.umu.se/en/staff/daniel-edler/)

*Higher-Order Community Detection with InfoMap* (30 minutes) | [slides](http://...)
- Memory Networks and the Higher-Order MapEquation
- State Lumping Algorithms
- ... 
- ... 

*Hands-on Coding Session* (60 minutes)
- Interactive Visualisation with InfoBaleen

# Data sets

A description of data sets that will be provided to tutorial participants, and that will be analysed in the tutorial is available [here](https://github.com/IngoScholtes/kdd2018-tutorial/tree/master/data).

# Setting up the environment

Hands-on sessions will be completed in `python`. A detailed description on how to set up the environment can be found in the [setup instructions](/kdd2018-tutorial/setup).