from Code.app_init import app

import dash
import copy
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

# Dimension et structure du graphique
def get_section(data: pd.DataFrame, team: str) -> list:
    global DATA
    DATA = copy.deepcopy(data)
    global TEAM
    TEAM = copy.deepcopy(team)
    return [
        html.Div(
            [
                dcc.RadioItems(
                    id="criteriaPolar",
                    options=[
                        {"label": "  Attaque", "value": "Attaque"},
                        {"label": "  Défense", "value": "Défense"},
                    ],
                    value="Attaque",
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
        html.Div(id="polar-charts"),
    ]

# Mise à jour des graphiques et callback pour le choix de l'attaque ou de la défense
@app.callback(Output("polar-charts", "children"), [Input("criteriaPolar", "value")])
def update_output(selected_option: str) -> list:
    
    # On choisit donc d'afficher les données offensives ou défensives 
    # en fonction de l'option sélectionnée par le lecteur
    # On affiche les 8 meilleures équipes (en terme de remplissage du radar) et l'équipe sélectionnée
    
    # Attaque
    if selected_option == "Attaque":
        new_data = DATA.sort_values(by=["Attack_Sum"], ascending=False).reset_index(
            drop=True
        )
        index = [i for i in range(len(new_data)) if new_data.iloc[i]["Squad"] == TEAM]
        if index[0] <= 8:
            index = [8]
        categories = [
            "Possession",
            "Buts marqués",
            "Passes décisives",
            "Buts hors<br>pénalty",
        ]

    # Défense
    else:
        new_data = DATA.sort_values(by=["Defense_Sum"], ascending=False).reset_index(
            drop=True
        )
        index = [i for i in range(len(new_data)) if new_data.iloc[i]["Squad"] == TEAM]
        if index[0] <= 8:
            index = [8]
        categories = [
            "Possession moy",
            "Buts non reçus",
            "Passes adv.<br>contrées",
            "Buts hors<br>pénalty<br>non reçus",
        ]
        
    # On retourne la mise à jour des 9 graphiques 
    return [
        html.Div(
            [
                dcc.Graph(
                    id="visu_2_" + str(i),
                    figure=get_figure(
                        data=new_data.iloc[i],
                        team=TEAM,
                        criteria=selected_option,
                        categories=categories,
                        classement=i,
                    ),
                    style={
                        "width": "33%",
                        "margin": "0 auto",
                        "display": "inline-block",
                    },
                )
                for i in list(range(8)) + index
            ],
            className="row",
        )
    ]

# Définition du graphique
def get_figure(
    data: pd.DataFrame, team: str, criteria: str, categories: list[str], classement: int
) -> dict:
    squad_name = data["Squad"]

    # On switch entre les critères offensifs et défensifs
    if criteria == "Attaque":
        values = data[
            [
                "Possession", 
                "Buts marqués", 
                "Passes décisives", 
                "Buts hors pénalty"
             ]
        ].tolist()
    else:
        values = data[
            [
                "Possession moy",
                "Buts non reçus",
                "Passes adv. contrées",
                "Buts hors pénalty non reçus",
            ]
        ].tolist()

    if squad_name == team: # On met en évidence l'équipe sélectionnée (en rouge)
        color = "rgba(255, 0, 0, 0.3)"
    else: # Sinon, on met en gris le fond du radar
        color = "rgba(223, 230, 224, 0.5)"

    fig = go.Figure()

    colors = ["#1f77b4", "#2ca02c", "#ffbb00", "#ff5733"]

    # Utilisation d'un graphe de type "Barpolar" pour le radar 
    fig.add_trace(
        go.Barpolar(
            r=values,
            theta=categories,
            name=squad_name,
            hoverinfo="text",
            hovertemplate="%{theta}:<br>" "%{r:.2f}<extra></extra>",
            marker=dict(color=colors),
        )
    )

    fig.update_layout(
        title=str(classement + 1) + " : " + squad_name,
        polar=dict(
            radialaxis=dict(
                range=[0, 2.5],
                visible=True,
                tickmode="array",
                tickvals=[0, 0.5, 1, 1.5, 2, 2.5],
                ticktext=[0, 0.5, 1, 1.5, 2, 2.5],
            ),
            bgcolor=color,
        ),
        title_x=0.5,
    )

    return fig
