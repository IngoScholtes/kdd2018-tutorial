#%%
import markdown
from IPython.core.display import display, HTML
def md(str):
    display(HTML(markdown.markdown(str + "<br />")))

#%%
md("""
# Higher-Order Data Analytics for Temporal Network Data

## 1.4 Exploration: Higher-order analysis of real-world pathway data

**Ingo Scholtes**  
Data Analytics Group  
Department of Informatics (IfI)  
University of Zurich  


**August 22 2018**

In the last (open-ended) exploration of this first tutorial session, you have the chance to use higher-order network analytics to study three real data sets for yourself: 

- Passenger itineraries constructed from London Metro Oystercard origin-destination data
- Flight itineraries of US airline passengers
- Wikipedia clickstream data

We include the code to load these data sets in `pathpy`. Using these data and the methods introduced in the first tutorial session, you can now address the following problems (in ascending order of difficulty):

- Generate higher-order visualisations of the different data sets and visually compare the graph layouts calculated at different order.
- Use the higher-order framework to identify those paths of length k that show the most anomalous statistics (compared to a memoryless null model). Which are these paths and how can we interpret the result?
- Compare the ranking of nodes in terms of centralities obtained at different orders k. How can we define a ground truth for this ranking. To what extent do the different rankings reproduce this ground truth?
- Perform a spectral clustering based on the Laplacian of higher-order networks at different order. How does the clustering differ from a first-order clustering?

You should see both the data sets as well as the questions as suggestions for your exploration. You are welcome to study other data sets or question instead. Just reach out to us if you encounter any problems. Feel free to contact me after the tutorial.
""")

#%% In [3]
import pathpy as pp

# Flight data  
flight_paths = pp.Paths.read_file('data/US_flights.ngram', frequency=False)

# Clickstream, ignore a single path with more than 400 clicks
clickstreams = pp.Paths.read_file('data/wikipedia_clickstreams.ngram', frequency=False, max_ngram_length=100)

# London Tube trips based on Oyster card checkin-checkouts
tube_net  = pp.Network.read_file('data/tube.edges', separator=';')
od_stats = pp.path_extraction.read_origin_destination('../data/tube_od.csv', separator=';')
tube_trips = pp.path_extraction.paths_from_origin_destination(od_stats, tube_net)

#%% In [None]


