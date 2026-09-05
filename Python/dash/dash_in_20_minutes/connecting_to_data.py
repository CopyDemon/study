import os
from dash import Dash, html, dash_table
import pandas as pd

# Incorporate data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children="My First App with Data"),
    dash_table.DataTable(data=df.to_dict("records"), page_size=20),
]

# extra practice
# this practice is to use ePB data dictionary as reference to create a new table and use xlsx file as data source
epb_data_dictionary = pd.read_excel(
    os.path.join(os.path.dirname(__file__), "epb_data_dictionary.xlsx")
)


# append extra practice title to the app layout
app.layout.append(html.H1(children="Extra Practice"))

# append data epb data dictionary table to the app layout
app.layout.append(
    dash_table.DataTable(
        data=epb_data_dictionary.to_dict("records"),
        page_size=20,
    )
)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
