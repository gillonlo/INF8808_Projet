from dash import dcc, html

def get_page() :
    return html.Div([
    html.H1("Another Page"),
    html.P("This is another page of your app."),
    html.Div(
        dcc.Link('Retour à la visualisation', href='/'),
        style={'padding' : '10px','textAlign': 'center'}
    )
])