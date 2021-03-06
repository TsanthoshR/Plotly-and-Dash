import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

happiness = pd.read_csv("./downloads/world_happiness.csv")

Regions = [{"label": i, "value": i} for i in happiness["region"].unique()]
Country = [{"label": i, "value": i} for i in happiness["country"].unique()]
# line_fig = px.line()
app = dash.Dash()

# app.layout = html.Div("My Dashboard 1")
app.layout = html.Div(
    [
        html.H1("World Happiness Dashboard"),
        html.P(
            [
                "World Happiness Report Data Sourse",
                html.Br(),
                html.A(
                    "World Happiness Report Data Sourse",
                    href="https://worldhappiness.report",
                    target="_blank",
                ),
            ]
        ),
        dcc.RadioItems(options=Regions, value="North America"),
        dcc.Checklist(options=Regions, value=["North America"]),
        dcc.Dropdown(id="Country_dropdown", options=Country, value="United States"),
        dcc.Graph(id="Happiness_Graph"),
    ]
)


@app.callback(
    Output("Happiness_Graph", "figure"),
    Input(component_id="Country_dropdown", component_property="value"),
)
def updateGraph(selected_country):

    df_filtered = happiness[happiness["country"] == selected_country]
    line_fig = px.line(
        df_filtered,
        x="year",
        y="happiness_score",
        title=f"Happiness Score in {selected_country}",
    )

    return line_fig


if __name__ == "__main__":
    app.run_server(debug=True)
