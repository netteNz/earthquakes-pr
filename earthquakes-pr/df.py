import folium
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('query45.csv')
pr = folium.Map(location=[18.2208, -66.5901],
                zoom_start=9,
                tiles='cartodbdark_matter'
               )

