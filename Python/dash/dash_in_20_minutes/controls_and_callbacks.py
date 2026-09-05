from dash import Dash, html, dcc, dash_table, callback, Input, Output
import pandas as pd
import plotly.express as px

# load data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

# initialize the app
app = Dash()

# app layout
app.layout = [
    html.Div(
        children="My first app with data, graph and control",
        style={"color": "blue"},
    ),
    dash_table.DataTable(data=df.to_dict("records"), page_size=5),
    html.Hr(),
    html.P("Select a option to render graph:"),
    dcc.RadioItems(
        options=["pop", "lifeExp", "gdpPercap"],
        value="pop",  # default value
        id="controls-and-radio-item",
    ),
    html.P(children="Please select a thing to render.", id="graph-title"),
    dcc.Graph(figure={}, id="controls-and-graph"),
]


# callback update graphic base on the selected option
# from tutorial
@callback(
    Output(component_id="controls-and-graph", component_property="figure"),
    Input(component_id="controls-and-radio-item", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig


# callback update title graphic base on the selected option
# self practice
@callback(
    Output(component_id="graph-title", component_property="children"),
    Input(component_id="controls-and-radio-item", component_property="value"),
)
def update_graph_title(col_chosen_value):
    return f"The histogram of {col_chosen_value}"


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
