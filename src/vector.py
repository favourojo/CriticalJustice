import os
import pandas as pd
from datatest import validate
import numpy as np 
import shapefile as shp
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from folium import Choropleth, Circle, Marker
from folium.features import GeoJsonTooltip
from folium.plugins import MarkerCluster


pitt_map = folium.Map()

folium.GeoJson('https://raw.githubusercontent.com/datasets/geo-admin1-us/master/data/admin1-us.geojson').add_to(pitt_map)

counties_gdf = gpd.read_file(r"C:\Users\favou\Documents\COMP\CriticalJustice\src\Neighborhood_SNAP.shp")



base_df = pd.read_csv(r'C:\Users\favou\Documents\COMP\CriticalJustice\data\shots.csv')
neighbor = pd.read_csv(r"C:\Users\favou\Documents\COMP\CriticalJustice\data\Neighborhood.csv")
neighbor = neighbor[["Pittsburgh_Neighborhood", "Black_Pop_Rate"]]

fire_data = pd.read_csv(r'C:\Users\favou\Documents\COMP\CriticalJustice\data\FireIncident.csv')

fire_data = fire_data.dropna(subset=['latitude', 'longitude'])

folium.Choropleth(
    geo_data='pittsburgh.geojson',
    data=neighbor,
    columns=['Pittsburgh_Neighborhood', 'Black_Pop_Rate'],
    key_on='feature.properties.name',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Black Population Rate in Pittsburgh, Pennsylvania" 
).add_to(pitt_map)




marker_cluster = MarkerCluster().add_to(pitt_map)
marker_cluster_1 = MarkerCluster().add_to(pitt_map)




tooltip = "Incident Type?"
tooltip1 = "Neighborhood Name?"

for i, r in base_df.iterrows():
    location =[r['Latitude'], r['Longitude']]
    # folium.Marker(location, tooltip=tooltip, popup=r["IncidentType"]).add_to(pitt_map)
    folium.Marker(location, tooltip=tooltip, popup=r["IncidentType"]).add_to(marker_cluster)

for i, r in fire_data.iterrows():
    location1 = [r['latitude'], r['longitude']]
    folium.Marker(location1, popup=r["type_description"], icon=folium.Icon(color="red", icon="fire", prefix='fa')).add_to(marker_cluster_1), 

folium.GeoJson(data=counties_gdf["geometry"]).add_to(pitt_map)

fg1 = folium.FeatureGroup(name = 'Inlines', show=False)
fg2 = folium.FeatureGroup(name = 'Choropleth', show=False)
fg3 = folium.FeatureGroup(name = 'Shots Fired Data', show=False)
fg4 = folium.FeatureGroup(name = 'Pittsburgh ShapeFile',show=False)

pitt_map.add_child(fg1)
pitt_map.add_child(fg2)
pitt_map.add_child(fg3)
pitt_map.add_child(fg4)

folium.TileLayer('openstreetmap').add_to(pitt_map)


pitt_map.add_child(folium.LayerControl())


# save map to html file
pitt_map.save('index.html')

