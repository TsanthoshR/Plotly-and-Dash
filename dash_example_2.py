import dash
from dash import html
from dash import dcc
from dash.dependencies import Input,Output
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('./downloads/world_happiness.csv')

Regions = [{'label':i, 'value':i} for i in happiness['region'].unique()]
Country = [{'label':i, 'value':i} for i in happiness['country'].unique()]
# line_fig = px.line()
app = dash.Dash()

# app.layout = html.Div("My Dashboard 1")
app.layout = html.Div([
    html.H1('World Happiness Dashboard'),
    html.P(['World Happiness Report Data Sourse',
            html.Br(),
            html.A('World Happiness Report Data Sourse',
                href="https://worldhappiness.report",
                target="_blank")

            ]),
    dcc.RadioItems(options=Regions,
                   value = 'North America'),
    dcc.Checklist(options=Regions,
                  value=['North America']),
    dcc.Dropdown(id="Country_dropdown",
                 options=Country, 
                 value ='United States'),

    dcc.RadioItems(id="Graph_select",
                   options=[
                       {'label':'Happiness Score','value':'happiness_score'}, 
                       {'label':'Happiness Rank','value':'happiness_rank'}, 
                             ],
                   value="happiness_score"),
                
    dcc.Graph(id = "Happiness_Graph" ),
    html.Div(id="avg_index")

])

@app.callback(
    Output("Happiness_Graph",'figure'),
    Output("avg_index","children"),
    
    Input(component_id="Country_dropdown",component_property='value'),
    Input("Graph_select",'value'),
)
def updateGraph(selected_country,selected_graph):

    df_filtered = happiness[happiness['country']==selected_country]
    line_fig =px.line(df_filtered,
                      x='year',
                      y=selected_graph,
                      title=f'{selected_graph} in {selected_country}')
    avg_val = df_filtered[selected_graph].mean()  
    return line_fig, f"the average value of {selected_graph} for {selected_country} is {avg_val}"


if __name__ == "__main__":
    app.run_server(debug=True)

