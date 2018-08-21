#%%
import markdown
from IPython.core.display import display, HTML
def md(str):
    display(HTML(markdown.markdown(str + "<br />")))

#%%
md("""
# 1.2 Introducing `pathpy`

**Ingo Scholtes**  
Data Analytics Group  
Department of Informatics (IfI)  
University of Zurich  


**August 22 2018**

In the introduction we have seen that higher-order modelling, visualisation, and analysis techniques are useful for all sorts of **temporal network data** that provide us with **statistics of paths in complex networks**. But how can we apply higher-order network analytics to such such data in practice?

In the first two sessions of our tutorial we introduce [``pathpy``](http://www.pathpy.net), an OpenSource `python` package that provides higher-order data analytics and representation learning techniques. It contains data structures, algorithms, data import/export methods, and visualisation techniques for various types of time series data on complex networks.

`pathpy` is pure `python` code with no platform-specific dependencies. It only depends on `numpy` and `scipy`, which come with `Anaconda`, so it should be very easy to install. In principle installing the latest 2.0 version of `pathpy` should be as easy as running

```
pip install pathpy2
```

on the terminal. In any case, you can find more detailed setup instructions on the [tutorial website](https://ingoscholtes.github.io/kdd2018-tutorial/setup).

<span style="color:red">**TODO:** Import the package `pathpy` and rename it to `pp`</span>
""")

#%% In [1]


#%%
md("""
A core functionality of `pathpy` is to read, calculate, store, manipulate, and model path statistics extracted from different kinds of temporal data on complex networks. For this `pathpy` provides the class `Paths`, which can store collections of paths with varying lengths. All classes and methods in `pathpy` are documented using `python`'s docstring feature so we can access the documentation using the standard `help` function. 

<span style="color:red">**TODO:** Use the `help` function to obtain a description of the class `Paths`.</span>
""")

#%% In [2]


#%%
md("""
In Visual Studio Code, the documentation of classes, methods, and properties is automatically shown as a tooltip as you type. If you use the browser-based `jupyter notebook` editor, you can bring up the documentation by pressing `Shift`+`Tab` as you type. You can try this with the `Paths` class. 

<span style="color:red">**TODO:** Create an empty `Paths` instance `toy_paths` by calling the constructor with no arguments.</span>
""")

#%% In [3]


#%%
md("""
We now have an empty `Paths` instance `toy_paths` that we can use to add path statistics to generate a small toy example. We can add paths using the method `add_path`. As the first parameter, it accepts any iterable (list, string, etc.) of `string` variables (or objects that can be cast to `string)`, where each entry in the iterable is one step (i.e. node) on a path. The optional `frequency` parameter captures the number of times a specific path has been observed.

<span style="color:red">**TODO:** Add 10 observations of a path $a \rightarrow c \rightarrow e$ between three nodes $a$, $c$, and $e$ to the `toy_paths` instance.</span>
""")

#%% In [4]


#%%
md("""
Each class in `pathpy` provides a properly formatted string representation, which can be shown by invoking `print` on an instance.

<span style="color:red">**TODO**: Print a string summary of the instance `toy_paths`</span>
""")

#%% In [5]


#%%
md("""
We get summary statistics of the `Paths` instance. Our toy example contains 10 observed paths between three nodes. These paths imply a graph topology with two edges `(a,b)` and `(b,c)`. Both the maximum and the average path length is two (the path length counts the number of edge traversals of a path).

To understand the last three lines and the second line in the output, we must look into the inner workings of `pathpy`. For the fitting of higher-order graphical models as well as for the representation learning algorithm, `pathpy` uses all path statistics available. Specifically to fit, say, a second-order model to a set of paths that all have length 10 or longer, we  calculate which paths of length two are contained as sub-paths within these observations of longer paths. For this reason, `pathpy` automatically calculates the statistics of actual path observations as well as the statistics of **sub-paths** contained in these observed paths.

In our case, we have $10$ observations of a single path $a \rightarrow b \rightarrow c$ of length two, thus the last line in the output above. Each of these paths additionally contains two sub-paths $a \rightarrow b$ and $b \rightarrow c$ of length two, thus the number $20.0$ in the sub-path count in the line $k=1$. Finally, each of the paths contains three "paths" of length zero, which are just observations of a single node (i.e. there is no transition across an edge), thus the sub-path count of $30.0$ in the line $k=0$. This amounts to a total of $50.0$ sub-paths + $10$ observations of an actual (longest) path, thus explaining the second line in the output.

Apart from adding paths as a tuple, we can also add them as string-encoded n-grams, using the parameter `separator` to specify a character that separates nodes.

<span style="color:red">**TODO:** Create a new `Paths` instance `ngram_paths`, add 10 path observations using the ngram `"b-c-e"`, and print a summary of the resulting instance.</span>
""")

#%% In [6]


#%%
md("""
We obtain a `Paths` object with 10 observations of path $b\rightarrow c \rightarrow$. We can add this to our previous `toy_paths` instance by using arithmetic operators on instances of the `Paths` class.


<span style="color:red">**TODO:** Use arithmetic operators to add `toy_paths` and `ngram_paths` and print a summary of the result.</span>
""")

#%% In [7]


