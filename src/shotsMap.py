# Python program to create a map that displays shots fired data as map

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import contextily as ctx
import csv

lat, lon, date = [],[],[]

with open('shots.csv') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=',')
    for data in reader:
        lat.append(float(data['Latitude']))
        lon.append(float(data['Longitude']))
        date.append(data['Date'])

# input desired coordiantes

my_coords = [40.4406, 79.9959]

zoom_scale = 1

bbox = [my_coords[0]-zoom_scale, my_coords[0]+zoom_scale,\
        my_coords[1]-zoom_scale, my_coords[1]+zoom_scale]

plt.figure(figsize=(12,6))

# defining projection, scale, corners of the map, and resolution
m = Basemap(projection='merc',llcrnrlat=bbox[0],urcrnrlat=bbox[1],\
            llcrnrlon=bbox[2],urcrnrlon=bbox[3],lat_ts=10,resolution='i')

# Draw coastlines and fill continents and water with color
m.drawcoastlines()
m.fillcontinents(color='peru',lake_color='dodgerblue')

# Draw parallels, meridians, and color boundaries
m.drawparallels(np.arange(bbox[0],bbox[1],(bbox[1]-bbox[0])/5),labels=[1,0,0,0])
m.drawmeridians(np.arange(bbox[2],bbox[3],(bbox[3]-bbox[2])/5),labels=[0,0,0,1],rotation=45)

m.drawmapboundary(fill_color='dodgerblue')

# read a shape file as a geodataframe
gdf = gpd.read_file(r'C:\Users\favou\Documents\COMP\CriticalJustice\src\Allegheny_County_Census_Block_Groups_2016.shp')

# convert from one crs to another
gdf_3857 = gdf.to_crs(epsg=3857)
ax = gdf_3857.plot()
ctx.add_basemap(ax)
plt.show()
 
# Build and plot coordiantes onto map
plt.title("Shots Fired Data Map")
plt.savefig('map_test.png', format='png', dpi=500)
