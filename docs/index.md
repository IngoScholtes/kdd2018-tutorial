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

### Session 1: Introduction to Higher-Order Network Analytics
*08:30 - 10:00*

Tutor: [Ingo Scholtes, University of Zurich](http://ifi.uzh.ch/dag)

**Pitch: Higher-Order Network Analytics: A Primer** (20 minutes) | [slides](http://...)
- Welcome and introduction
- Non-Markovian paths in temporal network data
- From graphs to higher-order generative models for paths
- Higher-order centrality measures for temporal network data

**Hands-on Coding Session** (70 minutes)  
Unit | Topic | Notebook | Live Solution
----|----|---- |----  
1.1 | Getting started with Visual Studio Code and `jupyter` | [download](http://...) | [download](http://)  
1.2 | Analysis and visualisation of paths and temporal networks in `pathpy` | [download](http://...) | [download](http://)  
1.3 | Fitting and visualising Higher-Order models | [download](http://...) | [download](http://)  
1.4 | Exploration: Analysis of flight ticket and Metro passenger data | [download](http://...) | [download](http://)  

**Coffee break**  
*10:00 - 10:30*

### Session 2: Multi-order Representation Learning
*10:30 - 12:00*

Tutor: [Ingo Scholtes, University of Zurich](http://ifi.uzh.ch/dag)

**Pitch: Multi-order Representation Learning** (20 minutes) | [slides](http://...)
- Higher- vs. multi-order graphical models
- Representation learning in temporal network data
- Cross-validation of multi-order models

**Hands-on Coding Session** (70 minutes)

Unit | Topic | Notebook | Live Solution
----|----|----|----
2.1 | Model selection and order detection in temporal data | [download](http://...) | [download](http://)  
2.2 | Multi-order network model learning in `pathpy` | [download](http://...) | [download](http://)  
2.3 | Multi-order visualisation of network data | [download](http://...) | [download](http://)  
2.4 | Exploration: Optimal node ranking in dynamic social networks | [download](http://...) | [download](http://)  

**Lunch break**  
*12:00 - 13:30*

### Session 3: Variable-order Models with BuildHON and HONViz
*13:30 - 14:30*

Tutor: [Nitesh Chawla, University of Notre Dame](https://www3.nd.edu/~nchawla/)

**Coffee break**  
*14:30 - 15:00*

**Session 4: Graph Clustering with InfoMap**  
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

**Coffee break**  
*16:30 - 17:00*

### Session 4: Higher-order Graph Clustering and Visualisation
*17:00 - 18:30*

Tutor: [Daniel Edler, Ume&aring; University](https://www.umu.se/en/staff/daniel-edler/)

*Higher-Order Community Detection with InfoMap* (30 minutes) | [slides](http://...)
- Memory Networks and the Higher-Order MapEquation
- State Lumping Algorithms
- ... 
- ... 

*Hands-on Coding Session* (60 minutes)
- Interactive Visualisation with InfoBaleen

# Setting up the environment

Hands-on sessions will be completed in `python`. A detailed description on how to set up the environment can be found in the [setup instructions](/kdd2018-tutorial/setup).