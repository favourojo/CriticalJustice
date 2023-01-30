import os
import pandas as pd
import numpy as np 
import shapefile as shp
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from folium import Choropleth, Circle, Marker
from folium.features import GeoJsonTooltip
from folium.plugins import MarkerCluster


# set the filepath and load 
# data = pd.read_csv(r"C:\Users\favou\Documents\COMP\CriticalJustice\data\shots.csv")
# plt.figure()
# for shape in sf.shapeRecords():
#  x = [i[0] for i in shape.shape.points[:]]
# y = [i[1] for i in shape.shape.points[:]]
# plt.plot(x,y)
# plt.show()

pitt_map = folium.Map()

folium.GeoJson('https://raw.githubusercontent.com/datasets/geo-admin1-us/master/data/admin1-us.geojson').add_to(pitt_map)

counties_gdf = gpd.read_file(r"C:\Users\favou\Documents\COMP\CriticalJustice\src\Neighborhood_SNAP.shp")
print(counties_gdf.head)



base_df = pd.read_csv(r'C:\Users\favou\Documents\COMP\CriticalJustice\data\shots.csv')
neighbor = pd.read_csv(r"C:\Users\favou\Documents\COMP\CriticalJustice\data\Neighborhood.csv")


folium.Choropleth(
    geo_data='https://raw.githubusercontent.com/datasets/geo-admin1-us/master/data/admin1-us.geojson',
    data=neighbor,
    columns=['Pittsburgh_Neighborhood', 'Black_Pop_Rate'],
    key_on='feature.properties.id',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Black Population Rate" 
).add_to(pitt_map)


marker_cluster = MarkerCluster().add_to(pitt_map)

tooltip = "Incident Type?"

for i, r in base_df.iterrows():
    location =[r['Latitude'], r['Longitude']]
    # folium.Marker(location, tooltip=tooltip, popup=r["IncidentType"]).add_to(pitt_map)
    folium.Marker(location, tooltip=tooltip, popup=r["IncidentType"]).add_to(marker_cluster)
# save map to html file
folium.GeoJson(data=counties_gdf["geometry"]).add_to(pitt_map)


folium.LayerControl(collapsed=False).add_to(pitt_map)



pitt_map.save('index.html')

# map.save('map.html')