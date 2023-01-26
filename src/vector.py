import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from folium import plugins


# set the filepath and load 
# sf = shp.Reader(r"C:\Users\favou\Documents\COMP\CriticalJustice\src\Neighborhood_SNAP.shp")
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

folium.GeoJson(data=counties_gdf["geometry"]).add_to(pitt_map)

# 

# base_df = pd.read_csv(r'C:\Users\favou\Documents\COMP\CriticalJustice\data\shots.csv')
# print(base_df.head())

neighbor = gpd.datasets.get_path(r"C:\Users\favou\Documents\COMP\CriticalJustice\data\Neighborhood.csv")
df = gpd.read_file(neighbor)
# neighborhood_data = pd.read_csv(neighbor)
center = [40.4406, -79.9959]
 

pitt_map = folium.Map(location=center,zoom_start=5,)
for i, r in df.iterrows():
    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j,
                            style_function=lambda x: {'fillColor': 'orange'})
    folium.Popup(r['Pittsburgh_Neighborhood']).add_to(geo_j)
    geo_j.add_to(pitt_map)
    # location =[r['Latitude'], r['Longitude']]
    # folium.Marker(location).add_to(pitt_map)  

# save map to html file

pitt_map.save('index.html')

# map.save('map.html')