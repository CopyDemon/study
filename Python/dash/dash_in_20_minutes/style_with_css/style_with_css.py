"""
This is a practice to style the app with css
This is from official Dash tutorial
"""

from dash import Dash, html, dcc, dash_table, callback, Input, Output
import pandas as pd
import plotly.express as px
import os

# load data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

# import css file
external_stylesheets = [
    "https://codepen.io/chriddyp/pen/bWLwgP.css",
    os.path.join(os.path.dirname(__file__), "dash_with_css.css"),
]

# initialize app
app = Dash(external_stylesheets=external_stylesheets)

# app layout
app.layout = [
    # html.H1(className="row", children="My First dash app with CSS style"),
    html.Div(
        className="row title",
        children="App plus style test",
        style={"textAlign": "center", "color": "blue", "fontSize": 30},
    ),
    dcc.RadioItems(
        className="row",
        options=["pop", "lifeExp", "gdpPercap"],
        value="pop",
        inline=True,
        id="my-radio-buttons-final",
    ),
    html.Div(
        className="row",
        children=[
            html.Div(
                className="six columns",
                children=[
                    dash_table.DataTable(
                        data=df.to_dict("records"),
                        page_size=10,
                        style_table={"overflowX": "auto"},
                    ),
                ],
            ),
            html.Div(
                className="six columns",
                children=[
                    dcc.Graph(figure={}, id="histo-chart-final"),
                ],
            ),
        ],
    ),
]


# Add controls to build the interaction
@callback(
    Output(component_id="histo-chart-final", component_property="figure"),
    Input(component_id="my-radio-buttons-final", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
