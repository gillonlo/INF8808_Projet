import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

def get_section(data : pd.DataFrame, team : str) -> dcc.Graph :
    return [dcc.Graph(
            id='visu_4',
            figure=get_figure(data=data, team=team),
            style={'width': '70%', 'margin': '0 auto'})
            ]

def get_figure(data : pd.DataFrame, team : str) -> dict :
    # EXEMPLE : linechart avec toy dataset
    fig = {
        'data': [
            go.Scatter(
                x=[1, 2, 3, 4, 5],
                y=[10, 15, 13, 17, 20]
            )
        ],
        'layout': go.Layout(
            title='Line Chart'
        )
    }
    return fig