#%%
import markdown
from IPython.core.display import display, HTML
def md(str):
    display(HTML(markdown.markdown(str + "<br />")))

#%%
md("""
# Higher-Order Data Analytics for Temporal Network Data

## 1.3 Higher-order analysis of path data in `pathpy`

**Ingo Scholtes**  
Data Analytics Group  
Department of Informatics (IfI)  
University of Zurich  


**August 22 2018**
""")

#%%
md("""
The real purpose of `pathpy` is to fit and analyse higher-order network models. For this we can use the class `HigherOrderNetwork`, which is summarised below:

<span style="color:red">**TODO:** Import the module pathpy and print the documentation of class `pp.HigherOrderNetwork`</span>
""")

#%% In [1]


#%%
md("""
An important motivation for higher-order network analytics is to view standard graphs or networks as **first-order generative model** for paths in real complex systems. As we have seen in the previous unit 1.1, these models only consider **first-order dyad statistics** (i.e. edge frequencies) but ignore higher-order dependencies in real-world pat, sequence, or time-stamped data.

The following works hve studied measures for higher-order correlations in such data and have generalised network models to higher-order models with arbitrary order: 

- R Pfitzner, I Scholtes, A Garas, CJ Tessone, F Schweitzer: **Betweenness Preference: Quantifying Correlations in the Topological Dynamics of Temporal Networks**, In Physical Review Letters, May 2013, [arXiv 1208.0588](http://arxiv.org/abs/1208.0588)

- I Scholtes, N Wider, R Pfitzner, A Garas, CJ Tessone, F Schweitzer: **Causality-driven slow-down and speed-up of diffusion in non-Markovian temporal networks**, In Nature Communications, September 2014, [arXiv 1307.4030](http://arxiv.org/abs/1307.4030)

- I Scholtes, N Wider, A Garas: **Higher-Order Aggregate Networks in the Analysis of Temporal Networks: Path structures and centralities**, In The European Physical Journal B, March 2016, [arXiv 1508.06467](http://arxiv.org/abs/1508.06467) 

- Yan Zhang, Antonios Garas, Ingo Scholtes: **Controllability of temporal networks: An analysis using higher-order networks**, preprint, January 2017,  [arXiv 1701.06331](https://arxiv.org/abs/1701.06331)

- I Scholtes: **When is a Network a Network? Multi-Order Graphical Model Selection in Pathways and Temporal Networks**, In KDD'17, February 2017, [arXiv 1702.05499](https://arxiv.org/abs/1702.05499)

You can further find an overview of this topic in the following preprint:

- R Lambiotte, M Rosvall, I Scholtes: **Understanding Complex Systems: From Networks to Optimal Higher-Order Models**, preprint, June 2018,  [arXiv 1806.05977](https://arxiv.org/abs/1806.05977)
""")

#%%
md("""
The data analysis and modelling framework outlined in these works builds on a generalisation of standard, first-order networks to $k$-dimensional De Bruijn graph models for paths in complex networks. 

The class `HigherOrderNetwork` allows us to generate such higher-order network models of paths. In the documentation, we find that the constructor of this class takes a parameter `paths`, in which we specify the path statistics that we want to model. The parameter `k` allows us to specify the order $k$ of the higher-order model that we want to fit to the path statistics.

To understand this better, let us consider our toy example from before.

<span style="color:red">**TODO:** Read the toy example from unit 1.2 from the file `data/toy_paths.ngram`, generate a **first-order** model instance `hon_1` and print a summary of the resulting instance.</span>
""")

#%% In [2]


#%%
md("""
We obtain a simple first-order model of our paths, with five nodes $a,b,c,d$ and $e$, and four links $(a,c), (b,c), (c,d), (c,e)$. This is identicaly to the `Network` instance that we have created using the `Network.from_paths` function in unit 1.1. Indeed, each `HigherOrderNetwork` instance is derived from the class `Network`, which means we can store edge and node attributes and visualise it using exactly the same methods:

<span style="color:red">**TODO:** Plot the `HigherOrderModel` instance `hon_1` and print the weight of all edges.</span>
""")

#%% In [3]


#%%
md("""
The output above confirms that the higher-order model with order $k=1$ is identical to our standard network model. However, we see that the weights are actually vector-valued, where the first entry again captures the sub-path frequency while the second entry is the number of occurrences as longest path. 

As mentioned before, we can see this network as a **first-order model** for paths where **nodes are zero-length paths** and **edges are paths of length one**. That is, in a model with order $k=1$ edge weights capture the statistics of (sub-paths) of length $k=1$.

We can generalise this idea to **k-th-order models** for paths, where **nodes are paths of length $k-1$** while the statistics of **paths of length $k$ are captured by edges**. In general, we obtain a $k$-th order model by performing a line graph transformation on the model with order $k-1$. That is, edges in the model of order $k-1$ become nodes in the model with order $k$. We then draw edges between higher-order nodes that represent a path of length $k$. 

The result is a $k$-dimensional De Bruijn graph model for paths. Let us try this in our example.

<span style="color:red">**TODO:** Create a second-order model `hon_2` for `toy_paths`. Visualise the model and print the weights of all edges.</span>
""")

