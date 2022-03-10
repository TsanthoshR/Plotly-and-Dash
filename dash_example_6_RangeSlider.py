import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

elec = pd.read_csv("./downloads/electricity.csv")
year_min = elec['Year'].min()
year_max = elec['Year'].max()
app = dash.Dash(
    external_stylesheets = [dbc.themes.YETI]
)

app.layout = html.Div([
    html.H1("Electricity Prices in US states"),
    dcc.RangeSlider(id="year-slider",
                    min=year_min,
                    max=year_max,
                    value=[year_min,year_max],
                    marks={i:str(i) for i in range(year_min,year_max+1)})
])


if __name__ == "__main__":
    app.run_server( port = 8051,
                    debug=True,
                    threaded = True
                    )
