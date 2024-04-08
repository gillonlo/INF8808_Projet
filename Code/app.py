from Code.app_init import app

import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.express as px

images = {
    'Algeria': 'https://ipdata.co/flags/dz.png',
    'Angola': 'https://ipdata.co/flags/ao.png',
    'Burkina Faso': 'https://ipdata.co/flags/bf.png',
    'Cameroon': 'https://ipdata.co/flags/cm.png',
    'Cape Verde': 'https://ipdata.co/flags/cv.png',
    'Congo DR': 'https://ipdata.co/flags/cd.png',
    'Côte dIvoire': 'https://ipdata.co/flags/ci.png',
    'Egypt': 'https://ipdata.co/flags/eg.png',
    'Equ. Guinea': 'https://ipdata.co/flags/gq.png',
    'Gambia': 'https://ipdata.co/flags/gm.png',
    'Ghana': 'https://ipdata.co/flags/gh.png',
    'Guinea': 'https://ipdata.co/flags/gn.png',
    'Guinea-Bissau': 'https://ipdata.co/flags/gw.png',
    'Mali': 'https://ipdata.co/flags/ml.png',
    'Mauritania': 'https://ipdata.co/flags/mr.png',
    'Morocco': 'https://ipdata.co/flags/ma.png',
    'Mozambique': 'https://ipdata.co/flags/mz.png',
    'Namibia': 'https://ipdata.co/flags/na.png',
    'Nigeria': 'https://ipdata.co/flags/ng.png',
    'Senegal': 'https://ipdata.co/flags/sn.png',
    'South Africa': 'https://ipdata.co/flags/za.png',
    'Tanzania': 'https://ipdata.co/flags/tz.png',
    'Tunisia': 'https://ipdata.co/flags/tn.png',
    'Zambia': 'https://ipdata.co/flags/zm.png',
}

import Code.visu1 as visu1
import Code.visu2 as visu2
import Code.visu3 as visu3
import Code.visu4 as visu4

import Code.init_pretraitement as init_pretraitement
import Code.visu1_pretraitement as visu1_pretraitement
import Code.visu2_pretraitement as visu2_pretraitement
import Code.visu3_pretraitement as visu3_pretraitement
import Code.visu4_pretraitement as visu4_pretraitement

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

@app.callback(
    Output('visu_1', 'figure'),
    [Input('team-selector', 'value')]
)
def update_graphs(selected_value):
    return visu1.get_figure(data=data_1, team=selected_value)

