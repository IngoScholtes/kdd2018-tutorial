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
The real purpose of `pathpy` is to fit and analyse higher-order network models for paths in complex networks. For this we can use the class `HigherOrderNetwork`. Let us look at the `docstring` of this class.

<span style="color:red">**TODO:** Import the module pathpy and use the `help` function to print the documentation of class `pp.HigherOrderNetwork`.</span>
""")

#%% In [1]


#%%
md("""
From a higher-order network analytic point of view, standard graphs or networks are **first-order probabilistic generative models** for paths in complex networks. As we have seen in 1.2, these models only consider **first-order dyad statistics** (i.e. edge frequencies) thus ignoring higher-order dependencies in real-world path, sequence, or time series data.

In the following works, we have studied measures for higher-order correlations in such data and we generalised network models to higher-order models with arbitrary order:

- R Pfitzner, I Scholtes, A Garas, CJ Tessone, F Schweitzer: **Betweenness Preference: Quantifying Correlations in the Topological Dynamics of Temporal Networks**, In Physical Review Letters, May 2013, [arXiv 1208.0588](http://arxiv.org/abs/1208.0588)

- I Scholtes, N Wider, R Pfitzner, A Garas, CJ Tessone, F Schweitzer: **Causality-driven slow-down and speed-up of diffusion in non-Markovian temporal networks**, In Nature Communications, September 2014, [arXiv 1307.4030](http://arxiv.org/abs/1307.4030)

- I Scholtes, N Wider, A Garas: **Higher-Order Aggregate Networks in the Analysis of Temporal Networks: Path structures and centralities**, In The European Physical Journal B, March 2016, [arXiv 1508.06467](http://arxiv.org/abs/1508.06467) 

- Yan Zhang, Antonios Garas, Ingo Scholtes: **Controllability of temporal networks: An analysis using higher-order networks**, preprint, January 2017,  [arXiv 1701.06331](https://arxiv.org/abs/1701.06331)

- I Scholtes: **When is a Network a Network? Multi-Order Graphical Model Selection in Pathways and Temporal Networks**, In KDD'17, February 2017, [arXiv 1702.05499](https://arxiv.org/abs/1702.05499)

A broader overview of the research on higher-order models for complex systems is available the following preprint:

- R Lambiotte, M Rosvall, I Scholtes: **Understanding Complex Systems: From Networks to Optimal Higher-Order Models**, preprint, June 2018,  [arXiv 1806.05977](https://arxiv.org/abs/1806.05977)
""")

#%%
md("""
The data analysis and modelling framework outlined in these works builds on a generalisation of standard, first-order networks to $k$-dimensional De Bruijn graph models for paths in complex networks.

The class `HigherOrderNetwork` allows us to generate such higher-order network models of paths. In the documentation, we find that the constructor takes a parameter `paths`, i.e. the statistics of the observed paths that we want to model. With the parameter `k` we specify the order $k$ of the higher-order model that we want to fit. To understand this better, let us do this for our toy example.

<span style="color:red">**TODO:** Read the toy example from unit 1.2 from the file `data/toy_paths.ngram`, generate a **first-order** model instance `hon_1` and print a summary of the resulting instance.</span>
""")

#%% In [2]


#%%
md("""
This generates a first-order model of our paths, with five nodes $a,b,c,d$ and $e$, and four links $(a,c), (b,c), (c,d), (c,e)$. It is identicaly to the `Network` instance that we have previously created using `Network.from_paths`. Indeed, each `HigherOrderNetwork` instance is derived from the class `Network`, which means we can store edge and node attributes and visualise it by exactly the same methods.

<span style="color:red">**TODO:** Plot the `HigherOrderModel` instance `hon_1` and print the weight of all edges.</span>
""")

#%% In [3]


#%%
md("""
This output confirms that a `HigherOrderModel` with $k=1$ is identical to our `Network` model. WIth one exception: edge weights are vector-valued. Just like in `Paths`, the first entry captures the sub-path frequency while the second entry counts the occurrence of an edge as a longest path. 

We can see this network as a **first-order model** for paths where **edges are paths of length one**. That is, in a model with order $k=1$ edge weights capture the statistics of paths of length $k=1$.

We can generalise this idea to **k-th-order models** for paths, where **nodes are paths of length $k-1$** while **edge weights capture the statistics of paths of length $k$**. We can generate such a $k$-th order model by performing a line graph transformation on a model with order $k-1$. That is, edges in the model of order $k-1$ become nodes in the model with order $k$. We then draw edges between higher-order nodes whenever there is a possible path of length $k$ in the underlying network. The result is a $k$-dimensional De Bruijn graph model for paths. Let us try this in our example.

<span style="color:red">**TODO:** Create a second-order model `hon_2` for `toy_paths`. Visualise the model and print the weights of all edges.</span>
""")

#%% In [4]


#%%
md("""
Each of the four **edges** in the first-order model is now represented by a **node** in the second-order model. We further have two directed edges $(a-c, c-d)$ and $(b-c,c-e)$ that represent the two paths of length two that occur in our data.

This is important because it captures to what extent the paths that we observe in our data deviate from what we would expect based on the (first-order) network topology of the system. Considering such a first-order model, all four paths $a \rightarrow c \rightarrow d, a \rightarrow c \rightarrow e, b \rightarrow c \rightarrow d$ and $b \rightarrow c \rightarrow e$ of length two are possible. If edges were statistically independent we would expect those four paths to occur with the same frequency.

Another way to express this independence assumption is to consider Markov chain models for the sequences of nodes traversed by a path. In this view, independently occurring edges translate to a memoryless first-order Markov process for the node sequence. In our example, we expect paths $a \rightarrow c \rightarrow d$ and $a \rightarrow c \rightarrow e$ to occur with the same probability, i.e. the next nodes $d$ or $e$ on a path through $c$ are independent from the previous node $a$, their probabilities only depending on the relative frequency of edges $(c,d)$ vs. $(c,e)$. In our toy example, we have a total of 20 observed paths of length two, so we expect each of the path to occur 5 times on average.

`pathpy` can actually generate this **null-model** for paths within the space of possible second-order models. This allows us to  compare how the observed path statistics deviate from a (Markovian) expectation.

<span style="color:red">**TODO:** Use the `null_model` parameter in the constructor of `HigherOrderNetwork` to generate a second-order null model `hon_2_null` for `toy_paths`. Visualise the model and output all edge weights.</span>
""")

#%% In [5]


#%%
md("""
We can easily find out which of the paths of length two occur more or less often than expected under the null model. We can just subtract the adjacency matrices of the two instances `hon_2` and `hon_2_null`.

<span style="color:red">**TODO:** For all egdes in `hon_2_null`, calculate how much the observed frequency in `hon_2` deviates from the random expectation.</span>

<span style="color:green">**Hint:** Use the function `HigherOrderNetwork.node_to_name_map()` to map node names to matrix indices.</span>
""")

#%% In [6]


#%%
md("""
This analysis confirms that the paths $a \rightarrow c \rightarrow e$ and $b \rightarrow c \rightarrow d$ occur five more times than we would expect at random, while the other two paths do occur five less times than expected. Importantly, this deviation from our expectation changes the causal topology of the system, i.e. who can influence whom. In a network model we implicitly assume that paths are transitive, i.e. since $a$ is connected to $c$ and $c$ is connected to $d$ we assume that there is a path by which $a$ can influence $d$ via node $c$. The second-order model of our toy example reveals that this transitivity assumption is misleading, highlighting higher-order dependencies in our data that result in the fact that neither $a$ can influence $d$ nor $b$ can influence $e$.

### Ranking nodes in higher-order networks

In summary, higher-order models capture deviations from the transitivity assumption that we often implicitly make when we apply standard graph mining or network analysis techniques. An important class of methods that rely on this assumption are centrality measures, which are often used to rank nodes in networked systems.

Let us consider the betweenness value of a node $v$, which (in its unnormalized variant) captures for how many pairs of nodes $x,y$ the shortest path from $x$ to $y$ passes through $v$. This measure is important, because is teaches us something about the role of nodes in information flow. It further captures to what extent removing a node will affect the shortest paths between other nodes. Let us try this in our example:

<span style="color:red">**TODO:** Use the method `pp.algorithms.centralities.betweenness` to calculate the betweenness of node `c` in the first-order network model of `toy_paths`.</span>
""")

#%% In [7]


#%%
md("""
This is easy to understand, as there are four pairs $(b,e)$, $(b,d)$, $(a,e)$, $(a,d)$ for which the shortest path in the topology passes through node $c$. However, this notion of *importance* of node $c$ is based on the assumption that paths are transitive and Markovian, which is not the case in our observed paths. `pathpy` actually allows us to calculate the betweenness of node $c$ in the observed paths `toy_paths`.

<span style="color:red">**TODO:** Use the method `pp.algorithms.centralities.betweenness` to calculate the betweenness of node `c` in the paths observed in `toy_paths`.</span>
""")

#%% In [8]


#%%
md("""
Not surprisingly, the betweenness of node $c$ in the actual paths is two, as $c$ only connects two pairs of nodes are connected via a (shortest) path. This change in centrality is captured in the higher-order model and `pathpy` allows us to directly generalize centrality measures to higher orders, simply by calling the functions on the class `HigherOrderNetwork`.

<span style="color:red">**TODO:** Use the method `pp.algorithms.centralities.betweenness` to calculate the betweenness of node `c` in a second-order model for `toy_paths`.</span>
""")

#%% In [9]


#%%
md("""
We see that in this example (since we **only** have second-order dependencies) the second-order model accurately captures the betweenness of node $c$. Let us contrast this to the second-order null model.

<span style="color:red">**TODO:** Use the method `pp.algorithms.centralities.betweenness` to calculate the betweenness of node `c` in the second-order null model for `toy_paths`.</span>
""")

#%% In [10]


#%%
md("""
This is what we expect, since this null model is simply a second-order representation of the first-order model, in which paths are transitive and memoryless.


## Predicting node rankings with higher-order models

Let us now explore how we can apply higher-order models in practical prediction tasks. Assume we are given the task to rank nodes in a network according to how often they are traversed by paths. This has practical applications, e.g. predicting the most frequently clicked Web pages based on the topology of the link graph, or predicting the most congested airports based on the topology of flight connections. Let us study the latter example based on a data set on the paths of airline passengers in the United Stated.

For your convenience, we have partitioned the data set into a training and a validation set of equal size. Our goal will be to use the training set to learn (higher-order) network models. We then calculate a higher-order generalisation of `pagerank` described [in this paper](http://dl.acm.org/citation.cfm?id=3098145) in these models to predict the ranking of airports according to the number of passengers in the validation set.

<span style="color:red">**TODO:** Use the `Paths.read_file` function to read path statistics from the ngram data file `US_flights_train.ngram`. Set the parameter `frequency` of the read_file function to `False`. Generate a first-, second-, and third-order model for the paths. Use `pp.algorithms.centralities.pagerank` to calculate the PageRank of nodes in the higher-order models.</span>
""")

#%% In [11]


#%%
md("""
We can now use the values as a prediction for the ranking of airports based on a first-, second-, and third-order model for passenger itineraries. To validate the prediction performance of these models, we need a **ground truth**. We can calculate this in the validation data set. Specifically, we are interested in a ranking of airports in terms of the passenger itineraries passing through any given airport. 

<span style="color:red">**TODO:** Use the `Paths.read_file` function to read path statistics from the ngram data file `US_flights_validate.ngram`. Set the parameter `frequency` of the read_file function to `False`. Use the method `pp.algorithms.centralities.node_traversals` to calculate the number of passengers that through each airport in the validation data set.</span>
""")

#%% In [12]


#%%
md("""
We can validate our models by calculating the Kendall-Tau rank correlations between the ground-truth ranking of airports, and the rankings that we obtain based on the different higher-order models.

<span style="color:red">**TODO:** Use the function `kendalltau` from the package `scipy.stats` to calculate the rank correlation between (i) the ground truth ranking in the validation data, and (ii) the rankings obtained based on the first-, second-, and third-order models respectively.</span>
""")

#%% In [13]


#%%
md("""
We make three interesting observations: 

1. The first-order topology of flight routes alone allows us to generate a fairly good ranking of airports.
2. We can considerably increase the prediction performance of our model by taking into account second-order dependencies in the observed path statistics. This confirms that higher-order models are useful to improve predictions in real-world systems.
3. Interestingly, moving to the third-order model does not translate to a further increase of prediction performance. This suggests that the data set does not contain strong third-order dependencies. 


Considering that in reality we often do not have ground-truth that allows us to test which order performs best, this highlights the problem that we must decide which order to use for a given data set. We will solve this riddle in session 2, when we introduce a method to learn the optimal order for a given data set. 


### Path statistics from origin-destination data

In the example above, the data provide us with full knowledge about the exact itinerary taken by each passenger. However, we are often confronted with situations where we do not have such detailed information about paths. Nevertheless, we often have aggregate information that allows us to generate path statistics: Consider a setting where we know (1) the topology of a transportation network, and (2) the origin and destination stations of individual passengers, i.e. where passengers start and finish their journey. Under the assumption that passengers travel along shortest paths, we can now use this information to extract the path statistics that we need. 

`pathpy` provides a number of path extraction methods that help you to deal with such situations. For the situation described above, we can use the `pp.path_extraction.paths_from_origin_destination` method to generate path statistics based on tuples capturing origin/destination statistics and an instance of the class `Network`. Let us try this in a toy example.

<span style="color:red">**TODO:** Generate a directed network with six nodes and six edges $(a,c), (b,c), (c,d), (d,f), (d,g)$. Plot the network. Based on a list of tuples $(a, f, 5), (b, g, 10)$ capturing origin destination statistics, use the method `pp.path_extraction.paths_from_origin_destination` to generate a `Paths` object and print the result.</span>
""")

#%% In [16]


#%%
md("""
As expected, we get an instance with $15$ paths of length four. The shortest path $a \rightarrow c \rightarrow d \rightarrow f$ occurs 5 times, while the shortest path $b \rightarrow c \rightarrow d \rightarrow g$ occurs 10 times. 

With this we close this session, and we will move to the open-ended exploration, in which you can apply higher-order models to analyse data on paths and origin-destination statistics.
""")

