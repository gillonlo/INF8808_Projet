import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

def get_section(data : pd.DataFrame, team : str) -> dcc.Graph :
    
    return [dcc.Graph(
            id='visu_1',
            figure=get_figure(data=data, team=team),
            style={'width': '70%', 'margin': '0 auto'})
            ]

def get_figure(data : pd.DataFrame, team : str) -> dict :
    fig = go.Figure()

    color_scale = ['#999999','#999999','#999999','#999999','#999999']

    # Add funnel traces
    fig.add_trace(go.Funnel(
        name='Namibia',
        orientation='h',
        y=["8ème"],
        x=[200],
        text=["Namibia"],  # Add name here
        textinfo="text",
        marker=dict(color=color_scale[0])
    ))

    fig.add_trace(go.Funnel(
                y=[f"8ème"],
                x=[5],
                text=[''],  # Empty text
                textinfo="text",
                opacity=0  # Make it transparent
            ))

    fig.add_trace(go.Funnel(
        name='Cameroon',
        orientation='h',
        y=["8ème"],
        x=[200],
        text=["Cameroon"],  # Add name here
        textinfo="text",
        marker=dict(color=color_scale[0])
    ))

    fig.add_trace(go.Funnel(
                y=[f"8ème"],
                x=[5],
                text=[''],  # Empty text
                textinfo="text",
                opacity=0  # Make it transparent
            ))

    fig.add_trace(go.Funnel(
        name='Mauritania',
        orientation='h',
        y=["8ème"],
        x=[200],
        text=["Mauritania"],  # Add name here
        textinfo="text",
        marker=dict(color=color_scale[0])
    ))

    fig.add_trace(go.Funnel(
                y=[f"8ème"],
                x=[5],
                text=[''],  # Empty text
                textinfo="text",
                opacity=0  # Make it transparent
            ))

    fig.add_trace(go.Funnel(
        name='Morocco',
        orientation='h',
        y=["8ème"],
        x=[200],
        text=["Morocco"],  # Add name here
        textinfo="text",
        marker=dict(color=color_scale[0])
    ))

    fig.add_trace(go.Funnel(
                y=[f"8ème"],
                x=[5],
                text=[''],  # Empty text
                textinfo="text",
                opacity=0  # Make it transparent
            ))

    fig.add_trace(go.Funnel(
        name='Equ. Guinea',
        orientation='h',
        y=["8ème"],
        x=[200],
        text=["Equ. Guinea"],  # Add name here
        textinfo="text",
        marker=dict(color=color_scale[0])
    ))

    fig.add_trace(go.Funnel(
                y=[f"8ème"],
                x=[5],
                text=[''],  # Empty text
                textinfo="text",
                opacity=0  # Make it transparent
            ))

    fig.add_trace(go.Funnel(
        name='Egypt',
        orientation='h',
        y=["8ème"],
        x=[200],
        text=["Egypt"],  # Add name here
        textinfo="text",
        marker=dict(color=color_scale[0])
    ))

    fig.add_trace(go.Funnel(
                y=[f"8ème"],
                x=[5],
                text=[''],  # Empty text
                textinfo="text",
                opacity=0  # Make it transparent
            ))

    fig.add_trace(go.Funnel(
        name='Senegal',
        orientation='h',
        y=["8ème"],
        x=[200],
        text=["Senegal"],  # Add name here
        textinfo="text",
        marker=dict(color=color_scale[0])
    ))

    fig.add_trace(go.Funnel(
                y=[f"8ème"],
                x=[5],
                text=[''],  # Empty text
                textinfo="text",
                opacity=0  # Make it transparent
            ))

    fig.add_trace(go.Funnel(
        name='Burkina Faso',
        orientation='h',
        y=["8ème"],
        x=[200],
        text=["Burkina Faso"],  # Add name here
        textinfo="text",
        marker=dict(color=color_scale[0])
    ))

    fig.add_trace(go.Funnel(
                y=[f"8ème"],
                x=[5],
                text=[''],  # Empty text
                textinfo="text",
                opacity=0  # Make it transparent
            ))

    fig.add_trace(go.Funnel(
        name='Angola',
        orientation='h',
        y=["8ème", "Quart"],
        x=[200, 200],
        text=["Angola", "Angola"],  # Add names here
        textinfo="text",
        marker=dict(color=color_scale[1])
    ))

    fig.add_trace(go.Funnel(
                y=["8ème", "Quart"],
                x=[5, 5],
                text=['',''],  # Empty text
                textinfo="text",
                opacity=0  # Make it transparent
            ))

    fig.add_trace(go.Funnel(
        name='Cape Verde',
        orientation='h',
        y=["8ème", "Quart"],
        x=[200, 200],
        text=["Cape Verde", "Cape Verde"],  # Add names here
        textinfo="text",
        marker=dict(color=color_scale[1])
    ))

    fig.add_trace(go.Funnel(
                y=["8ème", "Quart"],
                x=[5, 5],
                text=['',''],  # Empty text
                textinfo="text",
                opacity=0  # Make it transparent
            ))

    fig.add_trace(go.Funnel(
        name='Guinea',
        orientation='h',
        y=["8ème", "Quart"],
        x=[200, 200],
        text=["Guinea", "Guinea"],  # Add names here
        textinfo="text",
        marker=dict(color=color_scale[1])
    ))

    fig.add_trace(go.Funnel(
                y=["8ème", "Quart"],
                x=[5, 5],
                text=['',''],  # Empty text
                textinfo="text",
                opacity=0  # Make it transparent
            ))

    fig.add_trace(go.Funnel(
        name='Mali',
        orientation='h',
        y=["8ème", "Quart"],
        x=[200, 200],
        text=["Mali", "Mali"],  # Add names here
        textinfo="text",
        marker=dict(color=color_scale[1])
    ))

    fig.add_trace(go.Funnel(
                y=["8ème", "Quart"],
                x=[5, 5],
                text=['',''],  # Empty text
                textinfo="text",
                opacity=0  # Make it transparent
            ))

    fig.add_trace(go.Funnel(
        name='South Africa',
        orientation='h',
        y=["8ème", "Quart", "Semi-finale"],
        x=[200, 200, 200],
        text=["South Africa", "South Africa", "South Africa"],  # Add names here
        textinfo="text",
        marker=dict(color=color_scale[2])
    ))

    fig.add_trace(go.Funnel(
                y=["8ème", "Quart", "Semi-finale"],
                x=[5, 5,5],
                text=['','',''],  # Empty text
                textinfo="text",
                opacity=0  # Make it transparent
            ))

    fig.add_trace(go.Funnel(
        name='Congo DR',
        orientation='h',
        y=["8ème", "Quart", "Semi-finale"],
        x=[200, 200, 200],
        text=["Congo DR", "Congo DR", "Congo DR"],  # Add names here
        textinfo="text",
        marker=dict(color=color_scale[2])
    ))

    fig.add_trace(go.Funnel(
                y=["8ème", "Quart", "Semi-finale"],
                x=[5, 5,5],
                text=['','',''],  # Empty text
                textinfo="text",
                opacity=0  # Make it transparent
            ))

    fig.add_trace(go.Funnel(
        name='Nigeria',
        orientation='h',
        y=["8ème", "Quart", "Semi-finale", "Finale"],
        x=[200, 200, 200, 200],
        text=["Nigeria", "Nigeria", "Nigeria", "Nigeria"],  # Add names here
        textinfo="text",
        marker=dict(color=color_scale[3])
    ))

    fig.add_trace(go.Funnel(
                y=["8ème", "Quart", "Semi-finale","Finale"],
                x=[5, 5,5,5],
                text=['','','',''],  # Empty text
                textinfo="text",
                opacity=0  # Make it transparent
            ))

    fig.add_trace(go.Funnel(
        name="Côte d'Ivoire",
        orientation='h',
        y=["8ème", "Quart", "Semi-finale", "Finale", "Winner"],
        x=[200, 200, 200, 200, 200],
        text=["Côte d'Ivoire", "Côte d'Ivoire", "Côte d'Ivoire", "Côte d'Ivoire", "Côte d'Ivoire"],  # Add names here
        textinfo="text",
        marker=dict(color=color_scale[4])
    ))

    fig.add_trace(go.Funnel(
        y=["8ème", "Quart", "Semi-finale","Finale", "Winner"],
        x=[5, 5,5,5,5],
        text=['','','','',''],  # Empty text
        textinfo="text",
        opacity=0  # Make it transparent
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