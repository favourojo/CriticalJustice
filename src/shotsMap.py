# Python program to create a map that displays shots fired data as map

import branca
import folium
import pandas as pd
import matplotlib.pyplot as plt 
import geopandas as gpd 


# Read Pittsburgh, PA shots fired data
shots = pd.read_csv(
    "C:\\Users\\favou\\Documents\\COMP\\CriticalJustice\\data",
    header=0,
    dtype={0:str, 1:str, 2:float, 3:float, 4:str})
print(shots.shape)
# Import street map 
street_map = gpd.read_file('/home/ojof/Documents/COMP/CriticalJustice/src/Allegheny_County_Census_Block_Groups_2016.shp')

# designate coordiante system 
crs = {'init':'espc:4326'}  
# zip x and y coordinates into single feature

geometry = [Point(xy) for xy in zip(shots['longitude'], shots['latitude'])]

# Create GeoPandas dataframe
#geo_df = gpd.GeoDataFrame(shots, crs = crs, geometry = geometry)
geo_df = gpd.GeoDataFrame(shots, geometry = geometry)

# Create figure and axes, assigning to a subplot
fig, ax = plt.subplots(figsize=(15,15))

# Add .shp mapfile to axes
street_map.plot(ax=ax, alpha=0.4,color='grey')

geo_df.plot(column='longitude' & 'latitude', ax=ax, alpha=0.5,
            legend=True, markersize=10)

# Add title to graph
plt.title('Shots Fired Data in Pittsburgh', 
fontsize=15, fontweight='bold')

# Show map
plt.show()