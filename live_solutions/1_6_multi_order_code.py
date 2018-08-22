#%% In [1]
import pathpy as pp

toy_paths = pp.Paths()
toy_paths.add_path('a,c,d', 2)
toy_paths.add_path('b,c,e', 2)
print(toy_paths)

#%% In [2]
hon_1 = pp.HigherOrderNetwork(toy_paths)
pp.visualisation.plot(hon_1)
print(hon_1.transition_matrix())

#%% In [3]
print(hon_1.likelihood(toy_paths, log=False))

#%% In [4]
hon_2 = pp.HigherOrderNetwork(toy_paths, k=2)
print(hon_2.transition_matrix())
print(hon_2.likelihood(toy_paths, log=False))

#%% In [6]
hon_2_null = pp.HigherOrderNetwork(toy_paths, k=2, null_model=True)
pp.visualisation.plot(hon_2_null)
print(hon_2.transition_matrix())
hon_2_null.likelihood(toy_paths, log=False)

#%% In [7]
from scipy.stats import chi2

d = hon_2.degrees_of_freedom() - hon_1.degrees_of_freedom()
x = - 2 * (hon_1.likelihood(toy_paths, log=True) - hon_2.likelihood(toy_paths, log=True))
p = 1 - chi2.cdf(x, d)

print('p-value of null hypothesis (first-order) is {0}'.format(p))

#%% In [8]
toy_paths *= 2

x = - 2 * (hon_1.likelihood(toy_paths, log=True) - hon_2.likelihood(toy_paths, log=True))
p = 1 - chi2.cdf(x, d)

print('p-value of null hypothesis (first-order) is {0}'.format(p))

#%% In [9]
path = ('a','b','c','d','e','c','b','a','c','d','e','c','e','d','c','a')

p = pp.Paths()
p.add_path(path)
pp.visualisation.plot(pp.Network.from_paths(p))

hon_1 = pp.HigherOrderNetwork(p, k=1)
hon_2 = pp.HigherOrderNetwork(p, k=2, null_model=True)
hon_5 = pp.HigherOrderNetwork(p, k=5, null_model=True)

print(hon_1.likelihood(p, log=False))
print(hon_2.likelihood(p, log=False))
print(hon_5.likelihood(p, log=False))

#%% In [10]
print('Path consists of {0} nodes'.format(len(path)))
print('Number of transitions in  first-order model = ', str(len(hon_1.path_to_higher_order_nodes(path)[1:])))
print('Number of transitions in second-order model = ', str(len(hon_2.path_to_higher_order_nodes(path)[1:])))
print('Number of transitions in  fifth-order model = ', str(len(hon_5.path_to_higher_order_nodes(path)[1:])))

#%% In [11]
mog = pp.MultiOrderModel(toy_paths, max_order=2)
print(mog)

pp.visualisation.plot(mog.layers[0])
pp.visualisation.plot(mog.layers[1])
pp.visualisation.plot(mog.layers[2])

#%% In [12]
toy_paths *= 5
mog = pp.MultiOrderModel(toy_paths, max_order=2)

d = mog.degrees_of_freedom(max_order=2) - mog.degrees_of_freedom(max_order=1)
x = - 2 * (mog.likelihood(toy_paths, log=True, max_order=1) - mog.likelihood(toy_paths, log=True, max_order=2))
p = 1 - chi2.cdf(x, d)

print('p value of null hypothesis (max. order 1) = {0}'.format(p))

#%% In [13]

mog.estimate_order()

#%% In [14]
random_paths = pp.Paths()
random_paths.add_path('a,c,d', 5)
random_paths.add_path('a,c,e', 5)
random_paths.add_path('b,c,e', 5)
random_paths.add_path('b,c,d', 5)

mog = pp.MultiOrderModel(random_paths, max_order=2)
print('Optimal order = ', mog.estimate_order(random_paths))

#%% In [15]
p = pp.Paths()
p.add_path('a,c,d,f', 5)
p.add_path('b,c,d,g', 5)

m = pp.MultiOrderModel(p, max_order=3)
print('Optimal maximum order is {0}'.format(m.estimate_order()))

#%% In [17]
pp.visualisation.plot(m.layers[1], plot_higher_order_nodes=False)
pp.visualisation.plot(m.layers[2], plot_higher_order_nodes=False)
pp.visualisation.plot(m.layers[3], plot_higher_order_nodes=False)

#%% In [20]
pp.visualisation.plot(m, plot_higher_order_nodes=False)
