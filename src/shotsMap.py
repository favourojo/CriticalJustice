# Python program to create a map that displays shots fired data as map

import pandas as pd
import matplotlib.pyplot as plt 
import descartes 
import geopandas as gpd 
from shapely.geometry import Point, Polygon

# Create map with shape file 
Pitt_map = gpd.read_file('/home/ojof/Documents/COMP/CriticalJustice/src/Allegheny_County_Census_Block_Groups_2016.shp')

fig,ax = plt.subplots(figsize = (15,15))
Pitt_map.plot(ax = ax, alpha = 0.4, color="grey")

# Get data in the right format
df = pd.read_csv('/home/ojof/Documents/COMP/CriticalJustice/data/pittsburgh_pa.csv')
crs = {'init': 'espg:4326'}
df.head()

geometry = [Point(xy) for xy in zip(df["longitude"], df["latitude"])]
geo_df = gpd.GeoDataFrame(df, crs = crs, geometry = geometry)

geo_df.head()

geo_df[geo_df['WnvPresent'] == 0].plot(ax = ax, markersize = 20, color = "blue", marker = "o")



plt.show()