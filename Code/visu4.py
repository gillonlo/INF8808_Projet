import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output
from app_init import app

def get_section(data: pd.DataFrame, team: str) -> list:
    return [
        html.Div([
            dcc.RadioItems(
                id='criteria',
                options=[
                    {'label': '  Attaque', 'value': 'Attaque'},
                    {'label': '  Défense', 'value': 'Défense'},
                ],
                value='Attaque',
                labelStyle={'display': 'inline-block', 'margin-right': '10px'},
                style={'border': '1px solid #ccc', 'padding': '10px', 'display': 'inline-block', 'margin-left': '20%'}
            ),
            dcc.Graph(
                id='visu_4',
                figure=get_figure(data=data, team=team),
                style={'width': '70%', 'margin': '0 auto'}
            ),
            html.Div(id='output-container-radio'),  # Ajouter un élément de sortie pour l'option sélectionnée
            html.Div(id='output-container-map')  # Ajouter un élément de sortie pour la région sélectionnée sur la carte
        ])
    ]

def get_figure(data: pd.DataFrame, team: str) -> dict:
    # Créer une carte de l'Afrique avec des régions colorées
    fig = px.choropleth(data, 
                        locations="Squad",  # Colonnes des noms de pays
                        locationmode="country names",  # Mode de localisation des pays
                        color="Region",  # Colonne de la région
                        hover_name="Region",  # Nom à afficher au survol
                        color_discrete_map={"Nord": "blue", "Australe": "orange", "Ouest": "red", "Centrale": "green", "Est": "yellow"},
                        scope="africa")

    fig.update_geos(showcountries=True, showcoastlines=False, showland=False, fitbounds="locations", showframe=False)
    fig.update_traces(hovertemplate="<b>%{hovertext}</b><br>")

    # Désactiver le zoom et le panoramique
    fig.update_layout(
        dragmode=False,
        uirevision=True,
        margin=dict(l=0, r=50, t=0, b=0),  # Réduire les marges
        clickmode='event+select',  # Activer le mode de clic pour récupérer la région sélectionnée
    )

    return fig

@app.callback(
    Output('output-container-radio', 'children'),
    [Input('criteria', 'value')]
)
def display_selected_option(value):
    print( f"The selected option is: {value}")

@app.callback(
    Output('output-container-map', 'children'),
    [Input('visu_4', 'selectedData')]
)
def display_selected_region(selectedData):
    if selectedData:
        selected_region = selectedData['points'][0]['hovertext']
        print( f"You selected the {selected_region} region.")


