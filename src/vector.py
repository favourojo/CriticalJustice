import pandas as pd
from datatest import validate
import numpy as np 
import branca
import geopandas as gpd
import folium
from folium import Choropleth, Marker
from folium.plugins import FloatImage
from folium.features import GeoJsonTooltip
from folium.plugins import MarkerCluster

loc = "CriticalJustice"
title_html = '''
            <h3 align="center" style="font-size:24px"><b>{}</b></h3>
            '''.format(loc)

legend_html = '''
{% macro html(this, kwargs) %}
<div style="
    position: fixed; 
    bottom: 50px;
    left: 50px;
    width: 250px;
    height: 80px;
    z-index:9999;
    font-size:14px;
    ">
    <p><a style="color:#FD0505;font-size:150%;margin-left:20px;">&diams;</a>&emsp;Fire Incidents</p>
    <p><a style="color:#05BDFD;font-size:150%;margin-left:20px;">&diams;</a>&emsp;Shots Fired</p>
</div>
<div style="
    position: fixed; 
    bottom: 50px;
    left: 50px;
    width: 150px;
    height: 80px; 
    z-index:9998;
    font-size:14px;
    background-color: #ffffff;

    opacity: 0.7;
    ">
</div>
{% endmacro %}
'''
legend = branca.element.MacroElement()
legend._template = branca.element.Template(legend_html)


pitt_map = folium.Map()

pitt_map.get_root().html.add_child(folium.Element(title_html))

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
    fill_color='YlOrRd',
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
pitt_map.get_root().add_child(legend)

compass_rose = folium.FeatureGroup('compass rose')
FloatImage('https://upload.wikimedia.org/wikipedia/commons/9/99/Compass_rose_simple.svg', bottom =80, left = 7).add_to(compass_rose)
compass_rose.add_to(pitt_map)

# save map to html file
pitt_map.save('index.html')