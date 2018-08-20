#%%
import markdown
from IPython.core.display import display, HTML
def md(str):
    display(HTML(markdown.markdown(str + "<br />")))

#%%
md("""
# 2.3 Optimal higher-order analytics for temporal data

**Ingo Scholtes**  
Data Analytics Group  
Department of Informatics (IfI)  
University of Zurich  


**August 22 2018**
""")

#%%
md("""
In the previous session we have seen how we can use `pathpy`'s representation learning features to automatically learn the optimal maximum order of a multi-order network model. The resulting models are optimal in the sense that they offers -- in the spirit of William of Ockham -- the best compromise between model complexity and explanatory power.

But how does this "optimality" translate to actionable insights into real-world data? In this session we answer this question by showing that the model with optimal order generalises best to unseeen data, i.e. we address the question by means of a cross-validation experiment.

With this session, we put together the pieces that we assembled so far: We will extract causal paths from temporal networks, fit higher- and multi-order models to the resulting path statistics, we learn the optimal order of the multi-order model, and show how this translates to an optimal ranking and visualisation of temporal data. 

Let us start with our example temporal network from session 2, which was synthethically generated to exclusively contain second-order dependencies between edges that give rise to temporal clusters. We have seen that we can visually identify these clusters if we generate a higher-order visualisation at the "correct" order. Now we know how we can learn this "correct" order from the data itself. We simply run the multi-order representation learning and visualise the layer of the multi-order that corresponds to the optimal maximum order. Let us try this.

<span style="color:red">**TODO:** Import `pathpy`, read the `TemporalNetwork` file `data/temporal_clusters.edges` and extract causal paths for `delta=1`. Generate a multi-order model, learn the optimal order, and plot a higher-order visualisation at this order.</span>
""")

#%% In [1]


#%%
md("""
Neat! We can now automatically visualise -- and thus **explain** -- the pattern that is the reason why this temporal network requires a second-order network representation.

For those who are still sceptical whether it is really impossible to detect this pattern with standard graph mining techniques, let us confirm that it is solely due to the chronological ordering of events.

We can do this by randomly shuffling time stamps of edges. This neither changes the inter-event time distribution, nor the frequency or topology of edges. It does, however, break any second-order dependencies in the chronological order of edges, thus changing the statistics of causal paths. Let's try this.

<span style="color:red">**TODO:** Use the `random.shuffle` function to randomly shuffle the time stamps of edges in the temporal network `t`. Repeat the order detection and the optimal order visualisation from above for the shuffled temporal network.</span>
""")

#%% In [None]


#%%
md("""
The cluster pattern disappears, which confirms that **this pattern is exclusively due to the chronological ordering of time-stamped edges**. Moreover, the representation learning algorithm has correctly concluded that a simpler first-order network is the optimal model for the causal paths in the shuffled temporal network.

Concluding this session, we now study to what extent a model with optimal order translates to the best model for prediction tasks. For this, we will first define some utility functions that will simplfy the cross-validation.

Since the overlap between the nodes observed in the training data, and the nodes in the validation data may not be perfect, we first need to define a function that calculates the `kendalltau` rank correlation coefficient for the intersection of nodes in the training and validation sets.

<span style="color:red">**TODO:** Define a function `kendalltau(a,b)` that (i) calculates the intersection of nodes, passed in two dictionaries `a` and `b`, and (ii) returns the Kendall-Tau rank correlation for this intersection calculated by `scipy.stats.kendalltau`.</span>
""")

#%% In [10]


#%%
md("""
To speed up the analysis, we can use ground truth node traversal frequencies, which we have precomputed for you and which we have stored in `json` files. We now write a function that can read these data, returning a dictionary.

<span style="color:red">**TODO:** Define a function `read_gt(filename)` that reads a file and returns the JSON-deserialised python-object.</span>
""")

#%% In [11]


#%%
md("""
Next, we need a function to calculate the kendall-tau rank correlation for different layers of a multi-order model. We will use this to verify that the detected optimal order yield an advantage over the predictions derived from the first-order model.

<span style="color:red">**TODO:** Define a function `validate(mog, gt)` that ...</span>
""")

#%% In [7]


#%%
md("""
Finally, we want to plot our results (obviously in `xkcd`-style charts).

<span style="color:red">**TODO:** Define a function `plot_results(mog, gt)` that ...</span>
""")

#%% In [8]


#%%
md("""
We are now ready to analyse our data. Let us start with a data set where we know what to expect. For the data on US flight passenger trips, in unit 1.3 we have seen that the predictive performance of a higher-order model for the flight data saturated around order two. Moreover, using a multi-order model we have found that the optimal order to model the flight itineraries is two. Let us now plot the kendall-tau correlation of our ranking for different orders.

To speed things up a little, you can read the ground truth for the airport rankings from the file `US_flights_gt.json`. You can then use the method `validate` to calculate the kendall-tau rank correlation with the ground truth for different layers of the multi-order model, and the method `plot_results` to plot the results.

<span style="color:red">**TODO:** Read the training data set `US_flights_train.ngram`, generate a `MultiOrderModel` with maximum order three, and detect the optimal order. Cross-validate the obtained node ranking and plot the results.</span>
""")

#%% In [12]


#%%
md("""
This simply confirms what we have seen before. The predictive performance of our model reaches a plateau at the optimal order detected by the representation learning algorithm. Beyond that order, the additional complexity of a third-order model is not justified by the (marginal) increase of predictive power.

Let us now consider some real time-stamped social networks. 

<span style="color:red">**TODO:** XXX.</span>
""")

#%% In [18]


#%%
md("""


<span style="color:red">**TODO:** XXX.</span>
""")

#%% In [22]


#%%
md("""
We observe that a PageRank with the optimal order learned by our multi-order graphical model selection performs best in terms of prediction.

<span style="color:red">**TODO:** XXX.</span>
""")

#%% In [23]


#%%
md("""
This plot is interesting for several reasons ... 

1. Network model is a bad model for paths in the real systems
2. Second-order model is better, but still not good enough
""")

#%% In [None]


