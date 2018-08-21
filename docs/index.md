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

The tutorial will take place on **Wednesday August 22, 2018** from **08:30 - 17:10** in ICC Capital Suite Room 2+3+4 of the [ExCel London](https://www.excel.london/organiser/venue-map), 1 Western Gateway, Royal Victoria Dock, London, E16 1FR.

# Prerequisites

Participants should bring a laptop with a python 3.x environment. See [setup instructions](/kdd2018-tutorial/setup). Some basic prior exposure to python is beneficial. In the first session of the tutorial we will give a brief introduction to interactive data science with python, jupyter notebook, and VS Code.

# Schedule

The tutorial consists of three separate blocks, in which we give an overview of three different software frameworks for higher-order network analysis.

## Block I: Higher-Order Network Analytics with [pathpy](http://www.pathpy.net)

### Session: Introduction to Higher-Order Network Analytics
*08:30 - 09:30*

Tutor: [Ingo Scholtes, Data Analytics Group, University of Zurich](http://ifi.uzh.ch/dag)

**Welcome Note and Tutorial Overview**  

**Intro: Higher-Order Network Analytics for Time Series Data** (30 min) | [slides](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/talks/)  
- Causal paths in temporal network data
- Ordering matters in time series data
- Higher-order generative models for causal paths
- Representation learning in temporal network data


**Live Coding** (30 min)  

Unit | Topic | Notebook | Live Solution
----|----|----|----
1.1 | A Primer to Data Science with `python`, `jupyter`, `git` and `VS Code` (15 min) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/1_1_vscode_jupyter.py) | N/A
1.2 | Analysis and Visualisation of Path Data in [`pathpy`](http://www.pathpy.net) (15 min) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/1_2_pathpy.py), [.ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/1_2_pathpy.ipynb) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/live_solutions/1_2_pathpy.py)  

### KDD Coffee break
*09:30 - 10:00*

### Session: Multi-order Representation Learning
*10:00 - 12:00*

Tutor: [Ingo Scholtes, Data Analytics Group, University of Zurich](http://ifi.uzh.ch/dag)

**Live Coding** (120 min)

Unit | Topic | Notebook | Live Solution
----|----|----|----
1.3 | Fitting and Visualising Higher-order Network Models (15 min) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/1_3_higher_order.py),  [.ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/1_3_higher_order.ipynb) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/live_solutions/1_3_higher_order.py)
1.4 | Exploration: Higher-order Analysis of [real-world data](https://github.com/IngoScholtes/kdd2018-tutorial/tree/master/data) (20 min) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/1_4_exploration.py), [.ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/1_4_exploration.ipynb) | N/A
2.1 | Time-stamped Network Analysis in [`pathpy`](http://www.pathpy.net) (20 min) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/2_1_temporal_networks.py), [.ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/2_1_temporal_networks.ipynb) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/live_solutions/2_1_temporal_networks.py)
2.2 | Multi-order Representation Learning (20 min) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/2_2_multi_order.py), [.ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/2_2_multi_order.ipynb) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/live_solutions/2_2_multi_order.py)  
2.3 | Optimal Higher-order Analytics for Temporal Data (20 min) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/2_3_cross_validation.py), [.ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/2_3_cross_validation.ipynb) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/live_solutions/2_3_cross_validation.py)
2.4 | Exploration: Multi-order Analysis of [Time-stamped Social Networks](https://github.com/IngoScholtes/kdd2018-tutorial/tree/master/data) (30 min) | [.py](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/2_4_exploration.py),  [.ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/2_4_exploration.ipynb) | N/A

### KDD Lunch break 
*12:00 - 13:30*

## Block II: Introduction to Higher-Order Graph Clustering with [Infomap](http://www.mapequation.org)

### Session: Introduction to Flow Compression 
*13:30 - 15:30*

Tutor: [Daniel Edler, Ume&aring; University](https://www.umu.se/en/staff/daniel-edler/)

**Intro:** Flow Compression with the MapEquation (45 minutes) | [Slides](https://www.dropbox.com/s/wd48ejqjohrviss/KDD2018mapequation.pdf?dl=0)
- Coding theory: The minimum description length principle
- Compression of modular network flows: The MapEquation
- Multilevel partitions

**Live Coding** (75 min)
- Introducing `Infomap`
- Community detection in first-order models
- Mapping change in modular networks
- Generation of first- and second order networks from paths
- Interactive Visualisation of second-order hierarchical clusters

### KDD Coffee break
*15:30 - 16:00*

### Session: Higher-order Graph Clustering and Visualisation
*16:00 - 17:00*

Tutor: [Daniel Edler, Ume&aring; University](https://www.umu.se/en/staff/daniel-edler/)

**Live Coding** (60 min)
- From pathways to networks with and without memory
- Sparse Markov chain models
- Higher-order clustering with Infomap
- Interactive visualisation of hierarchical clusters

### Tutorial Closing 
*17:00 - 17:10*

## Block III: Variable-order Analytics with BuildHON/HONVis

Tutor: [Nitesh Chawla, University of Notre Dame](https://www3.nd.edu/~nchawla/)

Due to unforeseen circumstances, the tutor could not attend KDD'18. This block will thus be a 1 hour virtual self-study session. Participants can find the tutorial material in the gitHub repository.

**Intro:** Representing variable orders in networks (30 min) | [slides](http://www.jianxu.net/en/files/HON_Xu_KDD_2018.ppsx)
- Introduction to higher-order network
- Why variable orders?
- BuildHON algorithm in a nutshell
- Real-world applications

**Live Demo** (30 min) | [slides](http://www.jianxu.net/en/files/HON_Xu_KDD_2018_HandsOnTasks.ppsx)
- Synthesising trajectories with known variable orders of dependencies
- Use BuildHON+ (parameter-free) to extract variable orders of dependencies and build HON
- Use HONVis to visualize and interactively explore the higher-order network of NYC taxi data


# Data sets

A description of data sets that will be provided to participants, and which will be analysed in the tutorial is available [here](https://github.com/IngoScholtes/kdd2018-tutorial/tree/master/data).

# Setting up the environment

Hands-on sessions will be completed in `python`. A detailed description on how to set up the environment can be found in the [setup instructions](/kdd2018-tutorial/setup).
