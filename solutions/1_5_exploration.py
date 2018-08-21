#%%
import markdown
from IPython.core.display import display, HTML
def md(str):
    display(HTML(markdown.markdown(str + "<br />")))

#%%
md("""
# 1.5 Exploration: Higher-order analysis of real-world pathway data

**Ingo Scholtes**  
Data Analytics Group  
Department of Informatics (IfI)  
University of Zurich  


**August 22 2018**

In the last (open-ended) exploration of this first tutorial session, you have the chance to use higher-order network analytics to study real data sets for yourself.

Details on the available data sets can be found [here](https://github.com/IngoScholtes/kdd2018-tutorial/tree/master/data). Using these methods introduced in the first tutorial session, we suggest you to address the following problems (in ascending order of difficulty):

- Repeat the analysis of higher-order centralities in the toy example from 1.3 with the closeness centrality of nodes. What do you observe?
- Test the prediction performance of higher-order models for the London Tube and/or the Wikipedia clickstream data set. Does the prediction performance saturate at k=2 as it does for the US Flight data?
- Study the difference between higher- and first-order centralities in the dynamic social networks contained in the SQLite database file.
- Use the higher-order framework to identify those paths of length k that show "anomalous statistics" (compared to a memoryless null model). Which are these paths and how can we interpret the result?

Please consider the data sets as well as the questions above as mere **suggestions for your exploration of higher-order network analytics**. You are welcome to study other data sets or questions instead. Please reach out to me if you encounter any problems or questions (also after KDD). You can reach me at `scholtes@ifi.uzh.ch`.
""")

#%% In [1]
import pathpy as pp

# Flight data  
flight_paths = pp.Paths.read_file('data/US_flights.ngram', frequency=False)

# Clickstreams, ignore single path with more than 400 clicks
clickstreams = pp.Paths.read_file('data/wikipedia_clickstreams.ngram', frequency=False, max_ngram_length=100)

# London Tube trips based on Oyster card checkin-checkouts
tube_net  = pp.Network.read_file('data/tube.edges', separator=';')
od_stats = pp.path_extraction.read_origin_destination('data/tube_od.csv', separator=';')
tube_trips = pp.path_extraction.paths_from_origin_destination(od_stats, tube_net)

