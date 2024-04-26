import random
from Code.app_init import app

import dash
import copy
import pandas as pd
from dash import dcc, html
import plotly.express as px
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# Transformation des phases en français pour l'affichage
to_replace = {
    0: "Poule",
    1: "8ème",
    2: "Quart",
    3: "Semi",
    3.5: "Semi",
    4: "Finale",
    5: "Gagnant",
}

overlay_template = (
    '<span style="font-size:20px">%{text}</span><br>' + "<br>"
    "<b>Position:</b> %{customdata[0]}<br>"
    "<b>Équipe:</b> %{customdata[1]}<br>"
    "<b>Score moyen:</b> %{customdata[2]:.2f} buts/assists<br>"
    "<b>Âge:</b> %{customdata[3]} ans<br>"
    "<b>Pourcentage de fatigue:</b> %{customdata[4]:.2f}%<extra></extra>"
)

# Dimension du graphique
def get_section(data: list[pd.DataFrame], team: str) -> list:
    global DATA
    DATA = copy.deepcopy(data[0])
    global ADV
    ADV = copy.deepcopy(data[1])
    global TEAM
    TEAM = copy.deepcopy(team)
    return [
        html.Div(
            [
                dcc.RadioItems(
                    id="criteria1",
                    options=[
                        {"label": "  Toutes les équipes", "value": "all-teams"},
                        {
                            "label": "  Seulement les concurrents",
                            "value": "adverse-teams",
                        },
                    ],
                    value="all-teams",
                    labelStyle={"display": "inline-block", "margin-right": "10px"},
                ),
            ],
            style={
                "border": "1px solid #ccc",
                "padding": "10px",
                "display": "inline-block",
                "margin-left": "20%",
            },
        ),
        html.Div(style={"padding": "10px"}),
        html.Div(
            [
                dcc.RadioItems(
                    id="criteria2",
                    options=[
                        {"label": "  Score", "value": "Score"},
                        {"label": "  Âge", "value": "Age"},
                        {"label": "  Fatigue", "value": "Fatigue"},
                    ],
                    value="Age",
                    labelStyle={"display": "inline-block", "margin-right": "10px"},
                ),
            ],
            style={
                "border": "1px solid #ccc",
                "padding": "10px",
                "display": "inline-block",
                "margin-left": "20%",
            },
        ),
        html.Div(id="beeswarm"),
    ]

# Callback pour le choix de l'affichage de toutes les équipes ou seulement les concurrents
@app.callback(
    Output("beeswarm", "children"),
    [Input("criteria1", "value"), Input("criteria2", "value")],
)
def update_output(selected_option_1: str, selected_option_2: str) -> list:
    # Toutes les équipes
    if selected_option_1 == "all-teams":
        return [
            dcc.Graph(
                id="visu_3",
                figure=get_figure(
                    data_list=[DATA[DATA["Round"] == i], ADV[ADV["Team1"] == TEAM]],
                    team=TEAM,
                    criteria=selected_option_2,
                    phase=i,
                ),
                style={"width": "50%", "margin": "0 auto"},
            )
            for i in sorted(list(DATA["Round"].unique()))
        ]
    # Sinon, on fait un tri pour ne garder que les équipes adverses (concurrents)
    else:
        if TEAM != "Côte d'Ivoire":
            list_teams = list(ADV[ADV["Team1"] == TEAM]["Team2"].unique())
            list_teams.insert(-1, TEAM)
        else:
            list_teams = list(ADV[ADV["Team1"] == TEAM]["Team2"].unique()) + [TEAM]
        return [
            dcc.Graph(
                id="visu_3",
                figure=get_figure_2(
                    data_list=[DATA[DATA["Squad"] == i], ADV[ADV["Team1"] == TEAM]],
                    team=i,
                    criteria=selected_option_2,
                    phase=i,
                ),
                style={"width": "50%", "margin": "0 auto"},
            )
            for i in list_teams
        ]

