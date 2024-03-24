import plotly.graph_objs as go

def get_figure(data):
    # EXEMPLE : pie chart avec toy dataset
    fig = {
        'data': [
            go.Pie(
                labels=data['Category'],
                values=data['Values']
            )
        ],
        'layout': go.Layout(
            title='Pie Chart'
        )
    }
    return fig