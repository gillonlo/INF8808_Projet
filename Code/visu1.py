import dash
import math
import numpy as np
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.express as px

df_3 = pd.read_csv("Data/projet_data_3.csv", delimiter=";")

# Dimension du graphique
def get_section(data: pd.DataFrame, team: str) -> list:
    return [
        dcc.Graph(
            id="visu_1",
            figure=get_figure(data=data, team=team),
            style={"width": "80%", "margin": "0 auto"},
        )
    ]

# Fonction pour séparer le nom de l'équipe (utile lors de l'affichage du parcours de l'équipe / hoverlay)
def split_team_name(name: str) -> str:
    words = name.split()
    if len(words) > 2:
        return words[0] + " " + "<br>".join(words[1:])
    else:
        return name

# Définition du graphique
def get_figure(data: pd.DataFrame, team: str) -> dict:
    fig = go.Figure()

    color_scale = ["#999999"]
    name_of_round = ["8ème", "Quart", "Semi", "Finale", "Gagnant"]

    rounds = np.delete(df_3["Round"].unique(), 3)
    rounds = np.insert(rounds, 4, "Gagnant")

    for i in range(len(data)):
        round = math.floor(data.at[i, "Round"])
        name = data.at[i, "Team"]
        team_name_with_linebreak = split_team_name(name)

        # Le code suivant (assez bordélique) permet de récupérer les matchs joués par l'équipe 
        # C'est utile pour afficher le parcours de l'équipe lors du hover
        match_df = df_3[
            df_3["Team1"].str.contains(name) | df_3["Team2"].str.contains(name)
        ]
        idx = 0
        list_match = []
        for _, item in match_df.iterrows():
            list_match.append(
                str(name_of_round[idx])
                + " : "
                + item["Team1"]
                + " vs "
                + item["Team2"]
                + "  "
                + item["Score"]
            )
            list_match.append("Nombre de spectateurs : " + item["Attendance"])
            list_match.append("")
            idx += 1
        if i == 15:
            list_match.append("Gagnant de la CAN")
        elif i == 14:
            list_match.append("2e de la CAN")
        elif i == 13:
            list_match.append("3e de la CAN")
        elif i == 12:
            list_match.append("4e de la CAN")

        # Utilisation d'un graphe de type "Funnel" pour l'arbre d'élimination du tournoi
        fig.add_trace(
            go.Funnel(
                name=name,
                orientation="h",
                y=name_of_round[:round],
                x=round * [200],
                text=round * [team_name_with_linebreak],
                textinfo="text",
                marker=dict(color=color_scale[0]),
                hovertemplate="<b>%{text}</b>"
                + "<extra></extra>"
                + "<br>"
                + "<br>"
                + "Parcours complet :"
                + "<br>"
                + "<br>".join(list_match),
            )
        )

        fig.add_trace(
            go.Funnel(
                y=name_of_round[:round],
                x=round * [5],
                text=round * [""],
                textinfo="text",
                opacity=0,
                hoverinfo="skip",
            )
        )

    # Mettre en rouge l'équipe sélectionnée (et son parcours)
    for trace in fig.data:
        if trace.name == team:
            trace.marker.color = "red"

    # Mise en forme du graphique (titre, couleur de fond, légende)
    fig.update_layout(
        title={
            "text": "Tournois",
            "x": 0.5,
            "y": 0.95,
            "xanchor": "center",
            "yanchor": "top",
        },
        plot_bgcolor="white",
        showlegend=False,
    )

    return fig
