#%% In [1]
import pathpy as pp

#%% In [2]
help(pp.Paths)

#%% In [3]
toy_paths = pp.Paths()

#%% In [4]
toy_paths.add_path(('a', 'c', 'd'), frequency=10)

#%% In [5]
print(toy_paths)

#%% In [6]
ngram_paths = pp.Paths()
ngram_paths.add_path('b-c-e',  separator='-', frequency=10)
print(ngram_paths)

#%% In [7]
toy_paths += ngram_paths
print(toy_paths)

#%% In [8]
toy_paths.write_file('data/toy_paths.ngram')

#%% In [9]
toy_graph = pp.Network.from_paths(toy_paths)
print(toy_graph)

#%% In [10]
print('Weight of edge (a,c) is {0}'.format(toy_graph.edges[('a', 'c')]['weight']))

#%% In [11]
print('Frequency of path (a,c) as subpath of length one is {0}'.format(toy_paths.paths[1][('a', 'c')][0]))

#%% In [12]
# we can assign arbitrary additional attribute values to nodes and edges
toy_graph.edges[('a', 'c')]['edge_property'] = 'some value'
toy_graph.edges[('c', 'd')]['edge_property'] = 'some other value'
toy_graph.nodes['a']['node_property'] = 42.0
toy_graph.nodes['b']['node_property'] = 0.0
toy_graph.edges[('a', 'c')]['label'] = 'my_label'

# return edges with a given attribute value
print('Edges that satisfy edge_propery == "some value": ' + \
      str(toy_graph.find_edges(select_edges = lambda e: 'edge_property' in e and e['edge_property'] == 'some value')))

# return nodes with a given attribute value
print('Nodes that satisfy node_property > 40.0: ' + \
      str(toy_graph.find_nodes(select_node = lambda v: 'node_property' in v and v['node_property'] > 40.0)))

#%% In [18]
toy_graph

#%% In [14]
pp.visualisation.plot(toy_graph, node_color='red')

#%% In [15]
help(pp.visualisation.plot)

#%% In [16]
style = {'width': 300, 
          'height': 300,
          'node_size': 18.0,
          'edge_width' : 4.0,
          'node_color' : {'a': '#aacc99', 'b': '#aacc99', 'd': '#aacc99', 'e': '#aacc99', 'c': '#cc6666'},
          'edge_color' : '#ffaaaa',
          'edge_arrows': False,
          'label_color': '#000000',
          'label_opacity': 1,
          'label_offset': [0,0],
          'label_size': '20px',
          'edge_opacity': 1, 
          'force_charge': -10.0, 
          'force_repel': -550, 
          'force_alpha': 0.01
         }
pp.visualisation.plot(toy_graph, **style)

#%% In [17]
pp.visualisation.export_html(toy_graph, filename='visualisations/1_2_simple_network.html', **style)
