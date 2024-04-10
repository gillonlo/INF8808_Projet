import random
from Code.app_init import app

import dash
import copy
import pandas as pd
from dash import dcc, html
import plotly.express as px
import plotly.graph_objs as go
from dash.dependencies import Input, Output

to_replace = {0: 'Poule',
              1: '8ème',
              2: 'Quart',
              3: 'Semi',
              3.5: 'Semi',
              4: 'Finale',
              5: 'Gagnant'}


def get_section(data: pd.DataFrame, team: str) -> list:
    global DATA
    DATA = copy.deepcopy(data)
    global TEAM
    TEAM = copy.deepcopy(team)
    return [html.Div([
        dcc.RadioItems(
            id='criteria2',
            options=[
                {'label': '  Score', 'value': 'Score'},
                {'label': '  Âge', 'value': 'Age'},
                {'label': '  Fatigue', 'value': 'Fatigue'}
            ],
            value='Score',
            labelStyle={'display': 'inline-block',
                        'margin-right': '10px'}
        ),
    ], style={'border': '1px solid #ccc', 'padding': '10px', 'display': 'inline-block', 'margin-left': '20%'}),

        html.Div(id='beeswarm')
    ]


@app.callback(
    Output('beeswarm', 'children'),
    [Input('criteria2', 'value')]
)
def update_output(selected_option: str) -> list:
    return [dcc.Graph(
            id='visu_3',
            figure=get_figure(
                data=DATA[DATA['Round'] == i], team=TEAM, criteria=selected_option, phase=i),
            style={'width': '50%', 'margin': '0 auto'})
            for i in sorted(list(DATA['Round'].unique()))]


def get_figure(data: pd.DataFrame, team: str, criteria: str, phase: float) -> dict:
    scale = {'Score': [-0.5, 6],
             'Age': [15, 40],
             'Fatigue': [0, 100]}

    fig = go.Figure()

    # Add the first strip plot
    trigger = None
    for x in list(data['Squad'].unique()):
        if x != team:
            fig.add_trace(go.Scatter(
                x=data[data['Squad'] == x][criteria],
                y=[random.random()*20 for i in range(len(data[data['Squad'] == x][criteria]))],
                mode='markers',
                marker=dict(color='rgba(99, 110, 250, 255)', size=10,
                            line=dict(color='rgb(6, 18, 117, 230)', width=1)),
                hoverinfo='text',
                hovertemplate='<span style="font-size:20px">%{text}</span><br>' +
                "<b>Position:</b> %{customdata[0]}<br>" +
                "<b>Team:</b> %{customdata[1]}<br>" +
                "<b>Age:</b> %{customdata[2]}<br>" +
                "<b>Pourcentage de fatigue:</b> %{customdata[3]:.2f}<extra></extra>",
                text=data[data['Squad'] == x]['Player'],
                customdata=data[data['Squad'] == x][[
                    'Pos', 'Squad', 'Age', 'Fatigue']]
            ))
        else:
            trigger = 1

    if trigger is not None:
        fig.add_trace(go.Scatter(
            x=data[data['Squad'] == x][criteria],
            y=[random.random()*20 for i in range(len(data[data['Squad'] == x][criteria]))],
            mode='markers',
            marker=dict(color='rgba(235, 0, 0, 255)', size=10,
                        line=dict(color='rgb(255, 0, 0, 230)', width=1)),
            hoverinfo='text',
            hovertemplate='<span style="font-size:20px">%{text}</span><br>' +
            "<b>Position:</b> %{customdata[0]}<br>" +
            "<b>Team:</b> %{customdata[1]}<br>" +
            "<b>Age:</b> %{customdata[2]}<br>" +
            "<b>Pourcentage de fatigue:</b> %{customdata[3]:.2f}<extra></extra>",
            text=data[data['Squad'] == x]['Player'],
            customdata=data[data['Squad'] == x][[
                'Pos', 'Squad', 'Age', 'Fatigue']]
        ))
        print(data[data['Squad'] == x][[
            'Pos', 'Squad', 'Age', 'Fatigue']])
    fig.update_layout(
        title=to_replace[phase],
        height=200,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        yaxis=dict(showticklabels=False),
        margin=dict(l=10, r=10, t=50, b=5),
    )

    fig.update_layout(showlegend=False)

    fig.update_xaxes(range=scale[criteria])

    return fig
