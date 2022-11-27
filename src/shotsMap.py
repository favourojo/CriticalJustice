# Python program to create a map that displays shots fired data as map

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import descartes 
import geopandas as gpd 
from shapely.geometry import Point, Polygon

# Read Pittsburgh, PA shots fired data
shots = pd.read_csv('/home/ojof/Documents/COMP/CriticalJustice/data/pittsburgh_pa.csv')
assert shots.shape == (49352, 34)

# import street map 
street_map = gpd.read_file('/home/ojof/Documents/COMP/CriticalJustice/src/Allegheny_County_Census_Block_Groups_2016.shp')

# designate coordiante system 
crs = {'init':'espc:4326'}

# zip x and y coordinates into single feature 
geometry = [Point(xy) for xy in zip(shots['longitude'], shots['latitude'])]

# create GeoPandas dataframe
geo_df = gpd.GeoDataFrame(shots, crs = crs, geometry = geometry)



# plt.show()