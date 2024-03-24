import plotly.graph_objs as go

def get_figure(data):
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