"""
This is a test file, that you can use to validate 
"""

#%% validate that pathpy was installed correct
import pathpy as pp
paths = pp.Paths()
paths.add_path('a,b,c')
print(paths)

#%% validate that kernel was started in correct root directory
t = pp.TemporalNetwork.read_file('data/temporal_clusters.tedges')
print(t)

