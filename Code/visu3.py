import dash
import pandas as pd
from dash import dcc, html
import plotly.express as px
import plotly.graph_objs as go
from dash.dependencies import Input, Output

to_replace = {0 : 'Poule',
              1 : '8ème',
              2: 'Quart' ,
              3: 'Semi',
              3.5 : 'Semi' ,
              4 : 'Finale',
              5 : 'Gagnant'}

def get_section(data : pd.DataFrame, team : str) -> dcc.Graph :
    print( sorted(list(data['Round'].unique())))
    return [dcc.Graph(
            id='visu_3',
            figure=get_figure(data=data[data['Round'] == i], team=team, criteria='Fatigue', phase=i),
            style={'width': '50%', 'margin': '0 auto'})
            for i in sorted(list(data['Round'].unique()))]

def get_figure(data : pd.DataFrame, team : str, criteria : str, phase : float) -> dict :
    
    fig = px.strip(data, x=criteria, stripmode='group',range_y=[-0.10,0.10], )
    
    fig.update_layout(
        title = to_replace[phase],
        height=200,
        plot_bgcolor='rgba(0, 0, 0, 0)'
    )
    
    return fig