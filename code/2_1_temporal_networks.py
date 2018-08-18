#%%
import markdown
from IPython.core.display import display, HTML
def md(str):
    display(HTML(markdown.markdown(str + "<br />")))

#%%
md("""
# Higher-Order Data Analytics for Temporal Network Data


## 2.1 Temporal Network Analysis and Visualisation in `pathpy`

**Ingo Scholtes**  
Data Analytics Group  
Department of Informatics (IfI)  
University of Zurich  


**August 22 2018**

### Introduction to the `TemporalNetwork` class

So far, we have considered the `Paths` class, which is useful if you have direct access to path statistics in your time series data. In the last exploration, we have seen examples for such data, which can immediately be modelled using higher-order models. This includes clickstreams of users in information networks, origin-destination statistics in transportation networks, flight ticket sequences, or other **collections of short, ordered sequences**.

In this session, we expand this view towards temporal networks, i.e. high-resolution time series network data where edges carry. Considering technical, social, and biological systems that can be modelled as dynamic networks, such data cover a broad class of complex systems that can be studied with higher-order network models. In this session we consider examples for dynamic social interactions, such as time-stamped E-Mail exchanges, or social contact patterns recorded via smartphones or electronic sensors.

Acknowledging the importance of such time series data, `pathpy` provides special support for the analysis of temporal networks data via its `TemporalNetwork` class. It is suitable for data that captures time-stamped edges $(v, w, t)$ instantaneously occurring at discrete time stamps $t$. Let us start by creating an empty instance of this class.

<span style="color:red">**TODO:** Import the package `pathpy` and rename it to `pp`. Create a new instance `t` of the class `TemporalNetwork` and print a summary of the instance.</span>
""")

#%% In [1]


#%%
md("""
The `TemporalNetwork` instance `t` stores two key information: a list of nodes `t.nodes` and a collection `t.tedges` of time-stamped edges  $(v, w, t)$. Let us add some time-stamped edges to this instance.

<span style="color:red">**TODO:** Use the `add_edge` function to add six (directed) time-stamped edges $(a,b, 1), (b, a, 3), (b, c, 3), (d, c, 4), (c, d, 5), (c, b, 6)$ and print the result.</span>
""")

#%% In [2]


#%%
md("""
We see that we get some basic summary statistics, such as the number of time-stamped interactions, the minimum and maximum timestamp, the duration of the observation, the number of different timestamps, as well as the average, minimum, and maximum time difference between consecutive time-stamped edges.

In the example above we use integer timestamps, which we can view as **discrete time units**. This is easy to grasp, but we usually have data where time is given in terms of a date and/or time of day. Luckily, `pathpy` supports arbitrary timestamp formats. Let us try this in an example.

<span style="color:red">**TODO:** Create a new `TemporalNetwork` instance `t_realtime` and add three time-stamped edges with string timestamps in the format "YYYY-MM-DD HH:mm:SS". Print the resulting instance and print all time-stamped edges.</span>
""")

#%% In [3]


#%%
md("""
We observe that `pathpy` internally converts such timestamps into second-based UNIX timestamps. For custom formats, we can set a custom `timestamp_format` parameter that will be used for this conversion. After the conversion, all time units will be in seconds (see e.g. the min/max inter-event time).

Just like other `pathpy` objects, we can directly embed interactive visualisations of a `TemporalNetwork` in-line in `jupyter`. Let us try this with our first example instance `t`.

<span style="color:red">**TODO:** Visualise the `TemporalNetwork` instance `t` by writing the instance variable in an empty `jupyter` cell.</span>
""")

#%% In [4]


