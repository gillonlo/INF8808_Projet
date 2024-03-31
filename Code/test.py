import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.express as px


df_3 = pd.read_csv("Data/projet_data_3.csv", delimiter=';')

tt = ['8ème', 'Quart', 'Semi', 'Finale']

team = 'Angola'

test = df_3[df_3['Team1'].str.contains(team) | df_3['Team2'].str.contains(team)]

l = []
for item in test.iterrows() : 
   
   l.append("Match : "  + item[1]['Team1'] + " vs " + item[1]['Team2'] + '\n' + "Résultat : " + item[1]['Score'])

print(l)