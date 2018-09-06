---
title: KDD 2018 - Hands-on Tutorial on Higher-Order Data Analytics
permalink: /pathpy
---

# pathpy Tutorial

In this tutorial, we will give an in-depth introduction to the Open Source python data analytics package `pathpy`. We illustrate the theoretical foundations of higher- and multi-order network models in toy examples, and we will demonstrate their advantages in real-world time series data on complex networks. The latest version of `pathpy` is publicly available via the [python package index](https://pypi.org/project/pathpy2/). You can simply install it by typing:

```
pip install pathpy2
```

`pathpy` is fully integrated with `jupyter` notebooks, providing in-line, interactive and dynamic visualisations of graphs and networks, temporal networks, as well as higher- and multi-order network models. This teaser video highlights some of its features:

[![Watch promotional video](https://img.youtube.com/vi/QIPqFaR2Z5c/0.jpg)](https://www.youtube.com/watch?v=QIPqFaR2Z5c)

The following video explains the science behind `pathpy`:

[![Watch promotional video](https://img.youtube.com/vi/CxJkVrD2ZlM/0.jpg)](https://www.youtube.com/watch?v=CxJkVrD2ZlM)

You can find the technical details in the following publications:

1. I Scholtes: [When is a network a network? Multi-Order Graphical Model Selection in Pathways and Temporal Networks](http://dl.acm.org/citation.cfm?id=3098145), In KDD'17 - Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Halifax, Nova Scotia, Canada, August 13-17, 2017
2. I Scholtes, N Wider, A Garas: [Higher-Order Aggregate Networks in the Analysis of Temporal Networks: Path structures and centralities](http://dx.doi.org/10.1140/epjb/e2016-60663-0), The European Physical Journal B, 89:61, March 2016
3. I Scholtes, N Wider, R Pfitzner, A Garas, CJ Tessone, F Schweitzer: [Causality-driven slow-down and speed-up of diffusion in non-Markovian temporal networks](http://www.nature.com/ncomms/2014/140924/ncomms6024/full/ncomms6024.html), Nature Communications, 5, September 2014
4. R Pfitzner, I Scholtes, A Garas, CJ Tessone, F Schweitzer: [Betweenness preference: Quantifying correlations in the topological dynamics of temporal networks](http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.110.198701), Phys Rev Lett, 110(19), 198701, May 2013


Having completed a brief introduction to interactive data science with `python`, `Visual Studio Code`, and `jupyter` in [unit 1](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/1_1_vscode_jupyter.py), this tutorial consists of seven units (20 - 30 minutes each). For each unit we provide a stand-alone HTML file, as well as a juypter notebook that you can download and run on your own machine. In unit 5 and 8 we invite you to use `pathpy` to explore higher- and multi-order models on your own.


Unit | Topic | notebook  
------|-----|-----
2 | [Introducing `pathpy`](https://htmlpreview.github.io/?https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/solutions/1_2_pathpy.html) | [ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/solutions/1_2_pathpy.ipynb)  
3 | [Higher-order analysis of path data](https://htmlpreview.github.io/?https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/solutions/1_3_higher_order.html) | [ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/solutions/1_3_higher_order.ipynb)  
4 | [Temporal Network Analysis and Visualisation](https://htmlpreview.github.io/?https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/solutions/1_4_temporal_networks.html) | [ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/solutions/1_4_temporal_networks.ipynb)  
5 | [Exploration: Higher-order analysis of time series data](https://htmlpreview.github.io/?https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/solutions/1_5_exploration.html) | [ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/solutions/1_5_exploration.ipynb)  
6 | [Multi-order Representation Learning](https://htmlpreview.github.io/?https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/solutions/1_6_multi_order.html) | [ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/solutions/1_6_multi_order.ipynb)  
7 | [Optimal higher-order analysis of temporal data](https://htmlpreview.github.io/?https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/solutions/1_7_optimal_analysis.html)| [ipnyb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/solutions/1_7_optimal_analysis.ipynb)  
8 | [Exploration: Representation learning in time series data](https://htmlpreview.github.io/?https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/solutions/1_8_exploration.html) | [ipynb](https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/solutions/1_8_exploration.ipynb)  


`pathpy` is brought to you by the [Data Analytics Group](http://www.ifi.uzh.ch/dag) at the [IfI](http://www.ifi.uzh.ch) of [University of Zurich](http://www.uzh.ch). Feel free to [contact us](http://www.ifi.uzh.ch/dag) if you want to host an interaction hands-on tutorial session in your group, institute, or company.