#%%
md("""
Using the default parameters, this visualisation is too fast for the human eye. Luckily, we can use the generic `pp.visualisation.plot` function to pass a `style` for the visualisation. We can use all parameters that we used for static networks, plus additional parameters that influence the temporal aspects of the visualisation. 

Of particular importance are the two parameters `ms_per_frame` and `ts_per_frame`: The first specifies how many time units will be shown in one frame of the visualisation, allowing us to compress the visualisation by showing multiple timestamps in a single frame. This is helpful when you want to coarsen visualisations of high-resolution temporal network. The second parameter `ms_per_frame` defines the target frame rate of the visualisation by adjusting how many milliseconds each frame is displayed. 

Two more parameters will influence the force-directed layout algorithm, that is used to position nodes in the network. In a temporal network, the question is which time-stamped edges should be taken into account for the force-calculation at any given time stamp. If we only consider currently active edges, the layout will change too fast to recognize interesting patterns. If we consider all edges at every time step, node positions will be static despite the dynamics of edges. In real settings we want a compromise between those extremes, i.e. we specify a time window around the current time stamp within which edges are taken into account in the force-directed layout calculation. We can achieve this by setting the number of timestamps to consider before and after the currently shown frame via the `look_ahead` and `look_behind` parameters. 

Finally, we can style active and inactive nodes and edges individually via the parameters `active_edge_width`, `inactive_edge_width`, `active_node_color`, and `inactive_node_color`. This allows us to change the color and/or size of nodes/edges whenever they are involved in an interaction.

<span style="color:red">**TODO:** Create a visualisation where a single timestamp is shown per frame, and each frame is shown for 2 seconds. For the force-directed layout, consider edges active up to two time units before and after the current timestamp. Increase the thickness of currently active egdes. </span>
""")

#%% In [5]


#%%
md("""
Again, this generates an embedded **interactive** visualisation, i.e. you can pan and zoom, or drag nodes. The controls in the top part of the visualisation allow you to stop, start or restart the simulation. 

We can easily save such interactive visualisations as stand-alone HTML5 files, which can be distributed via the Web.

<span style="color:red">**TODO:** Save the visualisation from above to a file and open it in a Browser. </span>
""")

#%% In [6]


#%%
md("""
### Calculating path statistics in temporal networks
""")

#%%
md("""
In the previous session, **we modelled, analysed and visualised path statistics using higher-order network models**. But how can we  apply this higher-order analytics framework to time-stamped network data?

The key idea is that the ordering and timing in which time-stamped edges occur in a `TemporalNetwork` gives rise to so-called **causal or time-respecting paths**. In a nutshell, for two time-stamped edges $(a, b, t)$ and $(b, c, t')$ to contribute to a causal path $a \rightarrow b \rightarrow c$ it must hold that $t < t'$. If we swap timestamps such that the edge $(b, c)$ occurs **before** (a,b), no causal path $a \rightarrow b \rightarrow c$ exists.

So we observe that the chronological order of time-stamped edges crucially influences causal paths, i.e. which nodes can possibly influence each other in time-stamped edge sequences. Moreover, we often want to limit the **maximum time difference between consecutive edges** that contribute to a causal path. For data on dynamic social interactions that spans several years, it does not make sense to consider all chronologically ordered edges as possible causal paths for the propagation of information. After all, humans have limited memory and we should thus consider interactions that occur far apart in time as independent.

We can formally add this condition by setting a maximum time difference $\delta$ for the path calculation. That is, we only consider two edges $(a, b, t)$ and $(b, c, t')$ to contribute to a causal path $a \rightarrow b \rightarrow c$ if $ 0 < t' - t \leq \delta$.

With this definition at hand, and by setting our maximum time difference $\delta$, we can now **calculate causal path statistics in time-stamped network data**. `pathpy` provides powerful algorithms to calculate (or estimate) causal path statistics based on a `TemporalNetwork` instance. Let us try this in our toy example.

 <span style="color:red">**TODO:** Use the method `pp.path_extraction.paths_from_temporal_network_dag` to calculate causal path statistics for the example temporal network `t` and a maximum time difference $\delta=1$. Print the resulting `Paths` object. as well as all causal paths.</span>
""")

#%% In [7]


