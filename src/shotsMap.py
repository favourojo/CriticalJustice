#!/usr/bin/env python3

import folium
from folium import plugins
import numpy as np # linear algebra
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_df = pd.read_csv(r'C:\Users\favou\Documents\COMP\CriticalJustice\data\shots.csv')
print(base_df.head())
center = [40.4406, -79.9959]

"""Plotting Map with Shots Fired Data of Pittsburgh, PA"""
pitt_map = folium.Map(location=center,zoom_start=5,)
for i, r in base_df.iterrows():
    location =[r['Latitude'], r['Longitude']]
    folium.Marker(location, popup = f'Type of Shot:{r["Class"]}').add_to(pitt_map)

# save map to html file
pitt_map.save('index.html')