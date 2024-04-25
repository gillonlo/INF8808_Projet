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
    all_regions = {
        "Nord": [
            "Algeria",
            "Egypt",
            "Libya",
            "Morocco",
            "Tunisia"
        ],
        "Est": [
            "Burundi",
            "Djibouti",
            "Eritrea",
            "Ethiopia",
            "Kenya",
            "Rwanda",
            "Somalia",
            "South Sudan",
            "Sudan",
            "Tanzania",
            "Uganda"
        ],       
        "Ouest": [
            "Benin",
            "Burkina Faso",
            'Cape Verde',
            "Chad",
            "Gambia",
            "Ghana",
            "Guinea",
            "Guinea-Bissau",
            "Ivory Coast",
            "Liberia",
            "Mali",
            "Mauritania",
            "Niger",
            "Nigeria",
            "Senegal",
            "Sierra Leone",
            "Togo"
        ],
        "Centrale": [
            "Cameroon",
            "Central African Republic",
            "Chad",
            "Congo",
            "DR Congo",
            "Equatorial Guinea",
            "Gabon",
            "Sao Tome and Principe"
        ],
        "Australe": [
            "Angola",
            "Botswana",
            "Eswatini",
            "Lesotho",
            "Madagascar",
            "Malawi",
            "Mauritius",
            "Mozambique",
            "Namibia",
            "Seychelles",
            "South Africa",
            "Zambia",
            "Zimbabwe"
        ]
    }

    """
    regions = {
        "Nord": ["Maroc", "Algérie", "Tunisie", "Égypte", "Libie"],
        "Est": ["Soudan", "Soudan du Sud", "Éthiopie", "Somalie", "Kénya", "Ouganda", "Rwanda", "Burundi", "Tanzanie", "Djibouti", "Érythrée"],
        "Ouest": ["Mauritanie", "Mali", "Niger", "Nigéria", "Chad", "Sénégal", "Gambie", "Guinée-Bissau", "Guinée", "Sierra Leone", "Libéria", "Côte d'Ivoire", "Burkina Faso", "Ghana", "Togo", "Bénin"],
        "Centrale": ["Cameroun", "République centrafricaine", "Chad", "RD Congo", "Congo", "Gabon", "Guinée Equ.", "Sao Tomé et Principe"],
        "Australe": ["Angola", "Zambie", "Zimbabwe", "Malawi", "Botswana", "Namibie", "Afrique du Sud", "Lesotho", "Swaziland", "Madagascar"]
    }

    """

    # Define your dictionary mapping English names to French names
    english_to_french = {
        "Morocco": "Maroc", "Algeria": "Algérie", "Tunisia": "Tunisie", "Egypt": "Égypte", "Libya": "Libie", "Cape Verde": "Cap vert",
        "Sudan": "Soudan", "South Sudan": "Soudan du Sud", "Ethiopia": "Éthiopie", "Somalia": "Somalie",
        "Kenya": "Kénya", "Uganda": "Ouganda", "Rwanda": "Rwanda", "Burundi": "Burundi", "Tanzania": "Tanzanie",
        "Djibouti": "Djibouti", "Eritrea": "Érythrée", "Mauritania": "Mauritanie", "Mali": "Mali", "Niger": "Niger",
        "Nigeria": "Nigéria", "Chad": "Chad", "Senegal": "Sénégal", "Gambia": "Gambie", "Guinea-Bissau": "Guinée-Bissau",
        "Guinea": "Guinée", "Sierra Leone": "Sierra Leone", "Liberia": "Libéria", "Ivory Coast": "Côte d'Ivoire",
        "Burkina Faso": "Burkina Faso", "Ghana": "Ghana", "Togo": "Togo", "Benin": "Bénin", "Cameroon": "Cameroun",
        "Central African Republic": "République centrafricaine", "DR Congo": "RD Congo", "Congo": "Congo", "Gabon": "Gabon",
        "Equatorial Guinea": "Guinée Equ.", "Sao Tome and Principe": "Sao Tomé et Principe", "Angola": "Angola",
        "Zambia": "Zambie", "Zimbabwe": "Zimbabwe", "Malawi": "Malawi", "Botswana": "Botswana", "Namibia": "Namibie",
        "South Africa": "Afrique du Sud", "Lesotho": "Lesotho", "Eswatini": "Eswatini", "Madagascar": "Madagascar",
        "Mauritius": "Île Maurice", "Mozambique": "Mozambique", "Seychelles": "Seychelles"
    }

    # Récupération de la région du pays sélectionné
    selected_region = data[data["Squad"] == team]["Region"].iloc[0]

    # Pays ayant joué triés par région
    participating_regions = {
        'Nord': ['Algeria', 'Egypt', 'Mauritania', 'Morocco', 'Tunisia'],
        'Ouest': ['Burkina Faso', 'Cape Verde', 'Ghana', 'Gambia', 'Guinea', 'Guinea-Bissau', 'Ivory Coast', 'Mali', 'Nigeria', 'Senegal'],
        'Centrale': ['Cameroon', 'DR Congo', 'Equatorial Guinea'],
        'Est': ['Tanzania'],
        'Australe': ['Angola', 'Mozambique', 'Namibia', 'South Africa', 'Zambia']
    }

    # Liste complète des pays d'Afrique (en anglais)
    all_african_countries = [
        'Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde', 'Central African Republic', 'Congo', 'Ivory Coast',
        'Djibouti', 'Egypt', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau',
        'Equatorial Guinea', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Morocco', 'Mauritius',
        'Mauritania', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Uganda', 'DR Congo', 'Rwanda',
        'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'Sudan', 'South Africa', 'South Sudan', 'Tanzania',
        'Chad', 'Togo', 'Tunisia', 'Zambia', 'Zimbabwe'
    ]

    # Associer le bon code couleur à chaque pays
    country_categories = {country: 0 for country in all_african_countries}  # Tous les pays sont considérés comme n'ayant pas joué par défaut
    for region, countries in all_regions.items():
        for country in countries:
            if region == selected_region:
                country_categories[country] = 2 # Le pays est dans la région sélectionnée
            elif country in participating_regions[region]:
                country_categories[country] = 1 # Le pays a joué mais n'est pas dans la région sélectionnée
    
    # Échelle de couleur pour nos 3 catégories
    color_scale = [
        (0, "lightgrey"),               # Pays n'ayant pas participé à la CAN
        (1/2, "rgba(153,153,153,255)"), # Pays hors de la région sélectionnée ayant participé à la CAN
        (1, "rgba(255, 0, 0, 0.7)")     # Pays dans la région sélectionnée
    ]

    # Création de la carte de l'Afrique
    locations_countries = list(country_categories.keys())
    categories = [country_categories[country] for country in locations_countries]  
    location_to_region = {country: region for region, countries in all_regions.items() for country in countries} 
    
    fig = go.Figure(data=go.Choropleth(
        locations=locations_countries,
        z=categories,
        locationmode='country names',
        colorscale=color_scale,
        text=[f"{english_to_french[loc]}<br>Region: {location_to_region[loc]}" for loc in locations_countries],
        hovertemplate= '%{text}<extra></extra>',
        showlegend=False,
        showscale=False  # Ne pas afficher l'échelle
    ))
    
    # Mise en forme de la carte
    fig.update_layout(
        title_text="Carte de l'Afrique par régions",
        geo=dict(
            showframe=False, 
            showcoastlines=False, 
            projection_type='equirectangular', 
            bgcolor="rgba(198,240,248,0.7)",
            scope='africa'
        )
    )
    
    # Changer la couleur des labels
    hover_colors = ["lightgrey", "rgba(153,153,153,255)", "rgba(255, 0, 0, 0.7)"]
    for trace in fig.data:
        hover_bg_colors = []
        font_colors = []
        for z in trace.z:
            color = hover_colors[int(z)]
            hover_bg_colors.append(color)
            # Adapter la couleur du texte en fonction de la couleur de fond
            if color in ["rgba(153,153,153,255)", "rgba(255, 0, 0, 0.7)"]:
                font_colors.append('white')
            else:
                font_colors.append('black')

        trace.hoverlabel.bgcolor = hover_bg_colors
        trace.hoverlabel.font.color = font_colors

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
                    hoverlabel = dict(bordercolor = "white", font = dict(color = "white")),
                    marker=dict(color="#2ca02c"),
                ),
                go.Bar(
                    name="Possession moyenne",
                    x=moyennes_attaque.index,
                    y=moyennes_attaque["Avg_Poss_Attack"],
                    hovertemplate="Région: %{x}<br>Possession: %{y}%<extra></extra>",
                    hoverlabel = dict(bordercolor = "white", font = dict(color = "white")),
                    marker=dict(color="#1f77b4"),
                ),
                go.Bar(
                    name="Buts hors penalty marqués en moyenne<br>par 90 minutes",
                    x=moyennes_attaque.index,
                    y=moyennes_attaque["Avg_G-PK90_Attack"],
                    hovertemplate="Région: %{x}<br>Buts hors penalty marqués: %{y}<extra></extra>",
                    hoverlabel = dict(bordercolor = "white", font = dict(color = "white")),
                    marker=dict(color="#ff5733"),
                ),
                go.Bar(
                    name="Passes décisives en moyenne<br>par 90 minutes",
                    x=moyennes_attaque.index,
                    y=moyennes_attaque["Avg_Ast90_Attack"],
                    hovertemplate="Région: %{x}<br>Passe décisive: %{y}<extra></extra>",
                    hoverlabel = dict(bordercolor = "white", font = dict(color = "white")),
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
                    hoverlabel = dict(bordercolor = "white", font = dict(color = "white")),
                    marker=dict(color="#2ca02c"),
                ),
                go.Bar(
                    name="Possession concédée moyenne",
                    x=moyennes_defense.index,
                    y=moyennes_defense["Avg_Poss_Defense"],
                    hovertemplate="Région: %{x}<br>Possession concédée: %{y}%<extra></extra>",
                    hoverlabel = dict(bordercolor = "white", font = dict(color = "white")),
                    marker=dict(color="#1f77b4"),
                ),
                go.Bar(
                    name="Buts hors penalty concédés en moyenne<br>par 90 minutes",
                    x=moyennes_attaque.index,
                    y=moyennes_defense["Avg_G-PK90_Defense"],
                    hovertemplate="Région: %{x}<br>Buts hors penalty concédés: %{y}<extra></extra>",
                    hoverlabel = dict(bordercolor = "white", font = dict(color = "white")),
                    marker=dict(color="#ff5733"),
                ),
                go.Bar(
                    name="Passes décisives concédées en moyenne<br>par 90 minutes",
                    x=moyennes_defense.index,
                    y=moyennes_defense["Avg_Ast90_Defense"],
                    hovertemplate="Région: %{x}<br>Passe décisive concédée: %{y}<extra></extra>",
                    hoverlabel = dict(bordercolor = "white", font = dict(color = "white")),
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
