#%%
import pathpy as pp 
import sqlite3
import numpy as np
from random import shuffle
import scipy.stats
import numpy as np
import operator
import json


def write_gt(paths, file):
    ground_truth = pp.algorithms.centralities.visitation_probabilities(paths)
    with open(file, 'w') as f:
        json.dump(ground_truth, f)

con = sqlite3.connect('data/temporal_networks.db')
con.row_factory = sqlite3.Row


#%% London Tube
tube_net  = pp.Network.read_file('data/tube.edges', separator=';')
od_stats = pp.path_extraction.read_origin_destination('data/tube_od.csv', separator=';')
paths = pp.path_extraction.paths_from_origin_destination(od_stats, tube_net)
write_gt(paths, 'data/tube_gt.json')

#%% Flights
paths = pp.Paths.read_file('data/US_flights.ngram', frequency=False)
write_gt(paths, 'data/US_flights_gt.json')

#%% Wikipedia
paths = pp.Paths.read_file('data/wikipedia_clickstreams.ngram', frequency=False, expand_sub_paths=False)
write_gt(paths, 'data/wikipedia_clickstreams_gt.json')


#%% 
t = pp.TemporalNetwork.from_sqlite(con.execute('SELECT source, target, time FROM haggle'),
                                  time_rescale=10)
paths = pp.path_extraction.sample_paths_from_temporal_network_dag(t, delta=6, num_roots=1000)
write_gt(paths, 'data/haggle_gt.json')

#%%
t = pp.TemporalNetwork.from_sqlite(con.execute('SELECT source, target, time FROM manufacturing_email'),
                                   time_rescale=600)
paths = pp.path_extraction.sample_paths_from_temporal_network_dag(t, delta=12, num_roots=1000)
write_gt(paths, 'data/manufacturing_email_gt.json')


#%%
t = pp.TemporalNetwork.from_sqlite(con.execute('SELECT source, target, time FROM sociopatterns_hospital'),
                                   time_rescale=20, directed=False)
paths = pp.path_extraction.sample_paths_from_temporal_network_dag(t, delta=3, num_roots=200)
write_gt(paths, 'data/sociopatterns_hospital_gt.json')