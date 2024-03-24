import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

import visu1
import visu2
import visu3
import visu4

# Sample data
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [20, 14, 23, 25, 18]
})

# Initialize the Dash app
app = dash.Dash(__name__)

# Define options for the dropdown selector
options = [
    {'label': 'Nigeria', 'value': 'Nigeria'},
    {'label': 'Namibie', 'value': 'Namibie'},
    {'label': 'Côte d\'Ivoire', 'value': 'Côte d\'Ivoire'}
]

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
    return html.Div([
        dcc.Graph(
            id='visu_1',
            figure=visu1.get_figure(data=df, team=selected_value),
            style={'width': '70%', 'margin': '0 auto'}
        )
    ], className='part_1'), html.Div([
        dcc.Graph(
            id='visu_2',
            figure=visu2.get_figure(data=df),
            style={'width': '70%', 'margin': '0 auto'}
        )
    ], className='part_2'), html.Div([
        dcc.Graph(
            id='visu_3',
            figure=visu3.get_figure(data=df),
            style={'width': '70%', 'margin': '0 auto'}
        )
    ], className='part_3'), html.Div([
        dcc.Graph(
            id='visu_4',
            figure=visu4.get_figure(data=df),
            style={'width': '70%', 'margin': '0 auto'}
        )
    ], className='part_4')
