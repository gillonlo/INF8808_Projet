# Import necessary libraries
from dash.dependencies import Input, Output
import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go

import visu1
import visu2
import visu3
import visu4

# Initialize the Dash app
app = dash.Dash(__name__)

# Define options for the dropdown selector
options = [
    {'label': 'Option 1', 'value': 'option1'},
    {'label': 'Option 2', 'value': 'option2'},
    {'label': 'Option 3', 'value': 'option3'}
]

# Sample data
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [20, 14, 23, 25, 18]
})

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Caractérisation des équipes de la Coupe d'Afrique de Nations (CAN)", style={'textAlign': 'center'}),
    
    dcc.Dropdown(
        id='selector',
        options=options,
        value=options[0]['value'],
        style={'width': '50%', 'margin': '20px auto'}
    ),
    
    html.Div(id='graphs-container')
], style={'textAlign': 'center'})

# Define callback to update the graphs based on the selected value
@app.callback(
    Output('graphs-container', 'children'),
    [Input('selector', 'value')]
)
def update_graphs(selected_value):
    if selected_value == 'option1':
        return dcc.Graph(
            id='visu_1',
            figure=visu1.get_figure(data=df),
            style={'width': '70%', 'margin': '0 auto'}
        )
    elif selected_value == 'option2':
        return dcc.Graph(
            id='visu_2',
            figure=visu2.get_figure(data=df),
            style={'width': '70%', 'margin': '0 auto'}
        )
    elif selected_value == 'option3':
        return dcc.Graph(
            id='visu_3',
            figure=visu3.get_figure(data=df),
            style={'width': '70%', 'margin': '0 auto'}
        )

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
