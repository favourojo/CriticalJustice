import folium
import branca 
import pandas as pd

df = pd.read_csv(r'...data\pennsylvania.csv', index_col=0)
df.head()