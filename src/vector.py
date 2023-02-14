import pandas as pd
from datatest import validate
import numpy as np 
import geopandas as gpd
import folium
from folium import Choropleth, Marker
from folium.features import GeoJsonTooltip
from folium.plugins import MarkerCluster


pitt_map = folium.Map()


folium.GeoJson('https://raw.githubusercontent.com/datasets/geo-admin1-us/master/data/admin1-us.geojson').add_to(pitt_map)

counties_gdf = gpd.read_file(r'C:\Users\favou\Documents\COMP\CriticalJustice\src\Neighborhood_SNAP.shp')
base_df = pd.read_csv(r'C:\Users\favou\Documents\COMP\CriticalJustice\data\shots.csv')
neighbor = pd.read_csv(r"C:\Users\favou\Documents\COMP\CriticalJustice\data\Neighborhood.csv")
neighbor = neighbor[["Pittsburgh_Neighborhood", "Level_of_Need_Scale"]]
fire_data = pd.read_csv(r'C:\Users\favou\Documents\COMP\CriticalJustice\data\FireIncident.csv')

fire_data = fire_data.dropna(subset=['latitude', 'longitude'])

folium.Choropleth(
    geo_data='pittsburgh.geojson',
    data=neighbor,
    columns=['Pittsburgh_Neighborhood', 'Level_of_Need_Scale'],
    key_on='feature.properties.name',
    fill_color='OrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Level of Need Scale in Pittsburgh, Pennsylvania" 
).add_to(pitt_map)


marker_cluster = MarkerCluster().add_to(pitt_map)
marker_cluster_1 = MarkerCluster().add_to(pitt_map)


tooltip = "Incident Type?"
tooltip1 = "Fire Type Description?"

for i, r in base_df.iterrows():
    location =[r['Latitude'], r['Longitude']]
    folium.Marker(location, 
                tooltip=tooltip, 
                popup=r["IncidentType"], 
                icon=folium.Icon(color="blue", icon="person-rifle", prefix='fa')).add_to(marker_cluster)

for i, r in fire_data.iterrows():
    location1 = [r['latitude'], r['longitude']]
    folium.Marker(location1, 
                tooltip1=tooltip1, 
                popup=r["type_description"], 
                icon=folium.Icon(color="red", icon="fire", prefix='fa')).add_to(marker_cluster_1), 

folium.GeoJson(data=counties_gdf["geometry"]).add_to(pitt_map)


folium.LayerControl().add_to(pitt_map)

# save map to html file
pitt_map.save('index.html')