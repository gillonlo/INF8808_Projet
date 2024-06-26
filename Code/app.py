from Code.app_init import app

import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.express as px

server = app.server

# On définit les images des drapeaux et les descriptions des visualisations
images = {
    "Algérie": "https://ipdata.co/flags/dz.png",
    "Angola": "https://ipdata.co/flags/ao.png",
    "Burkina Faso": "https://ipdata.co/flags/bf.png",
    "Cameroun": "https://ipdata.co/flags/cm.png",
    "Cap Vert": "https://ipdata.co/flags/cv.png",
    "RD Congo": "https://ipdata.co/flags/cd.png",
    "Côte d'Ivoire": "https://ipdata.co/flags/ci.png",
    "Égypte": "https://ipdata.co/flags/eg.png",
    "Guinée Equ.": "https://ipdata.co/flags/gq.png",
    "Gambie": "https://ipdata.co/flags/gm.png",
    "Ghana": "https://ipdata.co/flags/gh.png",
    "Guinée": "https://ipdata.co/flags/gn.png",
    "Guinée-Bissau": "https://ipdata.co/flags/gw.png",
    "Mali": "https://ipdata.co/flags/ml.png",
    "Mauritanie": "https://ipdata.co/flags/mr.png",
    "Maroc": "https://ipdata.co/flags/ma.png",
    "Mozambique": "https://ipdata.co/flags/mz.png",
    "Namibie": "https://ipdata.co/flags/na.png",
    "Nigéria": "https://ipdata.co/flags/ng.png",
    "Sénégal": "https://ipdata.co/flags/sn.png",
    "Afrique du Sud": "https://ipdata.co/flags/za.png",
    "Tanzanie": "https://ipdata.co/flags/tz.png",
    "Tunisie": "https://ipdata.co/flags/tn.png",
    "Zambie": "https://ipdata.co/flags/zm.png",
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
    "Voici la répartition des joueurs de chaque équipe par âge, score global et fatigue (temps de jeu par match). \
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
        Les pays ayant participé à la CAN sont en gris foncés, ceux n'ayant pas participé sont en gris clair. \
        On remarque certains territoires en gris clair bleuté, qui sont des territoires en conflit ou non reconnus. \
        Les espaces blancs dans les terres sont des points d'eau. \
        Survolez un pays pour voir à quelle région il appartient. \
        Sur le graphique en barres, vous pouvez voir la moyenne de buts marqués, passes décisives et possessions par région d'Afrique. \
        Vous pouvez choisir entre les critères d'attaque et de défense. \
        Vous pouvez sélectionner et désélectionner des types d'action en cliquant sur les éléments de la légende. \
        La région encadrée en rouge correspond à la région de votre pays sélectionné.",
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

import Code.methodologie as meth

# Prétraitement des données
df_1 = pd.read_csv("Data/projet_data_1.csv", delimiter=";")
df_2 = pd.read_csv("Data/projet_data_2.csv", delimiter=",")
df_3 = pd.read_csv("Data/projet_data_3.csv", delimiter=";")
df_4 = pd.read_csv("Data/projet_data_4.csv", delimiter=";")

data_init = init_pretraitement.get_data(
    data_teams_attack=df_1,
    data_players=df_2,
    data_tournament=df_3,
    data_teams_defense=df_4,
)
data_1 = visu1_pretraitement.get_data(
    data_teams_attack=df_1,
    data_players=df_2,
    data_tournament=df_3,
    data_teams_defense=df_4,
)
data_2 = visu2_pretraitement.get_data(
    data_teams_attack=df_1,
    data_players=df_2,
    data_tournament=df_3,
    data_teams_defense=df_4,
)
data_3 = visu3_pretraitement.get_data(
    data_teams_attack=df_1,
    data_players=df_2,
    data_tournament=df_3,
    data_teams_defense=df_4,
)
data_4 = visu4_pretraitement.get_data(
    data_teams_attack=df_1,
    data_players=df_2,
    data_tournament=df_3,
    data_teams_defense=df_4,
)

all_data = [data_1, data_2, data_3, data_4]


# Définition des layouts et des callbacks des pages
layout_home = html.Div(
    [
        html.H1(
            "Caractérisation des équipes de la Coupe d'Afrique des Nations (CAN)",
            style={"textAlign": "center", "font-size": "40px", "font-family": "verdana", "margin-top": "100px"},
        ),
        html.P(
            "Sélectionnez une équipe pour voir ses caractéristiques:",
            style={"textAlign": "center", "font-size": "20px"},
        ),
        dcc.Dropdown(
            id="team-selector",
            options=[
                {
                    "label": html.Div(
                        [
                            html.Img(
                                src=images[country],
                                style={
                                    "width": "20px",
                                    "height": "10px",
                                    "padding-right": "5px",
                                },
                            ),
                            country,
                        ]
                    ),
                    "value": country,
                }
                for country in data_init
            ],
            value="Côte d'Ivoire", # On prend le vainqueur de la CAN par défaut
            style={"width": "50%", "margin": "20px auto", "textAlign": "center"},
        ),
        html.Div(id="visu-container"),
        html.Div(
            dcc.Link("Précision sur notre démarche", href="/methodologie"),
            style={"padding": "10px", "textAlign": "center", "font-size": "20px", "margin-top": "80px"},
        ),
        html.Div(
            html.A(
                "Nos données",
                href="https://github.com/gillonlo/INF8808_Projet/tree/main/Data",
            ),
            style={"padding": "10px", "textAlign": "center", "font-size": "20px", "margin-bottom": "100px"},
        ),
    ]
)

layout_methodologie = meth.get_page()

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Callback pour afficher la page correspondante à l'URL
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return layout_home
    elif pathname == "/methodologie":
        return layout_methodologie
    else:
        return "404 Page Not Found"


# Définir les callbacks pour les visualisations
@app.callback(Output("visu-container", "children"), [Input("team-selector", "value")])
def update_graphs(selected_value):
    graphs = [
        html.Div(
            [
                html.P(
                    descriptions[i],
                    style={"textAlign": "justify", 
                            "margin-top": "80px",
                            "margin-right": "15%",
                            "margin-bottom": "60px",
                            "margin-left": "15%",
                            "font-size": "20px"
                            },
                ),
                html.Div(
                    visu.get_section(data=all_data[i], team=selected_value),
                    className=f"part_{i+1}",
                    style={"margin-bottom": "60px"},
                ),
                html.Hr(
                    style={"width": "60%", "background": "rgba(153, 153, 153, 255)"}
                ),
            ],
        )
        for i, visu in enumerate([visu1, visu2, visu3, visu4])
    ]
    return graphs

# Ici, on définit le callback utile pour la 1ere visualisation
@app.callback(Output("visu_1", "figure"), [Input("team-selector", "value")])
def update_graphs(selected_value):
    return visu1.get_figure(data=data_1, team=selected_value)