#%%
md("""
We obtain a new `Paths` instance with $20$ observed paths between five nodes $a$, $b$, $c$, $d$, and $e$ across four edges $(a,c)$, $(c,d)$, $(b,c)$ and $(c,e)$. Let us first use the function `Paths.write_file` to save these paths for later use.

<span style="color:red">**TODO:** Save the paths to an ngram file `data/toy_paths.ngram`.</span>
""")

#%% In [8]


#%%
md("""
We often analyse or visualise graph or network topologies in which the observed paths have occurred. For this, `pathpy` provides the class `Network`, which you can use to read, manipulate, analyse, and visualise directed, undirected, weighted, and unweighted networks.

We can easily turn any `Paths` instance into a network by using the class method `Network.from_paths`. This will cut each path $v_0 \rightarrow v_1 \rightarrow v_2 \rightarrow$  into directed *dyadic relations* $(v_i, v_{i+1})$ that are represented by directed edges.

<span style="color:red">**TODO**: Create a `Network` instance `toy_graph` from the `toy_paths` instance and print a summary of the network.</span>
""")

#%% In [9]


#%%
md("""
We obtain a network with five nodes $a$, $b$, $c$, $d$, and $e$ and four directed edges. The number of times each edge is traversed by a path is captured by the **weights** of these edges. We can access these weights using the dictionary `tory_graph.edges[edge]`.

<span style="color:red">**TODO:** Print the `weight` of edge `(a, c)` in `toy_graph`.</span>
""")

#%% In [10]


#%%
md("""
In fact, since each edge can be viewed as a path of length one, the edge weights in our example are nothing more than the statistics of corresponding **sub-paths** of length one in the `toy_paths`. We can check the statistics of paths in a `Paths` instance by accessing `p.paths[length][path_tuple]`. This will return an array of two numbers, where the first entry is the number of times a path has been observed as **sub-path** of length l, and the second number gives the number of times a path has been observed as an **actual** (longest) path of length l.

<span style="color:red">**TODO:** Verify that the sub-path frequency of path `(a,c)` in `toy_paths` coincides with the weight of edge `(a,c)` in `toy_graph`.</span>
""")

#%% In [11]


#%%
md("""
When dealing with rich, real-world data we often want to store additional attributes of nodes and edges. `pathpy`'s  `Network` class accomodates for such settings by supporting arbitrary attributes both at the level of nodes and edges. Moreover, we can find nodes or edges with certain attributes by passing `lambda` functions to the `find_nodes` or `find_edges` method.

The attribute `x` of a node `v` or an edge `e` in a network instance `net` can be accessed simply by reading or writing to the dictionary net.nodes[v][x] and net.edges[e][x] respectively.

<span style="color:red">**TODO:** Set the node and edge attributes of some nodes and edges in `toy_graph`, and use `find_nodes` and `find_edges` to identify nodes and edges that have certain attributes.</span>
""")

#%% In [12]


#%%
md("""
Finally, `pathpy` offers rich, interactive HTML5 visualisations of all of its internal objects that can also be shown inline in a `jupyter` notebook. To embed a visualisation of our example network in our notebook, we simply have to write the name of the variable as the last line of a `jupyter` cell. 

Note that you can interact with the generated graph using the mouse. We can drag nodes as well as pan and zoom. Hovering above a node will show the name of that node.

<span style="color:red">**TODO**: Visualise the network `toy_graph`, drag a node, hover above a node, and pan and zoom.</span>
""")

#%% In [18]


#%%
md("""
Note the `[save svg]` label in the top-part of the output cell. Clicking this label will download the current view of the visualisation as a publication-grade scalable vector graphics file. This file is a good basis for further fine-tuning in SVG-compliant tools like Inkscape or Adobe Illustrator.

<span style="color:red">**TODO**: Export the file above as SVG by clicking the label.</span>

We can also programmatically style our network by using the generic `plot` function in the module `pathpy.visualisation`. This function allows us to pass parameters that will influence the visualisation.

<span style="color:red">**TODO**: Check the documentation of `pp.visualisation.plot` and change the color of nodes to red.</span>
""")

#%% In [14]


#%%
md("""
We often want to reuse the same visualisation parameters in multiple plots. For this, it is convenient to store our parameters in a dictionary and then pass all of them at once. 

Let us explore some of the features supported by `pathpy`'s default visualisation templates. In the second session we will learn more about **custom visualisation templates** that can be defined by the user, and which can take arbitrary visualisation parameters.

<span style="color:red">**TODO**: Use the `help` function to show which parameters are supported by the function `pp.visualisation.plot`.</span>
""")

#%% In [15]


#%%
md("""
<span style="color:red">**TODO**: Create a parameter dictionary `style` that changes the plot size, switches off edge arrows, assigns individual colors to nodes, changes label position, color and font size, and adjust node size and edge width.</span>
""")

#%% In [16]


#%%
md("""
Once we are satsfied with our visualisation, we can use the method `pp.visualisation.export_html` to save it as a stand-alone HTML file. This file will run in any HTML5 browser and we can share or publish as an interactive visualisation on the web.

<span style="color:red">**TODO**: Save your visualisation to a file `test_network.html`. Reuse the visualisation parameters from above.</span>
""")

#%% In [17]


