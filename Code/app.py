from Code.app_init import app

import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.express as px

server = app.server

images = {
    'Algeria': 'https://ipdata.co/flags/dz.png',
    'Angola': 'https://ipdata.co/flags/ao.png',
    'Burkina Faso': 'https://ipdata.co/flags/bf.png',
    'Cameroon': 'https://ipdata.co/flags/cm.png',
    'Cape Verde': 'https://ipdata.co/flags/cv.png',
    'Congo DR': 'https://ipdata.co/flags/cd.png',
    "Côte d'Ivoire": 'https://ipdata.co/flags/ci.png',
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

descriptions = [
    "Voici l'arbre des matchs de la CAN 2023 à partir des 8e de finale. Votre équipe sélectionnée s'affiche en rouge. \
        Survolez un pays en particulier pour voir le détail de ses matchs et son avancée dans la compétition. \
        Le détail pour la 3e place est visible en survolant les équipes de la demi-finale.",
    "Voici le score moyen des équipes en terme de buts, buts sans pénalty, passes décisives et possession ramenés sur 90 minutes. \
        Vous pouvez choisir entre les critères d'attaque et de défense. \
        Les équipes sont classées par ordre décroissant de score. \
        On affiche les 8 meilleures et votre équipe sélectionnée ou bien les 9 meilleures si votre équipe en fait partie. \
        Survolez une équipe pour voir son score détaillé.",
    "Voici la répartition des joueurs de chaque équipe par âge, score moyen et pourcentage de fatigue. \
        Vous pouvez choisir entre les critères de score, d'âge et de fatigue. \
        Le score d'un joueur correspond à la somme des buts marqués, buts hors pénalty et passes décisives, ramenée sur 90 minutes. \
        L'âge d'un joueur correspond à son âge au moment de la coupe d'Afrique des Nations. \
        La fatigue d'un joueur correspond au temps total passé sur le terrain ramené sur 90 minutes. \
            Ainsi, un joueur ayant 80% en fatigue aura passé 80% de son temps de jeu sur le terrain. \
        Les joueurs sont répartis par avancée de leur équipe dans la compétition. \
        Survolez un point pour voir le détail du joueur.",     
    "Voici la répartition des équipes par région d'Afrique. \
        Il y a 5 régions : Nord, Est, Ouest, Centrale et Australe. \
        Sur la carte, la région en rouge correspond à la région de votre pays sélectionné. \
        Survolez un pays pour voir à quelle région il appartient. \
        Sur le graphique en barres, vous pouvez voir le total de buts marqués, passes décisives et possessions par région d'Afrique. \
        Vous pouvez choisir entre les critères d'attaque et de défense. \
        Vous pouvez sélectionner et désélectionner des types d'action en cliquant sur les éléments de la légende. \
        La région encadrée en rouge correspond à la région de votre pays sélectionné."
    ]

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
    html.H1("Caractérisation des équipes de la Coupe d'Afrique des Nations (CAN)", style={'textAlign': 'center'}),
    html.P("Sélectionnez une équipe pour voir ses caractéristiques:", style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='team-selector',
        options=[{'label': html.Div([html.Img(src=images[country], style={'width': '20px', 'height': '10px', 'padding-right' :'5px'}), country]), 'value': country} for country in data_init],
        #options=[{'label': country, 'value': country} for country in data_init],
        value="Côte d'Ivoire",
        style={'width': '50%', 'margin': '20px auto', 'textAlign': 'center'}
    ),
    html.Div(id='visu-container'),
])


# Define callback to update the graphs based on the selected value
@app.callback(
    Output('visu-container', 'children'),
    [Input('team-selector', 'value')]
)
def update_graphs(selected_value):
    graphs = [
        html.Div([
            html.P(descriptions[i], style={'textAlign': 'center', 'margin': '40px 120px 10px'}),
            html.Div(visu.get_section(data=all_data[i], team=selected_value), className=f'part_{i+1}')
        ]) for i, visu in enumerate([visu1, visu2, visu3, visu4])
    ]
    return graphs

@app.callback(
    Output('visu_1', 'figure'),
    [Input('team-selector', 'value')]
)
def update_graphs(selected_value):
    return visu1.get_figure(data=data_1, team=selected_value)

