"""
This is from dash official documentation the fundamentals / layout

in this practice:
1. understand the html layout
2. understand what is dcc and create a dcc graph as an example
3. understand the how to use inline style in the app
"""

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# initialize the app
app = Dash()

# initialize data
df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)

# initialize figure
fig = px.bar(df, x="City", y="Amount", color="Fruit", barmode="group")

# define fig style
colors = {"background": "#111111", "text": "#7FDBFF"}
fig.update_layout(
    plot_bgcolor=colors["background"],
    paper_bgcolor=colors["background"],
    font_color=colors["text"],
)

# app layout
app.layout = html.Div(
    children=[
        html.H1("Dash tutorial fundamentals layout"),
        html.P(children="Dash: A web application framework for your data."),
        # dcc is dash core components
        dcc.Graph(id="example-graph", figure=fig),
    ],
    style={"textAlign": "center", "color": colors["text"]},
)


# run the app
if __name__ == "__main__":
    app.run(debug=True)
