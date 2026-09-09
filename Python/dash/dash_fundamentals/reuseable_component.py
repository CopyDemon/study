"""
This is from dash official documentation the fundamentals / layout / reuseable component

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

in this practice:
1. understand the how to create the component
1. understand the how to reuse the component
"""

from dash import Dash, html
import pandas as pd

# initialize the app
app = Dash()

# load data
df = pd.read_csv(
    "https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv"
)


# create the reusable component
def generate_table(dataframe, max_rows=1000):
    """
    Generate a table from the dataframe
    Args:
        dataframe (pd.DataFrame): The dataframe to generate the table from
        max_rows (int): The maximum number of rows to display in the table
    Returns:
        html.Table: The table component
    """
    return html.Table(
        children=[
            html.Thead(html.Tr(children=[html.Th(col) for col in dataframe.columns])),
            html.Tbody(
                children=[
                    html.Tr(
                        children=[
                            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                        ]
                    )
                    for i in range(min(len(dataframe), max_rows))
                ]
            ),
        ]
    )


# initialize ap
app = Dash()
app.layout = html.Div(
    children=[html.H4(children="US Agriculture Exports (2011)"), generate_table(df)]
)


# run app
if __name__ == "__main__":
    app.run(debug=True)