#%% In [13]


#%%
md("""
We see that each of the four **edges** in the first-order model is now represented by a **node** in this second-order model. We further have two edges $(a-c, c-d)$ and $(b-c,c-e)$ that represent the two paths of length two that occur in our data.

This is important because it captures to what extent the paths that we observe in our data deviate from what we would expect based on the (first-order) network topology of the system. Here, all four paths $a \rightarrow c \rightarrow d, a \rightarrow c \rightarrow e, b \rightarrow c \rightarrow d$ and $b \rightarrow c \rightarrow e$ of length two are possible. 

Even more, if edges were statistically independent we would expect those four paths to occur with the same frequency. Another way to express this independence assumption is to consider Markov chain models for the sequences of nodes traversed by paths. If these sequences are generated by a memoryless first-order Markov process we expect, e.g. paths $a \rightarrow c \rightarrow d$ and $a \rightarrow c \rightarrow e$ to occur with the same probability. In our case, since we have 20 observed paths of length two, we would expect that each of them occurs (on average) 5 times.

We can actually represent this **null-model** for paths as a second-order model, where edge statistics capture the expected frequency of edges if paths were generated by a memoryless process. This allows us to directly compare how the observed path statistics deviate from the (Markovian) expectation.

<span style="color:red">**TODO:** Use the `null_model` parameter in the constructor of `HigherOrderNetwork` to generate a second-order null model `hon_2_null` for `toy_paths`. Visualise the model and output all edge weights.</span>
""")

#%% In [15]


#%%
md("""
We can now easily find out which of the paths of length two occur more or less often than expected based on our Markovian null model. For this we can just subtract the adjacency matrices of the two instances `hon_2` and `hon_2_null`.

<span style="color:red">**TODO:** For all egdes in `hon_2_null`, calculate how much the observed frequency in `hon_2` deviates from the random expectation.</span>

<span style="color:green">**Hint:** Use the function `HigherOrderNetwork.node_to_name_map()` to map node names to matrix indices.</span>
""")

#%% In [16]


#%% In [17]


#%%
md("""
### Ranking nodes in higher-order networks

<span style="color:red">**TODO:** Calculate the betweenness centrality of node `c` and the closeness centrality of node `d` in a first- and second-order model, as well as in the null model for `toy_paths`.</span>
""")

#%% In [18]


#%% In [19]


#%% In [20]


#%%
md("""
This confirms our intuition that two of the paths of length two actually occur twice as likely as expected if paths were memoryless, while two other paths do not occur at all.
""")

#%%
md("""
FInally, to fit higher-order models with order $k$, we need observations of paths with length at least k (as we account for the statistics of **sub-paths** of length $k$). In our toy example we have onyl observed paths with length two, so the attempt to generate a third-order model will fail with a `PathsTooShort` exception:

<span style="color:red">**TODO:** Try to generate a `HigherOrderModel` with order $k=3$ for `toy_paths`.</span>
""")

#%% In [21]


#%%
md("""
## Application to real-world data
""")

#%%
md("""
We can read ngram data files ... 

<span style="color:red">**TODO:** Use the `Paths.read_file` function to read path statistics from the ngram data files `US_flights.ngram` and `wikipedia_clickstreams.ngram`. Show the summary statistics of the resulting instances.
""")

#%% In [None]


#%% In [None]


#%% In [None]


#%% In [None]


#%% In [None]


#%%
md("""
We sometimes do not know the exact paths or trajectories taken, e.g. by passengers in a transportation network. But we often have aggregate statistics that allows us to nevertheless generate path statistics. Consider a setting where we know (1) the topology of a transportation network, and (2) the origin and destination of individual passengers, i.e. where they start and finish their journey. Under the assumption that passengers travel along shortest paths, we can now extract the path statistics that we need. Let us consider this in an example, so you can do the analysis in a real-world data set.

We first create a simple network topology:
""")

#%% In [None]


#%% In [None]


#%%
md("""
# Higher-order network visualisations
""")

#%% In [None]


#%% In [None]


#%% In [None]


#%% In [None]


#%% In [None]


#%% In [None]


#%% In [None]


#%% In [None]


#%% In [None]


