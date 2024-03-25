import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

def get_section(data : pd.DataFrame, team : str) -> dcc.Graph :
    return [dcc.Graph(
            id='visu_2',
            figure=get_figure(data=data, team=team),
            style={'width': '70%', 'margin': '0 auto'})
            ]

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