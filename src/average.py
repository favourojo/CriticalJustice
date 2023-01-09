import pandas as pd
import numpy as np
import folium
import matplotlib.pyplot as plt 
import contextily as ctx

# Read into CSV file
nei_df = pd.read_csv(r'C:\Users\favou\Documents\COMP\CriticalJustice\data\Neighborhood.csv')

print(nei_df.head())

# Selecting a specifc column in CSV dataset
black = nei_df["Black_Pop_Rate"]


# Open .geojson file and store contents in a variable
pittmapdata = r'C:\Users\favou\Documents\COMP\CriticalJustice\src\pittsburgh.json'

center = [40.4406, -79.9959]

pitt_map = folium.Map(location=center,zoom_start=5,)

folium.Choropleth(
    geo_data=pittmapdata,
    name="choropleth",
    data=nei_df,
    columns=["Pittsburgh_Neighborhood", "Black_Pop_Rate"],
    key_on="feature.properties.id",
    fill_color="BuPu",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Black Population By Pittsburgh Neighborhood",
).add_to(pitt_map)

folium.LayerControl().add_to(pitt_map)

pitt_map.save('black.html')