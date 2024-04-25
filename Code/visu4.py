import copy
import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output

from Code.app_init import app


def get_section(data: pd.DataFrame, team: str) -> list:
    global data_copy
    data_copy = copy.deepcopy(data)

    return [
        dcc.RadioItems(
            id="criteria",
            options=[
                {"label": "  Attaque", "value": "Attaque"},
                {"label": "  Défense", "value": "Défense"},
            ],
            value="Attaque",
            labelStyle={"display": "inline-block", "margin-right": "10px"},
            style={
                "border": "1px solid #ccc",
                "padding": "10px",
                "display": "inline-block",
                "margin-left": "20%",
            },
        ),
        html.Div(
            style={"display": "flex"},
            children=[
                dcc.Graph(
                    id="visu_4",
                    figure=get_figure(data=data[0], team=team),
                    style={"width": "30%"},  # Set the width of visu_4 to 30%
                ),
                html.Div(
                    style={"width": "70%"},
                    children=[  # Set the width of the containing div to 70%
                        dcc.Graph(
                            id="bar_plot",  # Ajout de l'identifiant pour le graphique à barres
                            style={
                                "width": "100%"
                            },  # Set the width of bar_plot to 100% to fill its container
                        )
                    ],
                ),
            ],
        ),
    ]


def get_figure(data: pd.DataFrame, team: str) -> go.Figure:

    # Définition des régions avec les pays associés
    regions = {
        "Nord": ["Maroc", "Algeria", "Tunisia", "Egypt", "Libya"],
        "Est": [
            "Sudan",
            "South Sudan",
            "Ethiopia",
            "Somalia",
            "Kenya",
            "Ouganda",
            "Rwanda",
            "Burundi",
            "Tanzania",
            "Djibouti",
            "Eritrea",
        ],
        "Ouest": [
            "Mauritania",
            "Mali",
            "Niger",
            "Nigeria",
            "Chad",
            "Senegal",
            "Gambie",
            "Guinea-Bissau",
            "Guinea",
            "Sierra Leone",
            "Liberia",
            "Côte d'Ivoire",
            "Burkina Faso",
            "Ghana",
            "Togo",
            "Benin",
        ],
        "Centrale": [
            "Cameroon",
            "Central African Republic",
            "Chad",
            "Congo DR",
            "Congo",
            "Gabon",
            "Guinea Equ.",
            "Sao Tome e Principe",
        ],
        "Australe": [
            "Angola",
            "Zambia",
            "Zimbabwe",
            "Malawi",
            "Botswana",
            "Namibia",
            "South Africa",
            "Mozambique",
            "Lesotho",
            "Swaziland",
            "Madagascar",
        ],
    }

    """
    regions = {
        "Nord": ["Maroc", "Algérie", "Tunisi", "Égypte", "Libie"],
        "Est": ["Soudan", "Soudan du Sud", "Éthiopie", "Somalie", "Kénya", "Ouganda", "Rwanda", "Burundi", "Tanzanie", "Djibouti", "Érythrée"],
        "Ouest": ["Mauritanie", "Mali", "Niger", "Nigéria", "Chad", "Sénégal", "Gambie", "Guinée-Bissau", "Guinée", "Sierra Leone", "Libéria", "Côte d'Ivoire", "Burkina Faso", "Ghana", "Togo", "Bénin"],
        "Centrale": ["Cameroun", "République centrafricaine", "Chad", "RD Congo", "Congo", "Gabon", "Guinée Equ.", "Sao Tomé et Principe"],
        "Australe": ["Angola", "Zambie", "Zimbabwe", "Malawi", "Botswana", "Namibie", "Afrique du Sud", "Lesotho", "Swaziland", "Madagascar"]
    }

    """

    # Récupération de la région du pays sélectionné
    selected_region = data[data["Squad"] == team]["Region"].iloc[0]

    # Création de la liste des traces pour chaque région
    traces = []

    # Création de la carte de l'Afrique
    fig = go.Figure()


    # Parcours de chaque région
    for region, countries in regions.items():
        # Couleur de la région
        color = "red" if region == selected_region else "rgba(153,153,153,255)"
        # Création de la trace pour la région
        trace = go.Choropleth(
            locations=countries,
            z=[1] * len(countries),
            locationmode="country names",
            colorscale=[[0, color], [1, color]],
            hoverinfo="location",
            hovertemplate="%{location}<br>Région: " + region + "<extra></extra>",
            showlegend=False,
            showscale=False,  # Ne pas afficher l'échelle
        )
        traces.append(trace)


    # Ajout des traces à la figure
    for trace in traces:
        fig.add_trace(trace)

    # Mise en forme de la carte
    fig.update_layout(
        title_text="Carte de l'Afrique par régions",
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type="equirectangular",
            bgcolor="rgba(0,0,0,0)",
            scope="africa",
        ),
    )

    return fig