#%%
md("""
For $\delta=1$, it is easy to verify that this output is correct. After all, there is only one pair of (directed) edges $(d, c, 4), (c, d, 5)$ that contributes to a causal path of length two. In addition, we have four time-stamped edges, each of which is a trivial causal path of length one.

This brings us to an important observation: In line with what we have discussed in the previous session, time-aggregated models of temporal networks discard the ordering and timing of links. They are thus **maximum entropy, first-order network models for causal paths** in temporal networks.

While it is easy to understand the path statistics for a maximum time difference of $\delta=1$, already for $\delta=2$ the situation gets more complicated.

<span style="color:red">**TODO:** Generate and print all causal paths emerging for a maximum time difference $\delta=2$.</span>
""")

#%% In [8]


#%%
md("""
We now observe one causal path $a \rightarrow b \rightarrow c \rightarrow d$ of length three, and three additional causal paths of length two. All shorter causal paths are contained in those longer causal paths, as shown by the path statistics shown above.

While I will not go into the full details of `pathpy`'s path calculation algorithm, we can at least peek into how it is done. Internally, `pathpy` generates a so-called **time-unfolded** directed and acyclic graph (see definition and illustration in [this work](https://arxiv.org/abs/1208.0588)). This graph is then the basis to calculate causal path statistics. We can get an idea how this works by manually generating a time-unfolded graph from a temporal network.

<span style="color:red">**TODO:** Use the `pp.DAG.from_temporal_network` method to create a time-unfolded graph from the `TemporalNetwork` `t` for $\delta=2$. Generate a visualisation where you color all time-unfolded nodes according to the "real" node to which they belong and increase the size of root nodes so you can easily tell them apart.</span>
""")

#%% In [9]


#%%
md("""
We obtain a time-unfolded graph, where each node is a **temporal copy** of an actual node, and where colors indicate to which node each temporal copy belongs. Importantly, the resulting directed acyclic graph has two root nodes (shown as larger nodes) with degree zero. Each of these root nodes shows where a causal path can possibly start. These roots are the basis for `pathpy`'s path calculation algorithm, i.e. in the simplest case `pathpy` will simply process all of these results to generate the path statistics.

### Higher-order analysis of real dynamic social networks

To simplify the analysis of large collections of time-stamped network data, `pathpy` natively supports `SQLite` databases. For this, let us import `python`'s `sqlite3` module and use the `connect` function to connect to a `SQLite` database file. In order to access columns by name rather than index, we also need to set the default `row_factory` on the `Connection` object that is returned by the `connect` function to `sqlite3.Row`.

<span style="color:red">**TODO:** Import the module `sqlite3` and connect to the `SQLite` database file `temporal_networks.db`, which we provide for you in the `/data` directory. Set the `row_factory` of the resulting connection to `row_factory`.</span>
""")

#%% In [10]


#%%
md("""
We can now generate temporal networks from an `SQLite` database. For this, we must pass a so-called `SQLite` cursor to the constructor of `TemporalNetwork`. This cursor essentially tells which rows and columns of the database should be used for the temporal network creation. We can create it by passing an `SQL` query to the `execute` function of the `connection` object.

 The `TemporalNetwork` class assumes that the source, target, and timestamp of time-stamped edges are stored in columns called `source`, `target` and `time`. If your database has a different format, you can use the `SQL` `as` keyword to rename the columns in the query. Note that you can use the extension [SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) to browse the `SQLite database` file within Visual Studio Code. Once you have installed it,  hit `CTRL + Shift + P` and enter the command `SQLite: Open Database in Explorer`. This will bring up a new database panel in the explorer section on the left, which you can use to show the structure and contents of the database.
 
Let us now try this with a data set on (undirected) time-stamped proximity contacts between patients and workers in a hospital, collected via the [Sociopatterns](http://www.sociopatterns.com) project.
 
<span style="color:red">**TODO:** Create an undirected `TemporalNetwork` instance `t_ho` from an `SQL` query of the database `sociopatterns_hospital` and print the resulting object.</span>
""")

