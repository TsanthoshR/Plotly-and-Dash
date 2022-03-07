import dash
from dash import html, dcc
from dash.dependencies import Input,Output


app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='Input_text', 
        value="Enter your text",
        type='text',
        ),
    html.Div(children = '',
             id='Output_text')

])

@app.callback(
    Output(component_id="Output_text",component_property='children'),
    Input(component_id="Input_text",component_property='value')
)
def update_op_div(Input_text):
    return f"Text : {Input_text}"

if __name__ == "__main__":
    app.run_server(debug=True)