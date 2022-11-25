# Python program to create a map that displays shots fired data as map

import pandas as pd
import matplotlib.pyplot as plt 
import descartes 
import geopandas as gpd 
from shapely.geometry import Point, Polygon

Pitt_map = gpd.read_file('/home/ojof/Documents/COMP/CriticalJustice/src/Allegheny_County_Census_Block_Groups_2016.shp')

fig,ax = plt.subplots(figsize = (15,15))
Pitt_map.plot(ax = ax)

df = pd.read_csv()



plt.show()

