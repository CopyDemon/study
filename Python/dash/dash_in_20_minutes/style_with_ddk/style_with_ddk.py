"""
This is a practice to style the app with ddk
This is from official Dash tutorial


!!! can't run this because of the ddk require dash enterprise license
"""

from dash import Dash, html, dcc, dash_table, callback, Input, Output
import pandas as pd
import plotly.express as px
import dash_design_kit as ddk

# load data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

# initialize app
app = Dash(__name__)

# app layout
app.layout = []

if __name__ == "__main__":
    app.run(debug=True)
