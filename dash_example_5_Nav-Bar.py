import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

soccer = pd.read_csv('downloads/fifa_soccer_players.csv')

avg_age = soccer['age'].mean()
avg_height = soccer['height_cm'].mean()
avg_weight = soccer['weight_kg'].mean()

cards =dbc.CardDeck([
    dbc.Card(
        dbc.CardBody([
            html.H4('Avg. Age'),
            html.H5(f'{round(avg_age),1} years')
            
        ]),
        style = {'testAlign':'centre','color':'weight'},
        color='lightblue'
    ),
    dbc.Card(
        dbc.CardBody([
            html.H4('Avg. Height'),
            html.H5(f'{round(avg_height),1} years')
            
        ]),
        style = {'testAlign':'centre','color':'weight'},
        color='blue'
    ),
    dbc.Card(
        dbc.CardBody([
            html.H4('Avg. Weight'),
            html.H5(f'{round(avg_weight),1} years')
            
        ]),
        style = {'testAlign':'centre','color':'weight'},
        color='darkblue'
    ),
])

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
    navbar,
    html.Br(),
    cards,
])




if __name__ == "__main__":
    app.run_server( port = 8051,
                    debug=True,
                    threaded = True
                    )
