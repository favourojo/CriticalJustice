import pandas as pd
from datatest import validate
import branca
import geopandas as gpd
import time
from datetime import datetime
import folium
import json
from folium import Choropleth, Marker
from folium.plugins import FloatImage
from folium.features import GeoJsonTooltip
from folium.plugins import MarkerCluster

loc = "CriticalJustice"

title_html = '''
          <h3 align="center" style="font-size:24px; margin-top: -4px; margin-bottom: -2px;"><b>{}</b></h3>
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

pitt_map = folium.Map(zoom_start=12)

fg1 = folium.FeatureGroup(name='GeoJSON Layer')
fg2 = folium.FeatureGroup(name='Shots Fired Incidents')
fg3 = folium.FeatureGroup(name='Fire Incidents')
fg5 = folium.FeatureGroup(name='Borders')
fg6 = folium.FeatureGroup(name='Scale Indicator')


pitt_map.get_root().html.add_child(folium.Element(title_html))

print("Acquiring GeoJSON")

folium.GeoJson('https://raw.githubusercontent.com/datasets/geo-admin1-us/master/data/admin1-us.geojson').add_to(fg1)

counties_gdf = gpd.read_file(r'Neighborhood_SNAP.shp')
base_df = pd.read_csv(r'Shots.csv')
neighbor = pd.read_csv(r'Neighborhood.csv')
fire_data = pd.read_csv(r'FireIncident.csv')

fire_data = fire_data.dropna(subset=['latitude', 'longitude'])

print("Loaded datasets...")

choropleth = folium.Choropleth(
    geo_data='pittsburgh.geojson',
    data=neighbor,
    columns=['Pittsburgh_Neighborhood', 'Level_of_Need_Scale'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    nan_fill_color="Grey",
    fill_opacity=0.7,
    line_opacity=0.2,
    highlight=True,
    legend_name="Level of Need Scale",
    line_color='black'
).add_to(pitt_map)


print("Map creation complete...")

marker_cluster = MarkerCluster().add_to(fg2)
marker_cluster_1 = MarkerCluster().add_to(fg3)


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



folium.GeoJson(data=counties_gdf["geometry"]).add_to(fg5)

sw = base_df[['Latitude', 'Longitude']].min().values.tolist()
ne = base_df[['Latitude', 'Longitude']].max().values.tolist()

pitt_map.fit_bounds([sw,ne])

print("Finished mapping sets...")

FloatImage('https://upload.wikimedia.org/wikipedia/commons/9/99/Compass_rose_simple.svg', bottom =80, left = 7).add_to(pitt_map)

print("Compass rose added...")

fg1.add_to(pitt_map)
fg2.add_to(pitt_map)
fg3.add_to(pitt_map)
fg5.add_to(pitt_map)
fg6.add_to(pitt_map)




folium.LayerControl().add_to(pitt_map)
pitt_map.get_root().add_child(legend)

# save map to html file
pitt_map.save('index.html')

print("Saved HTML file!")
