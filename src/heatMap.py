#!/usr/bin/env python3
"""Plotting Folium Map with Shots Fired Data of Pittsburgh, PA"""


import folium
from folium import plugins
import numpy as np # linear algebra
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_df = pd.read_csv(r'C:\Users\favou\Documents\COMP\CriticalJustice\data\shots.csv')
print(base_df.head())

center = [40.4406, -79.9959]

pitt_map = folium.Map(location=center,zoom_start=5,)
tooltip = "Incident Type?"
for i, r in base_df.iterrows():
    folium.CircleMarker([r['Latitude'], r['Longitude']],
                        radius=15,
                        tooltip=tooltip,
                        popup=r['IncidentType'],
                        fill_color="#3db7e4", # divvy color
                        ).add_to(pitt_map)

# convert to (n, 2) nd-array format for heatmap
mapArr = base_df[['Latitude', 'Longitude']].to_numpy()

# plot heatmap

pitt_map.add_child(plugins.HeatMap(mapArr, radius=15))

# save map to html file

pitt_map.save('heat.html')

