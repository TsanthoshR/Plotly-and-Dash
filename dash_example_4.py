import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

soccer = pd.read_csv("./downloads/fifa_soccer_players.csv")

player_names = [{'label' : i , 'value' : i } for i in soccer['long_name'].unique()]

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Location(id = 'url',pathname="/test"),
    html.H1('Soccer Players Dashboard',
            style={
                    'textAlign' : 'Centre',
                    'fontFamily' : 'fantasy',
                    'fontSize' : 'blue'
            }),
    html.P(['Source: ',
            html.A('Sofifa',
                    href = 'https://sofifa.con/',
                    target = '_blank')],
                    style= {'border':'solid'} ),
    html.Label('Player name : '),
    dcc.Dropdown(options = player_names,
                 value = player_names[0]['value'],
                 style={'backgroundColor':'lightblue'})
],
style={'padding':100, 'border':'solid'})


if __name__ == "__main__":
    app.run_server( port = 8051,
                    debug=True,
                    threaded = True
                    )
