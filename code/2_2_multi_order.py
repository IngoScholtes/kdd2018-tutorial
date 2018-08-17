#%%
import markdown
from IPython.core.display import display, HTML
def md(str):
    display(HTML(markdown.markdown(str + "<br />")))

#%%
md("""
# Higher-Order Data Analytics for Temporal Network Data


## 2.2 Multi-Order Representation Learning

**Ingo Scholtes**  
Data Analytics Group  
Department of Informatics (IfI)  
University of Zurich  


**August 22 2018**
""")

#%%
md("""
## Detecting higher-order correlations

So far, we have studied higher-order network models for path data with a fixed, given order $k$. We have also seen that such higher-order models can yield better predictions compared to standard network models. But there are also a number of open questions, namely: 

1.) When do we need higher-order network models, and when are standard (first-order) models enough? 
2.) What is the optimal higher order to model a given data set? 
3.) Given that a model with order $k$ can only capture correlations in paths at a single fixed length $k$, how can we combine models with multiple higher orders into a multi-order model?

In this session, we will answer these questions. Let us again start with our simple toy example:
""")

#%% In [None]


#%%
md("""
Before, we have seen that in this example we only observe two of the four possible paths of length two that would be possible in the underlying network topology. Hence, this is a simple example for path statistics that exhibit correlations that warrant a second-order model. 

But how can we decide this analytically? We will take a statistical inference perspective on the problem. We can first use the (weighted) first-order network model to construct the transition matrix for a Markov chain model for paths in a network. We simply use the relative frequencies of edges to proportionally scale the probabilities of edges. Let us have a look at the first-order weighted network in our example:
""")

#%% In [None]


#%%
md("""
We can use this transition matrix to calculate a likelihood of the first-order Markov chain model given the paths that we have observed:
""")

#%% In [None]


#%%
md("""
In our toy example, this result is particularly easy to understand. For each of the twenty paths in `toy_paths`, the first transition is deterministic because the nodes $a$ and $b$ only point to a single node $c$. However, based on the network topology, for the second step we have a choice between nodes $d$ and $e$. Considering that we see as many first-order transitions through edge $(c,d)$ as we see through edge $(c,e)$, in a first-order model we have no reason to prefer one over the other, so each of them have probability $0.5$.

Hence, for each of the ten observed paths we obtain a likelihood of $1 \cdot 0.5 = 0.5$, which yields a total likelihood for our (independent) observations of $0.5^{10} = 0.0009765625$. 
""")

#%%
md("""
Let us now consider the likelihood of a second-order model for our paths:
""")

#%% In [None]


#%%
md("""
Here, the likelihood assumes a maximal value of $1.0$ because all transitions in the second-order model are deterministic, i.e. we simply multiply the likelihood of $1 \cdot 1$ for each of the twenty observed paths.

Let us have a look at the second-order null model, which really is a first-order model represented in the second-order space:
""")

#%% In [None]


#%%
md("""
This confirms our expectation that the second-order null model actually has the same as the first-order model. It also highlights an interesting way to test the hypothesis
""")

#%%
md("""
Let us calculate the likelihood ratio for our example:
""")

#%% In [None]


#%% In [None]


#%% In [None]


#%%
md("""
## Multi-order graphical model learning
""")

#%%
md("""
Unofortunately, our toy is too simple in multiple ways: First, it only contains correlations at a single length two, thus justifying a second-order model. Real data are likely to exhibit multiple correlation lengths at the same time. 

Even more importantly, in more realistic examples the model selection will actually not work as described above. The reason is that we cannnot directly compare likelihoods of models with different order, as they are nto calculated on the same 

That becomes clear in the following simple example path:
""")

#%% In [None]


#%% In [None]


#%% In [None]


#%% In [None]


#%% In [None]


#%% In [None]


#%% In [None]


#%%
md("""
We can visualise and analyse the layers of a multi-order model as follows:
""")

#%% In [None]


#%%
md("""
## Representation learning in real data sets
""")

#%% In [None]


#%% In [None]


#%% In [None]


#%% In [None]


#%% In [None]


#%% In [None]


#%% In [None]


#%%
md("""
## Multi-order graph visualisation
""")

#%% In [None]


