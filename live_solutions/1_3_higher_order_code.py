#%% In [1]
import pathpy as pp
help(pp.HigherOrderNetwork)

#%% In [2]
toy_paths = pp.Paths.read_file('data/toy_paths.ngram')
print(toy_paths)

hon_1 = pp.HigherOrderNetwork(toy_paths, k=1)
print(hon_1)

#%% In [3]
style = { 'label_offset': [0,-1], 'label_color' : 'black', 'width': 600, 'height': 600}
pp.visualisation.plot(hon_1, **style)
for e in hon_1.edges:
    print(e, hon_1.edges[e]['weight'])

#%% In [5]
hon_2 = pp.HigherOrderNetwork(toy_paths, k=2)
pp.visualisation.plot(hon_2, **style)

for e in hon_2.edges:
    print(e, hon_2.edges[e])

#%% In [6]
hon_2_null = pp.HigherOrderNetwork(toy_paths, k=2, null_model=True)
pp.visualisation.plot(hon_2_null, **style)

for e in hon_2_null.edges:
    print(e, hon_2_null.edges[e])

#%% In [7]
A_2 = hon_2.adjacency_matrix()
idx_2 = hon_2.node_to_name_map()

A_2n = hon_2_null.adjacency_matrix()
idx_2n = hon_2_null.node_to_name_map()

for (v,w) in hon_2_null.edges:
    print(e, A_2[idx_2[v],idx_2[w]] - A_2n[idx_2n[v],idx_2n[w]])

#%% In [8]
print(pp.algorithms.centralities.betweenness(hon_1)['c'])

#%% In [9]
print(pp.algorithms.centralities.betweenness(toy_paths)['c'])

#%% In [10]
print(pp.algorithms.centralities.betweenness(hon_2)['c'])

#%% In [11]
print(pp.algorithms.centralities.betweenness(hon_2_null)['c'])

#%% In [13]
training_paths = pp.Paths.read_file('data/US_flights_train.ngram', frequency=False)

hon_1 = pp.HigherOrderNetwork(training_paths, k=1)
hon_2 = pp.HigherOrderNetwork(training_paths, k=2)
hon_3 = pp.HigherOrderNetwork(training_paths, k=3)

pr_1 = pp.algorithms.centralities.pagerank(hon_1)
pr_2 = pp.algorithms.centralities.pagerank(hon_2)
pr_3 = pp.algorithms.centralities.pagerank(hon_3)

# with this, we generate 
pr_1 = [pr_1[v] for v in training_paths.nodes]
pr_2 = [pr_2[v] for v in training_paths.nodes]
pr_3 = [pr_3[v] for v in training_paths.nodes]

#%% In [14]
validate_paths = pp.Paths.read_file('data/US_flights_validate.ngram', frequency=False)

traversals = pp.algorithms.centralities.node_traversals(validate_paths)
rank_true = [traversals[v] for v in training_paths.nodes]

#%% In [15]
from scipy.stats import kendalltau

print('tau(pr_1, traversals) = {0}'.format(kendalltau(pr_1, rank_true).correlation))
print('tau(pr_2, traversals) = {0}'.format(kendalltau(pr_2, rank_true).correlation))
print('tau(pr_3, traversals) = {0}'.format(kendalltau(pr_3, rank_true).correlation))

#%% In [16]
n = pp.Network(directed=True)
n.add_edge('a', 'c')
n.add_edge('b', 'c')
n.add_edge('c', 'd')
n.add_edge('d', 'f')
n.add_edge('d', 'g')
n

#%%
od_stats = [('a', 'f', 5), ('b', 'g', 10)]

#%%
paths = pp.path_extraction.paths_from_origin_destination(od_stats, n)
print(paths)