#%% In [11]


#%%
md("""
We see that this temporal network has more than 64,000 time-stamped contacts between 75 individuals. On average, each individual engages in more than 860 contacts and the average time difference between contacts is approx. 36 seconds. More interestingly, the minimum inter-event time is 20 seconds, which is due to the fact that the sensor equipment used registered contacts every 20 seconds.

Blindly calculating causal paths for large values of $\delta$ (say $\delta=300$ for a maximum time difference between contacts of five minutes) would lead to the generation of a huge time-unfolded graph. However, since the sampling interval in this data set is larger than the time unit of 1 second, we can use `pathpy`'s time rescaling feature. It helps us to more efficiently calculate causal paths by rescaling internal time units to match a data set's sampling frequency. In the Sociopatterns data, we can rescale time by a factor of 20 without any loss of information. This means that timestamps 20, 40, 80 will be mapped to integer time units 1, 2, 4. Let us try this:

<span style="color:red">**TODO:** Repeat the previous step, but rescale internal time units by a factor of 20. Print the resulting instance `t_ho`</span>
""")

#%% In [12]


#%%
md("""
The fact that the minimum inter-event time is now 1 shows that the internal time units have been scaled accordingly. Note that as long as we match the time rescaling to the ssampling frequency, this does not change path structure of the resulting temporal network. We must, however, account for the time unit when we specifiy the $\delta for the causal path calculation.

<span style="color:red">**TODO:** Calculate causal paths in the temporal network `t_ho` and set the maximum time difference to one minute.</span>
""")

#%% In [13]


#%%
md("""
For this calculation, `pathpy` needs to analyse a time-unfolded graph with more than 100,000 nodes and more than 5000 root nodes, which are processed in the path calculation. This actually takes quite some time. And depending on the size and temporal characteristics of your data, exhaustively calculating causal paths for large values of $\delta$ can quickly become prohibitive. 

Let us cancel this computation by interrupting the kernel. We need more efficient methods to get a quick **estimate** of causal path statistics, which we can use to generate higher-order models.

`pathpy` provides a smart way to do this by randomly sampling roots in the time-unfolded acyclic graph. Let us try this for 50 root nodes.

<span style="color:red">**TODO:** Use the method `sample_paths_from_temporal_network_dag` to estimate causal path statistics in the temporal network `t_ho` for a maximum time difference of one minute.</span>
""")

#%% In [14]


#%%
md("""
### Higher-order clustering and visualisation of causal structures in temporal networks

An interesting application of higher-order models concerns the visualisation of time-aggregated representations of temporal networks. We demonstrate this in a temporal network synthetically generated to exhibit a specific pattern in the ordering of time-stamped edges. Let us load this example and visualise the first 250 time stamps: 

<span style="color:red">**TODO:** Read the file `temporal_clusters.tedges` as a `TemporalNetwork`. Use the `pp.visualisations.plot()` method to visualise the temporal network. Use the parameter `max_time` to limit the visualisation to the first 250 time stamps.</span>
""")

#%% In [15]


#%%
md("""
What you probably cannot see in this visualisation is that this temporal network exhibits **clusters in the causal topology**, i.e. there are more **causal paths** between certain clusters of nodes than we would expect if links were independent (and paths were Markovian). We can get a vague idea of this by simulating a random walk in the temporal network, following the trajectory of a walker as it is moved through the nodes by dynamic edges.

<span style="color:red">**TODO:** Use the method `pp.algorithms.temporal_walk.generate_walk` to create a sequence of 500 random walk steps in the temporal network `t`. Use the method `pp.visualisation.plot_walk` to visualise the random walk trajectory in the (first-order) time-aggregated network.</span>
""")

#%% In [16]


