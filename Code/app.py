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

# get data
df = pd.read_csv("INF8808_Projet/Data/projet_data_3.csv", delimiter=';')
all_teams = pd.concat([df['Team1'], df['Team2']])

# get unique teams
unique_teams = all_teams.unique()



# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Caractérisation des équipes de la Coupe d'Afrique de Nations (CAN)", style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='team-selector',
        options=[{'label': country, 'value': country} for country in unique_teams],
        value=unique_teams[0],
        style={'width': '50%', 'margin': '20px auto', 'textAlign': 'center'}
    ),
    html.Div(id='visu-container')
])

# Define callback to update the graphs based on the selected value
@app.callback(
    Output('visu-container', 'children'),
    [Input('team-selector', 'value')]
)
def update_graphs(selected_value):
    graphs = [html.Div(visu.get_section(data=df, team=selected_value), className=f'part_{i+1}') 
              for i, visu in enumerate([visu1,visu2,visu3,visu4])]
    return graphs