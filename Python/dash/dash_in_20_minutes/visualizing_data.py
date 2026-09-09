"""
This is a practice for visualizing data in Dash.
With official 20 minutes tutorial.
"""

from dash import Dash, html, dcc, dash_table
import pandas as pd
import plotly.express as px  # graph is come from here

# Load data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div("My first app with data and a graph"),
    dash_table.DataTable(data=df.to_dict("records"), page_size=10),
    dcc.Graph(
        figure=px.histogram(df, x="continent", y="lifeExp", histfunc="avg"),
    ),
]


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
