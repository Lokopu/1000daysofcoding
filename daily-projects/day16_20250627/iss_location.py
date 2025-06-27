import requests
import json
import pandas as pd
import os
import altair as alt
from vega_datasets import data
import time
import plotly.graph_objects as go
import plotly.io as pio

# 25544 = ID of the international space station

URL = "https://api.wheretheiss.at/v1/satellites/25544"
pio.renderers.default = "notebook"

def main():
    starttime = time.monotonic()
    # while True:
        # print("tick")
        # time.sleep(60.0 - ((time.monotonic() - starttime) % 60.0))
    df = iss_location_data(URL)
    append_to_csv(df)
    plot(read_csv())

def iss_location_data(url):
    request = requests.get(url)

    response = json.loads(request.text)

    df = pd.DataFrame.from_dict([response])
    df = df[["timestamp", "latitude", "longitude"]]
    return df

def append_to_csv(df):
    output_path = "iss_location.csv"
    if os.path.getsize(output_path) == 0:
        df.to_csv(output_path, mode="w", index=False)
    else:
        df.to_csv(output_path, mode="a", header=not os.path.exists(output_path), index=False)

def read_csv():
    path = "iss_location.csv"
    df = pd.read_csv(path)
    df["timestamp"].nlargest(n=5)
    return df


def plot(df):
    largest_idx = df['timestamp'].idxmax()
    center_lat, center_lon = df.loc[largest_idx, ['latitude', 'longitude']]
    fig = go.Figure(go.Scattergeo(lat=df["latitude"], lon=df["longitude"]))
    #editing the marker
    fig.update_traces(marker_size=20, line=dict(color='Red'))
    # this projection_type = 'orthographic is the projection which return 3d globe map'
    fig.update_geos(projection_type="orthographic",
                    center=dict(lat=center_lat, lon=center_lon),
        # Optionally, set the projection rotation to focus on the center
        projection_rotation=dict(lat=center_lat, lon=center_lon)
        )
    #layout, exporting html and showing the plot
    fig.update_layout(width= 800, height=800, margin={"r":0,"t":0,"l":0,"b":0})
    fig.write_html("3d_plot.html")
    

if __name__ == "__main__":
    main()
