"""
Dash Mantine Components
This is learning from official tutorial, dash in 20 minutes.

Dash Mantine is a community-maintained library built off of the Mantine component system. Although it is not officially maintained or supported by the Plotly team, Dash Mantine is another powerful way of customizing app layouts. The Dash Mantine Components uses the Grid module to structure the layout. Instead of defining a row, we define a dmc.Grid, within which we insert dmc.Cols and define their width by assigning a number to the span property.

For the app below to run successfully, make sure to install the Dash Mantine Components library: pip install dash-mantine-components==0.12.1
"""

from dash import Dash, dcc, dash_table, callback, Input, Output
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc

# load data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

# initialize the app
app = Dash()

# app layout
app.layout = dmc.Container(
    [
        dmc.Title("Dash App with Mantine Components", size="h3"),
        dmc.RadioGroup(
            id="my-dmc-radio-item",
            size="sm",
            children=[dmc.Radio(i, value=i) for i in ["pop", "lifeExp", "gdpPercap"]],
            value="lifeExp",
        ),
        dmc.Grid(
            [
                dmc.Col(
                    [
                        dash_table.DataTable(
                            data=df.to_dict("records"),
                            page_size=12,
                            style_table={"overflowX": "auto"},
                        )
                    ],
                    span=6,
                ),
                dmc.Col([dcc.Graph(figure={}, id="graph-placeholder")], span=6),
            ],
            gutter=10,
        ),
    ]
)


@callback(
    Output(component_id="graph-placeholder", component_property="figure"),
    Input(component_id="my-dmc-radio-item", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig


if __name__ == "__main__":
    app.run(debug=True)
