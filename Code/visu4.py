import copy
import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output
from app_init import app

def get_section(data: pd.DataFrame, team: str) -> list:
    global data_copy
    data_copy = copy.deepcopy(data)
    
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
                figure=get_figure(data=data[0], team=team),
                style={'width': '70%', 'margin': '0 auto'}
            ),
            dcc.Graph(
                id='bar_plot',  # Ajout de l'identifiant pour le graphique à barres
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
        margin=dict(l=0, r=50, t=0, b=0),
        clickmode='event+select',  
    )
    
    return fig

@app.callback(
    Output('output-container-radio', 'children'),
    [Input('criteria', 'value')]
)
def display_selected_option(value):
    print( f"The selected option is: {value}")
    if value == 'Attaque':
        print("Voici les données d'attaque :")
        print(data_copy[2])  
    elif value == 'Défense':
        print("Voici les données de défense :")
        print(data_copy[3])  
    else:
        print("Option invalide : veuillez sélectionner 'Attaque' ou 'Défense'.")

@app.callback(
    Output('output-container-map', 'children'),
    [Input('visu_4', 'selectedData')]
)
def display_selected_region(selectedData):
    if selectedData:
        selected_region = selectedData['points'][0]['hovertext']
        print(f"You selected the {selected_region} region.")
        # Filtrer les données pour n'afficher que les pays de la région sélectionnée
        filtered_data = data_copy[0][data_copy[0]['Region'] == selected_region]
        # Créer une liste des noms de pays de cette région
        countries_in_region = filtered_data['Squad'].tolist()
        print(f"Countries in the {selected_region} region: {countries_in_region}")
        return countries_in_region
    else:
        return None


@app.callback(
    Output('bar_plot', 'figure'),
    [Input('criteria', 'value'),
     Input('visu_4', 'selectedData')]
)
def update_bar_plot(value, selectedData):
    print('helooooooooooo')
    
    attack_means = data_copy[2]
    defense_means = data_copy[3]
    
    if value == 'Attaque':
        fig = go.Figure(data=[
            go.Bar(name='Average Goals Scored per 90 Minutes', x=attack_means.index, y=attack_means['Avg_Gls90_Attack']),
            go.Bar(name='Average Assists per 90 Minutes', x=attack_means.index, y=attack_means['Avg_Ast90_Attack']),
            go.Bar(name='Average Possession', x=attack_means.index, y=attack_means['Avg_Poss_Attack'])
        ])
        fig.update_layout(barmode='group', title='Average Metrics for Attack by Region')
    elif value == 'Défense':
        
        fig = go.Figure(data=[
            go.Bar(name='Average Goals Conceded per 90 Minutes', x=defense_means.index, y=defense_means['Avg_Gls90_Defense']),
            go.Bar(name='Average Assists Conceded per 90 Minutes', x=defense_means.index, y=defense_means['Avg_Ast90_Defense']),
            go.Bar(name='Average Possession Conceded', x=defense_means.index, y=defense_means['Avg_Poss_Defense'])
        ])
        fig.update_layout(barmode='group', title='Average Metrics for Defense by Region')
    
    # Highlight selected region in red
    if selectedData:
        selected_region = selectedData['points'][0]['hovertext']
        selected_region_index = attack_means.index.get_loc(selected_region)
        fig.add_shape(
            type="rect",
            xref="x",
            yref="y",
            x0=selected_region_index - 0.5,
            y0=0,
            x1=selected_region_index + 0.5,
            y1=attack_means.loc[selected_region, 'Avg_Poss_Attack'] + 1,
            line=dict(
                color="red",
                width=3,
            ),
            fillcolor="rgba(0,0,0,0)"  
        )
    
    return fig


