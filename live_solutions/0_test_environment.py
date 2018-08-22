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


#%% validate that infomap is installed correctly
import infomap
print("Infomap version:", infomap.Infomap().version)
print("Make sure it is at least 1.0.0-beta.14")

#%% check that relative read and write works
from pathlib import Path
Path('output').mkdir(exist_ok=True)
im = infomap.Infomap("")
im.network().readInputData("data/ninetriangles.net")
im.run()
im.writeClu("output/ninetriangles.clu")
print(im.maxTreeDepth()) # Should print 3
