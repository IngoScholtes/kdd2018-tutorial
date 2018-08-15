#%%
import pathpy as pp

#%%
t = pp.TemporalNetwork()
t.add_edge('a', 'b', 1)
t.add_edge('b', 'a', 3)
t.add_edge('b', 'c', 3)
t.add_edge('d', 'c', 4)
t.add_edge('c', 'd', 5)
t.add_edge('c', 'b', 6)
print(t)

#%% 
t

#%%
params = {
    'ms_per_frame': 1000, 
    'ts_per_frame': 1, 
    'look_ahead': 2, 
    'look_behind': 2, 
    'node_size': 15, 
    'width': 800, 
    'height': 800, 
    'inactive_edge_width': 2, 
    'active_edge_width': 4, 
    'label_color' : '#ffffff',
    'label_size' : 18,
    'label_offset': [0,0]
    }
pp.visualisation.plot(t, **params)

#%%
pp.visualisation.export_html(t, 'visualisations/2_1_temporal_network.html', **params)

#%%
t = pp.TemporalNetwork.read_file('data/temporal_clusters.tedges')
t

#%% 
params = {
    'ms_per_frame': 1,
    'ts_per_frame': 1
}
pp.visualisation.plot(t, **params)

#%%
pp.visualisation.plot(pp.Network.from_temporal_network(t))

#%%
p = pp.path_extraction.paths_from_temporal_network_dag(t)
hon_2 = pp.HigherOrderNetwork(p, k=2)
print(hon_2)

#%%
pp.visualisation.plot(hon_2, plot_higher_order_nodes=False)
