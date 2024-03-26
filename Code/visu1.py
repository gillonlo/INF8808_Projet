import dash
import math
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

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
    
    for i in range(len(data)) :
        round = math.floor(data.at[i,'Round'])
        name = data.at[i,'Team']
        
        fig.add_trace(go.Funnel(
            name=name,
            orientation='h',
            y=name_of_round[:round],
            x=round*[200],
            text=round*[name],
            textinfo="text",
            marker=dict(color=color_scale[0])
        ))
        
        fig.add_trace(go.Funnel(
            y=name_of_round[:round],
            x=round*[5],
            text=round*[''],
            textinfo="text",
            opacity=0
        ))

    # Update the emphasized funnel color to red
    for trace in fig.data:
        if trace.name == team:
            trace.marker.color = 'red'

    # Update layout
    fig.update_layout(title={'text': 'Tournament', 'x':0.5, 'y':0.95, 'xanchor': 'center', 'yanchor': 'top'},
                      plot_bgcolor='white',
                      showlegend=False)
    
    return fig