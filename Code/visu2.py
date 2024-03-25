from app_init import app

import dash
import copy
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

def get_section(data : pd.DataFrame, team : str) -> dcc.Graph :
    global DATA
    DATA = copy.deepcopy(data)
    global TEAM
    TEAM = copy.deepcopy(team)
    return [html.Div([
                dcc.RadioItems(
                    id='radio-buttons',
                    options=[
                        {'label': '  Attaque', 'value': 'Attaque'},
                        {'label': '  Défense', 'value': 'Défense'},
                    ],
                    value='Attaque',  # Valeur sélectionnée par défaut
                    labelStyle={'display': 'inline-block', 'margin-right': '10px'}
                ),
            ], style={'border': '1px solid #ccc', 'padding': '10px', 'display': 'inline-block', 'margin-left': '20%'}),
            
            html.Div(id='blabla')
            ]

@app.callback(
    Output('blabla', 'children'),
    [Input('radio-buttons', 'value')]
)
def update_output(selected_option):
    print(selected_option)
    if selected_option == 'Attaque' : 
        return [html.Div([dcc.Graph(
            id='visu_3',
            figure=get_figure(data=DATA, team=TEAM),
            style={'width': '70%', 'margin': '0 auto'})],
                        className='Attaque')]
    else : 
        return [html.Div([dcc.Graph(
            id='visu_3',
            figure=get_figure(data=DATA, team=TEAM),
            style={'width': '70%', 'margin': '0 auto'}),
                dcc.Graph(
            id='visu_3',
            figure=get_figure(data=DATA, team=TEAM),
            style={'width': '70%', 'margin': '0 auto'})
            ])]

def get_figure(data : pd.DataFrame, team : str) -> dict :
    # EXEMPLE : barplot avec toy dataset
    fig = {
        'data': [
            go.Bar(
                x=data['Category'],
                y=data['Values']
            )
        ],
        'layout': go.Layout(
            title='Bar Chart'
        )
    }
    return fig