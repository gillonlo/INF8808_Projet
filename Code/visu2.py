from Code.app_init import app

import dash
import copy
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State


def get_section(data: pd.DataFrame, team: str) -> list:
    global DATA
    DATA = copy.deepcopy(data)
    global TEAM
    TEAM = copy.deepcopy(team)
    return [html.Div([
        dcc.RadioItems(
            id='criteriaPolar',
            options=[
                {'label': '  Attaque', 'value': 'Attaque'},
                {'label': '  Défense', 'value': 'Défense'},
            ],
            value='Attaque',
            labelStyle={'display': 'inline-block',
                        'margin-right': '10px'}
        ),
    ], style={'border': '1px solid #ccc', 'padding': '10px', 'display': 'inline-block', 'margin-left': '20%'}),

        html.Div(id='polar-charts')
    ]


@app.callback(
    Output('polar-charts', 'children'),
    [Input('criteriaPolar', 'value')]
)
def update_output(selected_option: str) -> list:
    if selected_option == 'Attaque':
        new_data = DATA.sort_values(
            by=['Attack_Sum'], ascending=False).reset_index(drop=True)
        index = [i for i in range(len(new_data))
                 if new_data.iloc[i]['Squad'] == TEAM]
        if index[0] <= 10:
            index = [9]
        categories = ['Passes tentées', 'Buts marqués',
                      'Passes décisives', 'Buts sans pénalité']

    else:
        new_data = DATA.sort_values(
            by=['Defense_Sum'], ascending=False).reset_index(drop=True)
        index = [i for i in range(len(new_data))
                 if new_data.iloc[i]['Squad'] == TEAM]
        if index[0] <= 10:
            index = [9]
        categories = ['Passes adverses tentées', 'Buts reçus',
                      'Passes décisives adverses', 'Buts sans pénalités reçus']
    return [
        html.Div(
            [dcc.Graph(
                id='visu_2_'+str(i),
                figure=get_figure(
                    data=new_data.iloc[i], team=TEAM, criteria=selected_option, categories=categories, classement=i),
                style={'width': '20%', 'margin': '0 auto', 'display': 'inline-block'})
                for i in list(range(9))+index
             ],
            className='row')
    ]


def get_figure(data: pd.DataFrame, team: str, criteria: str, categories: list[str], classement: int) -> dict:
    squad_name = data['Squad']

    if criteria == 'Attaque':
        values = data[['Passes tentées', 'Buts marqués',
                       'Passes décisives', 'Buts sans pénalité']].tolist()
    else:
        values = data[['Passes adverses tentées', 'Buts reçus',
                       'Passes décisives adverses', 'Buts sans pénalités reçus']].tolist()

    if squad_name == team:
        color = 'rgba(255, 0, 0, 0.3)'
    else:
        color = 'rgba(169, 169, 169, 0.1)'

    fig = go.Figure()

    # Add trace
    fig.add_trace(go.Barpolar(
        r=values,
        theta=categories,
        name=squad_name,
        hoverinfo="text",
        hovertemplate="%{theta}<br>""%{r}<extra></extra>",
    ))

    fig.update_layout(
        # Adding a title to the chart
        title=str(classement+1)+' : '+squad_name,
        polar=dict(
            radialaxis=dict(
                range=[0, 2.5],
                visible=True,
                tickmode='array',
                tickvals=[0, 0.5, 1, 1.5, 2, 2.5],  # Adjust this as needed
                ticktext=[0, 0.5, 1, 1.5, 2, 2.5]  # Adjust this as needed
            ),
            bgcolor=color
        ),
        title_x=0.5,  # Centering the title horizontally
        legend=dict(
            font=dict(
                size=10  # Adjust this value to change the size of the legend text
            )
        )
    )

    return fig