#%%
md("""
Still, the pattern is difficult to see as the layout of nodes does not reflect the causal structures in the temporal network. With `pathpy` we can easily get around this problem. We can generate a **time-aware layout** that considers the causal topology of the temporal network that results from higher-order dependencies between time-stamped edges. The basic approach of calculating higher-order layouts for temporal networks is described in this preprint:

I Scholtes: [Force-Directed Layout of Non-Markovian Temporal Networks](http://www.sg.ethz.ch/research/publications/), preprint, 2014

Generating such a time-aware layout in `pathpy` is actually trivial. We simply plot a `HigherOrderNetwork` model for the causal path in a temporal network, while setting a parameter `plot_higher_order_nodes` to False. Different from the previous visualisations, this will project the higher-order topology on the first-order nodes. Let us try this.

<span style="color:red">**TODO:** Generate a second-order model for causal paths in `t` assuming $\delta=1$. Use the `pp.visualisations.plot()` method to visualise the second-order model. Set the `plot_higher_order_nodes` parameter to `False`.</span>
""")

#%% In [18]


#%%
md("""
We see that nodes automatically position themselves in groups that correspond to the natural cluster structure in the causal topology. In the visualisation above, we have additionally colored nodes based to their (synthetically generated) ground-truth clusters. With this layout of the graph, let us visualise again our random walk trajectory from above.

<span style="color:red">**TODO:** Visualise the random walk trajectory in the network layouted according to the second-order model.</span>
""")

#%% In [19]


#%%
md("""
We now see that the random walker indeed has a tendency to visit, in subsequent steps, nodes that belong to the same clusters. In this specific case, the cluster pattern in the layout actually disappears if we calculate a third-order layout.

<span style="color:red">**TODO:** Generate a third-order model for the causal topology of the temporal network. Visualise the third-order model like above, again setting the `plot_higher_order_nodes` parameter to `False`.</span>
""")

#%% In [21]


#%%
md("""
The reason for this is simple: This example exhibits correlations at correlation length two (i.e. for paths of length two), but there are no correlations at correlation length three. This highlights two important issues, that we will address in a moment:

1. We need a method to determine the optimal order of the higher-order models that we use to analyse (or visualise) a given data set.
2. As real systems are likely to exhibit multiple correlation length simultaneously, we need models that can combine multiple higher-order models.


But before move to these questions, let us spend some words on higher-order clustering in temporal networks. We have seen that correlations in the ordering of time-stamped edges can change the trajectory of a random walker. In particular, we observe clusters in the **causal structure** of a system that make the random walk subsequently visit nodes within the same cluster with higher probability. In the [afternoon sessions of our tutorial](https://ingoscholtes.github.io/kdd2018-tutorial/), Daniel Edler will give an in-depth introduction to [InfoMap](http://www.mapequation.org), a popular information-theoretic approach to graph clustering that utilises this property of random walks.

Complementary to this part of our tutorial, here we briefly introduce another approach to higher-order clustering. The idea is to generalise **spectral graph clustering algorithms** to higher-order network models. These algorithms utilise [graph Laplacians](https://en.wikipedia.org/wiki/Laplacian_matrix), a matrix representation of a graph where edges are represented by -1 entries, while the diagonal contains the degrees of nodes (and other entries are zero). The eigenvalues and eigenvectors of this matrix provide interesting insights about the topology of a graph, and about its influence on dynamical processes like random walks or diffusion. In particular, the second-smallest eigenvalue of the Laplacian matrix captures how **well-connected** a graph is, where small values close to zero indicate small cuts that can signify cluster structures. Moreover, the corresponding eigenvector, the so-called [Fiedler vector](https://en.wikipedia.org/wiki/Algebraic_connectivity#Partitioning_a_graph_using_the_Fiedler_vector) can be used for a simple spectral clustering algorithm, where nodes in different clusters are represented by eigenvector entries falling to different value ranges.

An interesting prospect for higher-order network analytics is that we can generalise graph Laplacians to higher-order network models, which can then be used to study cluster structures in the causal topology of a temporal network. If you are interested in the mathematical details, check: 

I Scholtes, N Wider, R Pfitzner, A Garas, CJ Tessone, F Schweitzer: [Causality-driven slow-down and speed-up of diffusion in non-Markovian temporal networks](http://www.nature.com/ncomms/2014/140924/ncomms6024/full/ncomms6024.html), Nature Communications, Vol. 5, Article 5024, 2014

Let us try this in our synthetic data set:

<span style="color:red">**TODO:** Use the methods in `pp.algorithms.spectral` to calculate the algebraic connectivity of the second-order model for causal  paths in the temporal network `t`. Compare the value to the the algebraic connectivity of (i) the corresponding second-order null model, and (ii) a first-order model of paths.</span>
""")

