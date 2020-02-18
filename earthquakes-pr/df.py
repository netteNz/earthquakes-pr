import folium
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


lat = []
lon = []


df = pd.read_csv('query45.csv',
                usecols=['latitude', 'longitude',
                        'place', 'mag']
                )

df.sort_index()

for index, row in df.iterrows():

    folium.CircleMarker
    lat.append(row['latitude']), lon.append(row['longitude'])

df.iloc[[0],[0]]
df.iloc[[0],[1]]


pr = folium.Map(location=[18.2208, -66.5901],
                zoom_start=9,
                tiles='cartodbdark_matter'
               )
