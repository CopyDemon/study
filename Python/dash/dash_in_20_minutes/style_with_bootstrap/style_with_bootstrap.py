"""
This is a practice to style the app with bootstrap
This is from official Dash tutorial
"""

from dash import Dash, html, dcc, dash_table, callback, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# load data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# app layout
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                html.Div(
                    "Dash App with Bootstrap", className="text-primary text-center fs-3"
                )
            ]
        ),
        dbc.Row(
            [
                dcc.RadioItems(
                    options=[
                        {"label": x, "value": x}
                        for x in ["pop", "lifeExp", "gdpPercap"]
                    ],
                    value="pop",
                    inline=True,
                    id="radio-buttons-final",
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dash_table.DataTable(
                            data=df.to_dict("records"),
                            page_size=6,
                            style_table={"overflowX": "auto"},
                        )
                    ],
                    width=6,
                    style={"outline": "1px solid #ccc"},
                ),
                dbc.Col(
                    [
                        dcc.Graph(
                            figure={},
                            id="my-first-graph-final",
                            config={"displayModeBar": False},
                        )
                    ],
                    width=6,
                    style={"outline": "1px solid #ccc"},
                ),
            ],
        ),
    ],
    fluid=True,
)


@callback(
    Output(component_id="my-first-graph-final", component_property="figure"),
    Input(component_id="radio-buttons-final", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig


if __name__ == "__main__":
    app.run(debug=True)
