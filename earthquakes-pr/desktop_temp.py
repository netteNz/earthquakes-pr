import folium
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pr = folium.Map(location=[18.2208, -66.5901],
                zoom_start=9,
                tiles='cartodbdark_matter'
               )

df = pd.read_csv('query45.csv',
                 usecols=['latitude', 'longitude','place', 'mag'],
                )

lat = []
lon = []

for index, row in df.iterrows():
    lat.append(row['latitude']), lon.append(row['longitude'])
    print(lat,lon)