# On ajoute une nouvelle fonction pour mettre à jour le graphique à barres 
# On veut pouvoir switcher entre les métriques d'attaque et de défense
@app.callback(
    Output("bar_plot", "figure"),
    [Input("criteria", "value"), Input("team-selector", "value")],
)
def update_bar_plot(valeur, equipe):
    moyennes_attaque = data_copy[2]
    moyennes_defense = data_copy[3]

    if valeur == "Attaque":
        fig = go.Figure(
            data=[
                go.Bar(
                    name="Buts marqués en moyenne<br>par 90 minutes",
                    x=moyennes_attaque.index,
                    y=moyennes_attaque["Avg_Gls90_Attack"],
                    hovertemplate="Région: %{x}<br>Buts marqués: %{y}<extra></extra>",
                    marker=dict(color="#2ca02c"),
                ),
                go.Bar(
                    name="Possession moyenne",
                    x=moyennes_attaque.index,
                    y=moyennes_attaque["Avg_Poss_Attack"],
                    hovertemplate="Région: %{x}<br>Possession: %{y}%<extra></extra>",
                    marker=dict(color="#1f77b4"),
                ),
                go.Bar(
                    name="Buts hors penalty marqués en moyenne<br>par 90 minutes",
                    x=moyennes_attaque.index,
                    y=moyennes_attaque["Avg_G-PK90_Attack"],
                    hovertemplate="Région: %{x}<br>Buts hors penalty marqués: %{y}<extra></extra>",
                    marker=dict(color="#ff5733"),
                ),
                go.Bar(
                    name="Passes décisives en moyenne<br>par 90 minutes",
                    x=moyennes_attaque.index,
                    y=moyennes_attaque["Avg_Ast90_Attack"],
                    hovertemplate="Région: %{x}<br>Passe décisive: %{y}<extra></extra>",
                    marker=dict(color="#ffbb00"),
                ),
            ]
        )
        fig.update_layout(
            barmode="group",
            title="Métriques moyennes pour l'attaque par région",
            plot_bgcolor="rgba(239,242,240,255)",
        )
    elif valeur == "Défense":

        fig = go.Figure(
            data=[
                go.Bar(
                    name="Buts concédés en moyenne<br>par 90 minutes",
                    x=moyennes_defense.index,
                    y=moyennes_defense["Avg_Gls90_Defense"],
                    hovertemplate="Région: %{x}<br>Buts concédés: %{y}<extra></extra>",
                    marker=dict(color="#2ca02c"),
                ),
                go.Bar(
                    name="Possession concédée moyenne",
                    x=moyennes_defense.index,
                    y=moyennes_defense["Avg_Poss_Defense"],
                    hovertemplate="Région: %{x}<br>Possession concédée: %{y}%<extra></extra>",
                    marker=dict(color="#1f77b4"),
                ),
                go.Bar(
                    name="Buts hors penalty concédés en moyenne<br>par 90 minutes",
                    x=moyennes_attaque.index,
                    y=moyennes_defense["Avg_G-PK90_Defense"],
                    hovertemplate="Région: %{x}<br>Buts hors penalty concédés: %{y}<extra></extra>",
                    marker=dict(color="#ff5733"),
                ),
                go.Bar(
                    name="Passes décisives concédées en moyenne<br>par 90 minutes",
                    x=moyennes_defense.index,
                    y=moyennes_defense["Avg_Ast90_Defense"],
                    hovertemplate="Région: %{x}<br>Passe décisive concédée: %{y}<extra></extra>",
                    marker=dict(color="#ffbb00"),
                ),
            ]
        )
        fig.update_layout(
            barmode="group",
            title="Métriques moyennes pour la défense par région",
            plot_bgcolor="rgba(239,242,240,255)",
        )

    # Mettre en surbrillance la région sélectionnée en rouge
    if equipe:
        region_selectionnee = data_copy[0][data_copy[0]["Squad"] == equipe][
            "Region"
        ].iloc[0]

        indice_region_selectionnee = moyennes_attaque.index.get_loc(region_selectionnee)
        fig.add_shape(
            type="rect",
            xref="x",
            yref="y",
            x0=indice_region_selectionnee - 0.5,
            y0=0,
            x1=indice_region_selectionnee + 0.5,
            y1=moyennes_attaque.loc[region_selectionnee, "Avg_Poss_Attack"] + 1,
            line=dict(
                color="red",
                width=3,
            ),
            fillcolor="rgba(0,0,0,0)",
        )

    return fig
