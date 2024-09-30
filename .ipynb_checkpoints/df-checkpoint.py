# Data frame

import pandas as pd
import folium
import matplotlib.pyplot as plt


def main():
    pr_map = folium.Map(location=[18.000, -66.000])
    df = pd.read_csv('query45.csv')

    return pr_map


if __name__ == '__main__':
    main()