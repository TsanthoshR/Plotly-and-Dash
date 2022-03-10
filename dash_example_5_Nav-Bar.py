import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

navbar = dbc.NavbarSimple(
    brand ='Soccer Players Dashboard',
    children = [
        html.Img(src='https://uptime.com/media/website_profiles/sofifa.com.png',
                height=20),
        html.A('Data Source',
                href="https://sofifa.com",
                target="_blank",
                style={'color':'black'}
                )
    ],
    color='primary',
    fluid=True,
)

app = dash.Dash(
                __name__,
                external_stylesheets = [dbc.themes.BOOTSTRAP]
                )

app.layout = html.Div([
    navbar
])




if __name__ == "__main__":
    app.run_server( port = 8051,
                    debug=True,
                    threaded = True
                    )