#%% In [22]


#%%
md("""
We clearly see that the algebraic connectivity of the second-order model is close to zero, thus indicating cluster structures that lead to a small cut in the causal topology of the system. This small value actually captures the "trapping" of the random walker within clusters. The algebraic connectivity of the second-order null model and the first-order model are actually identical (up to numerical imprecision).

Let us now go one step further and use the distribution of Fiedler vector entries to reveal the cluster structure in the causal topology.
""")

#%%
md("""
<span style="color:red">**TODO:** Use the methods in `pp.algorithms.spectral` to calculate the fiedler vector of (i) the second-order model, and (ii) the second-order null model. Use a scatter plot to visually compare the distributions of the real parts of both eigenvectors.</span>
""")

#%% In [24]


#%%
md("""
The three clusters in the temporal network clearly show up as three different value ranges in the distribution of entries in the Fiedler vector. The lack of this structure in the null model confirms, that the cluster structure is only due to the chronological ordering of links, and neither due to their topology nor due their frequencies.

### Bonus: Data-driven story-telling with custom visualisation templates

Finally, we briefly introduce custom visualisation templates, which you may find useful for data-driven and visual story-telling tasks. As an example, we will use a data set on character co-occurrences in the text of The Lord of the Rings. You can load it from the table `lotr` SQLite database. In this table, each row `source, target, time` captures that the characters `source` and `target` are mentioned within the same sentence, where `time` chronologically numbers sentences throughout all three novels.

In the following, we want to generate a nice interactive visualisation of this data set. For this, we will use the custom templating mechanism of `pathpy`. It allows you to define your own HTML templates, that you can derive from the default visualisation templates that we have used so far. This enables us to use the default `pathpy` visuals as a baseline, that we can tune to our needs. 

Technically, such a template is nothing more than an HTML5 file with embedded JavaScript and CSS code. `pathpy` will use this template, and replace placeholder variables that we can set via the `style` parameter dictionary. We can tell `pathpy` to use an arbitrary custom template file by setting the entry `style['template'] = filename`. In this template, we can then use variables in the form `$variable`, which we can set from within `python` by setting `style['variable'] = value`.

In the custom template file `data/custom_template.html` we use all of `pathpy`'s default style parameters, as well as two additional parameters `chapter_data` and `character_classes`. We will use the first to pass chapter marks to the visualisation, which are then shown in the top left part of the visualisation as the story unfolds. Moreover, we will visualise the different factions (Hobits, Elves, Fellowship, Dwarves, ...) to which characters belong, so we need to pass those to the template as well.

You can read the character and chapter data from the corresponding json-files in the data directory. Just use the `json.load` function in `python's` json file to read them into two dictionaries and pass those two dictionaries to the corresponding `style` parameters.

<span style="color:red">**TODO:** Use the `pp.visualisations.export_html()` method to create a visualisation of dynamic character interactions in The Lord of The Rings based on the table `lotr` in the SQLite database and the custom template file `custom_template.html` in the `data` folder.</span>
""")

#%% In [25]


#%%
md("""
As a little distraction at the end of this session, open the generated file in your browser, lean back and enjoy watching the story unfold - as a temporal network :-)
""")

