import plotly.graph_objs as go

def get_figure(data):
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