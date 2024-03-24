import plotly.graph_objs as go

from plotly import graph_objects as go

def get_figure(data, team):
    fig = go.Figure()

    color_scale = ['#999999','#999999','#999999','#999999','#999999']

    # Add funnel traces
    fig.add_trace(go.Funnel(
        name='Namibie',
        orientation='h',
        y=["8ème"],
        x=[200],
        text=["Namibie"],  # Add name here
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
        name='Cameroun',
        orientation='h',
        y=["8ème"],
        x=[200],
        text=["Cameroun"],  # Add name here
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
        name='Mauritanie',
        orientation='h',
        y=["8ème"],
        x=[200],
        text=["Mauritanie"],  # Add name here
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
        name='Maroc',
        orientation='h',
        y=["8ème"],
        x=[200],
        text=["Maroc"],  # Add name here
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
        name='Guinée Éq.',
        orientation='h',
        y=["8ème"],
        x=[200],
        text=["Guinée Éq."],  # Add name here
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
        name='Egypte',
        orientation='h',
        y=["8ème"],
        x=[200],
        text=["Egypte"],  # Add name here
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
        name='Sénégal',
        orientation='h',
        y=["8ème"],
        x=[200],
        text=["Sénégal"],  # Add name here
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
        name='Burk. Faso',
        orientation='h',
        y=["8ème"],
        x=[200],
        text=["Burk. Faso"],  # Add name here
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
        name='Cap-Vert',
        orientation='h',
        y=["8ème", "Quart"],
        x=[200, 200],
        text=["Cap-Vert", "Cap-Vert"],  # Add names here
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
        name='Guinée',
        orientation='h',
        y=["8ème", "Quart"],
        x=[200, 200],
        text=["Guinée", "Guinée"],  # Add names here
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
        name='Af. du Sud',
        orientation='h',
        y=["8ème", "Quart", "Semi-finale"],
        x=[200, 200, 200],
        text=["Af. du Sud", "Af. du Sud", "Af. du Sud"],  # Add names here
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
        name='RD Congo',
        orientation='h',
        y=["8ème", "Quart", "Semi-finale"],
        x=[200, 200, 200],
        text=["RD Congo", "RD Congo", "RD Congo"],  # Add names here
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
        name='Côte d\'Ivoire',
        orientation='h',
        y=["8ème", "Quart", "Semi-finale", "Finale", "Winner"],
        x=[200, 200, 200, 200, 200],
        text=["Côte d'Iv.", "Côte d'Iv.", "Côte d'Iv.", "Côte d'Iv.", "Côte d'Iv."],  # Add names here
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