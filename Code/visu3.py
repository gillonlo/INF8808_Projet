import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

def get_section(data : pd.DataFrame, team : str) -> dcc.Graph :
    return [dcc.Graph(
            id='visu_3',
            figure=get_figure(data=data, team=team),
            style={'width': '70%', 'margin': '0 auto'})
            ]

def get_figure(data : pd.DataFrame, team : str) -> dict :
    labels = ['A', 'B', 'C', 'D', 'E']
    values = [20, 30, 25, 15, 10]
    # EXEMPLE : pie chart avec toy dataset
    fig = {
    'data': [
        go.Pie(
            labels=labels,
            values=values
        )
    ],
    'layout': go.Layout(
        title='Pie Chart'
    )
}
    return fig