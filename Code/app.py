from app_init import app

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
        style={'width': '50%', 'margin': '20px auto', 'textAlign': 'center'}
    ),
    
    html.Div(id='graphs-container')
])


# Define callback to update the graphs based on the selected value
@app.callback(
    Output('graphs-container', 'children'),
    [Input('selector', 'value')]
)
def update_graphs(selected_value):
    return [html.Div(visu1.get_section(data=df, team=selected_value), 
                     className='part_1'), 
            html.Div(visu2.get_section(data=df, team=selected_value), 
                     className='part_2'), 
            html.Div(visu3.get_section(data=df, team=selected_value), 
                     className='part_3'), 
            html.Div(visu4.get_section(data=df, team=selected_value), 
                     className='part_4')
            ]
