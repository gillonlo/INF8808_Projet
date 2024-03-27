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

import init_pretraitement
import visu1_pretraitement
import visu2_pretraitement
import visu3_pretraitement
import visu4_pretraitement

# Prétraitement
df_1 = pd.read_csv("Data/projet_data_1.csv", delimiter=';')
df_2 = pd.read_csv("Data/projet_data_2.csv", delimiter=',')
df_3 = pd.read_csv("Data/projet_data_3.csv", delimiter=';')
df_4 = pd.read_csv("Data/projet_data_4.csv", delimiter=';')

data_init = init_pretraitement.get_data(data_teams_attack=df_1,
                                        data_players=df_2,
                                        data_tournament=df_3,
                                        data_teams_defense=df_4) 
data_1 = visu1_pretraitement.get_data(data_teams_attack=df_1,
                                        data_players=df_2,
                                        data_tournament=df_3,
                                        data_teams_defense=df_4) 
data_2 = visu2_pretraitement.get_data(data_teams_attack=df_1,
                                        data_players=df_2,
                                        data_tournament=df_3,
                                        data_teams_defense=df_4) 
data_3 = visu3_pretraitement.get_data(data_teams_attack=df_1,
                                        data_players=df_2,
                                        data_tournament=df_3,
                                        data_teams_defense=df_4) 
data_4 = visu4_pretraitement.get_data(data_teams_attack=df_1,
                                        data_players=df_2,
                                        data_tournament=df_3,
                                        data_teams_defense=df_4) 

all_data = [data_1, data_2, data_3, data_4]


# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Caractérisation des équipes de la Coupe d'Afrique de Nations (CAN)", style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='team-selector',
        options=[{'label': country, 'value': country} for country in data_init],
        value="Côte d'Ivoire",
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
    graphs = [html.Div(visu.get_section(data=all_data[i], team=selected_value), className=f'part_{i+1}') 
              for i, visu in enumerate([visu1,visu2,visu3,visu4])]
    return graphs