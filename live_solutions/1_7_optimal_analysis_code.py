#%% In [1]
import pathpy as pp

t = pp.TemporalNetwork.read_file('data/temporal_clusters.tedges')
paths = pp.path_extraction.paths_from_temporal_network_dag(t)

mog = pp.MultiOrderModel(paths, 3)

# Color nodes according to known ground-truth clusters
clusters = { v: 'red' if len(v)<2 else ('green' if v.startswith('1') else 'blue') for v in paths.nodes}

pp.visualisation.plot(mog.layers[mog.estimate_order()], plot_higher_order_nodes=False, node_color=clusters)

#%% In [2]
from random import shuffle

edges = [(v,w) for (v,w,t) in t.tedges]
times = [t for (v,w,t) in t.tedges]
shuffle(times)

t_shuffled = pp.TemporalNetwork()
for i in range(len(edges)):
    t_shuffled.add_edge(edges[i][0], edges[i][1], times[i])
    
paths = pp.path_extraction.paths_from_temporal_network_dag(t_shuffled)

mog = pp.MultiOrderModel(paths, 3)

clusters = { v: 'red' if len(v)<2 else ('green' if v.startswith('1') else 'blue') for v in paths.nodes}

pp.visualisation.plot(mog.layers[mog.estimate_order()], plot_higher_order_nodes=False, node_color=clusters)

#%% In [3]
import scipy.stats

def kendalltau(a, b):
    x = []
    y = []
    for v in set(a.keys()).intersection(set(b.keys())):
            x.append(a[v])
            y.append(b[v])
    return scipy.stats.kendalltau(x, y)

#%% In [4]
import json

def read_gt(file):    
    with open(file, 'r') as f:
        return json.load(f)

#%% In [5]
def validate(mog, gt):
    res = {}
    for k in range(1, mog.max_order+1):
        pr = pp.algorithms.centralities.pagerank(mog.layers[k])
        res[k] = kendalltau(gt, pr).correlation
    return res

#%% In [6]
from matplotlib import pyplot as plt
plt.xkcd()

def plot_results(res, optimal_order):
    if optimal_order>1:
        diff = res[optimal_order] - res[1]
        print('Relative increase over first-order = {0} %'.format(100*diff/res[1]))
    plt.plot(range(1, max(res.keys())+1), [res[k] for k in range(1, max(res.keys())+1)], '-o')
    plt.plot([optimal_order], [res[optimal_order]], 'g', marker='x', markersize=20.0)
    plt.title('Kendall-Tau')
    plt.show()

#%% In [7]
paths = pp.Paths.read_file('data/US_flights_train.ngram', frequency=False)
gt = read_gt('data/US_flights_gt.json')

mog = pp.MultiOrderModel(paths, 3)
order = mog.estimate_order()

res = validate(mog, gt)
plot_results(res, order)

#%% In [8]
import sqlite3
con = sqlite3.connect('data/temporal_networks.db')
con.row_factory = sqlite3.Row

t = pp.TemporalNetwork.from_sqlite(con.execute('SELECT source, target, time FROM manufacturing_email'),
                                   time_rescale=600)
gt = read_gt('data/manufacturing_email_gt.json')

max_order = 3

training_data = t.filter_edges(lambda u,v,time: time<min(t.ordered_times)+0.5*t.observation_length())
paths = pp.path_extraction.sample_paths_from_temporal_network_dag(training_data, 
                                                                  delta=12, 
                                                                  max_subpath_length=max_order, 
                                                                  num_roots=2000)

mog = pp.MultiOrderModel(paths, max_order)
order = mog.estimate_order()

res = validate(mog, gt)
plot_results(res, order)

#%% In [9]
t = pp.TemporalNetwork.from_sqlite(con.execute('SELECT source, target, time FROM haggle'),
                                  time_rescale=10)
gt = read_gt('data/haggle_gt.json')

max_order = 3

training_data = t.filter_edges(lambda u,v,time: time<min(t.ordered_times)+0.5*t.observation_length())
paths = pp.path_extraction.sample_paths_from_temporal_network_dag(training_data, 
                                                                  delta=6, 
                                                                  max_subpath_length=max_order, 
                                                                  num_roots=200)

mog = pp.MultiOrderModel(paths, max_order)
order = mog.estimate_order()

res = validate(mog, gt)
plot_results(res, order)

#%% In [10]
max_order = 4

paths = pp.Paths.read_file('data/tube_paths_train.ngram', max_subpath_length=max_order)
gt = read_gt('data/tube_gt.json')

mog = pp.MultiOrderModel(paths, max_order)
order = mog.estimate_order()

res = validate(mog, gt)
plot_results(res, order)

