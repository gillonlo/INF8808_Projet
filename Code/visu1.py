import dash
import math
import numpy as np
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.express as px

df_3 = pd.read_csv("Data/projet_data_3.csv", delimiter=';')

def get_section(data : pd.DataFrame, team : str) -> list :
    
    return [dcc.Graph(
            id='visu_1',
            figure=get_figure(data=data, team=team),
            style={'width': '70%', 'margin': '0 auto'})
            ]

def get_figure(data : pd.DataFrame, team : str) -> dict :
    fig = go.Figure()

    color_scale = ['#999999']
    name_of_round = ['8ème','Quart','Semi','Finale','Gagnant']
    

    rounds = np.delete( df_3['Round'].unique(), 3)
    rounds = np.insert(rounds, 4, "Gagnant")
    
    for i in range(len(data)) :
        round = math.floor(data.at[i,'Round'])
        name = data.at[i,'Team']

        match_df = df_3[df_3['Team1'].str.contains(name) | df_3['Team2'].str.contains(name)]      
        idx = 0  
        list_match = []
        for item in match_df.iterrows() : 
            list_match.append(str(name_of_round[idx]) + " : " + item[1]['Team1'] + " vs " + item[1]['Team2'] + "  "+  item[1]['Score'])
            list_match.append("Nombre de spectateurs : " + item[1]['Attendance'])
            list_match.append("")
            idx+=1
        if i == 15 : 
            list_match.append("Gagnant de la CAN")
        elif i == 14:
            list_match.append("2e de la CAN")
        elif i == 13:
            list_match.append("3e de la CAN")    
        elif i == 12:
            list_match.append("4e de la CAN")

        fig.add_trace(go.Funnel(
            name=name,
            orientation='h',
            y=name_of_round[:round],
            x=round*[200],
            text=round*[name],
            textinfo="text",
            marker=dict(color=color_scale[0]),
            hovertemplate='<b>%{text}</b>' + '<extra></extra>' + '<br>' + '<br>' + "Parcours complet :"  + '<br>' + "<br>".join(list_match)

        ))
        
        fig.add_trace(go.Funnel(
            y=name_of_round[:round],
            x=round*[5],
            text=round*[''],
            textinfo="text",
            opacity=0, 
            hoverinfo='skip'
        ))

    # Update the emphasized funnel color to red
    for trace in fig.data:
        if trace.name == team:
            trace.marker.color = 'red'

    # Update layout
    fig.update_layout(title={'text': 'Tournois', 'x':0.5, 'y':0.95, 'xanchor': 'center', 'yanchor': 'top'},
                      plot_bgcolor='white',
                      showlegend=False)
    
    return fig


