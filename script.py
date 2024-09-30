import folium
import pandas as pd
import numpy as np

coor = []


def base_map(default_location=[18.2208, -66.5901], default_zoom=9):
    pr = folium.Map(location=default_location,
                    control_scale=True,
                    zoom_start=default_zoom,
                    tiles='cartodbdark_matter'
                    )
    return pr


def read_data():
    df = pd.read_csv('D:/Projects/earthquakes-pr/earthquakes-pr/query45.csv', 
                    usecols=['latitude', 'longitude','place', 'mag']
                     )

    for i, row in df.iterrows():
        coor.append(row['latitude']), coor.append(row['longitude'])
        print(coor)

if __name__ == '__main__':
    read_data()