# Définition du graphique
def get_figure(
    data_list: list[pd.DataFrame], team: str, criteria: str, phase: float
) -> dict:
    data = data_list[0]
    scale = {"Score": [-0.5, 6.5], "Age": [15, 40], "Fatigue": [0, 102]}

    fig = go.Figure()

    # Ajout d'un strip plot pour chaque équipe (scatter plot avec une seule dimension)
    trigger = None
    for x in list(data["Squad"].unique()):
        if x != team:
            fig.add_trace(
                go.Scatter(
                    x=data[data["Squad"] == x][criteria],
                    y=[
                        random.random() * 20
                        for i in range(len(data[data["Squad"] == x][criteria]))
                    ],
                    mode="markers",
                    marker=dict(
                        color="rgba(153,153,153,255)",
                        size=10,
                        line=dict(color="rgba(10, 10, 10, 1.0)", width=1),
                    ),
                    hoverinfo="text",
                    hoverlabel = dict(font = dict(color = 'white')),
                    hovertemplate=overlay_template,
                    text=data[data["Squad"] == x]["Player"],
                    customdata=data[data["Squad"] == x][
                        ["Pos", "Squad", "Score", "Age", "Fatigue"]
                    ],
                )
            )
        else:
            trigger = 1

    if trigger is not None:
        fig.add_trace(
            go.Scatter(
                x=data[data["Squad"] == team][criteria],
                y=[
                    random.random() * 20
                    for i in range(len(data[data["Squad"] == team][criteria]))
                ],
                mode="markers",
                marker=dict(
                    color="rgba(255, 0, 0, 0.7)",
                    size=10,
                    line=dict(color="rgb(200, 0, 0, 255)", width=1),
                ),
                hoverinfo="text",
                hoverlabel = dict(font = dict(color = 'white')),
                hovertemplate=overlay_template,
                text=data[data["Squad"] == team]["Player"],
                customdata=data[data["Squad"] == team][
                    ["Pos", "Squad", "Score", "Age", "Fatigue"]
                ],
            )
        )
    # Mise en forme du graphique
    fig.update_layout(
        title=to_replace[phase],
        height=200,
        plot_bgcolor="rgba(0, 0, 0, 0)",
        yaxis=dict(showticklabels=False),
        margin=dict(l=10, r=10, t=50, b=5),
    )

    fig.update_layout(showlegend=False)

    fig.update_xaxes(range=scale[criteria])

    return fig


def get_figure_2(
    data_list: list[pd.DataFrame], team: str, criteria: str, phase: float
) -> dict:
    data = data_list[0]
    adv = data_list[1]

    scale = {"Score": [-0.5, 6.5], "Age": [15, 40], "Fatigue": [0, 101]}

    fig = go.Figure()

    # Ajout du premier strip plot pour l'équipe sélectionnée
    if team != TEAM:
        fig.add_trace(
            go.Scatter(
                x=data[data["Squad"] == team][criteria],
                y=[
                    random.random() * 20
                    for i in range(len(data[data["Squad"] == team][criteria]))
                ],
                mode="markers",
                marker=dict(
                    color="rgba(153,153,153,255)",
                    size=10,
                    line=dict(color="rgba(10, 10, 10, 1.0)", width=1),
                ),
                hoverlabel = dict(font = dict(color = "white")),
                hoverinfo="text",
                hovertemplate=overlay_template,
                text=data[data["Squad"] == team]["Player"],
                customdata=data[data["Squad"] == team][
                    ["Pos", "Squad", "Score", "Age", "Fatigue"]
                ],
            )
        )

        fig.update_layout(
            title=str(to_replace[list(adv[adv["Team2"] == team]["Round"])[0]])
            + " : "
            + team,
            height=200,
            plot_bgcolor="rgba(0, 0, 0, 0)",
            yaxis=dict(showticklabels=False),
            margin=dict(l=10, r=10, t=50, b=5),
        )
    else:
        fig.add_trace(
            go.Scatter(
                x=data[data["Squad"] == team][criteria],
                y=[
                    random.random() * 20
                    for i in range(len(data[data["Squad"] == team][criteria]))
                ],
                mode="markers",
                marker=dict(
                    color="rgba(255, 0, 0, 0.7)",
                    size=10,
                    line=dict(color="rgb(200, 0, 0, 255)", width=1),
                ),
                hoverlabel = dict(font = dict(color = "white")),
                hoverinfo="text",
                hovertemplate=overlay_template,
                text=data[data["Squad"] == team]["Player"],
                customdata=data[data["Squad"] == team][
                    ["Pos", "Squad", "Score", "Age", "Fatigue"]
                ],
            )
        )

        fig.update_layout(
            title=str(to_replace[list(adv[adv["Team1"] == team]["Round"])[-1]])
            + " : "
            + team,
            height=200,
            plot_bgcolor="rgba(0, 0, 0, 0)",
            yaxis=dict(showticklabels=False),
            margin=dict(l=10, r=10, t=50, b=5),
        )

    fig.update_layout(showlegend=False)

    fig.update_xaxes(range=scale[criteria])

    return fig
