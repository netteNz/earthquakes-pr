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


def plot(point):
    lat = []
    lon = []

    for i, row in df.iterrows():
        lat.append(row[i]['latitude']), lon.append(row[i]['longitude'])
        folium.CircleMarker(location=[point.lat, point.lon], radius=2).add_to(pr)
