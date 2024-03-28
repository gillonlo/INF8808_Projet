import numpy as np
import pandas as pd

def get_data(data_teams_attack : pd.DataFrame, 
             data_players : pd.DataFrame, 
             data_tournament : pd.DataFrame, 
             data_teams_defense : pd.DataFrame) -> pd.DataFrame :
    
    regions = {
    'Algeria': 'Nord',
    'Angola': 'Australe',
    'Burkina Faso': 'Ouest',
    'Cameroon': 'Centre',
    'Cape Verde': 'Ouest',
    'Congo DR': 'Centre',
    "Côte d'Ivoire": 'Ouest',
    'Egypt': 'Nord',
    'Equ. Guinea': 'Centre',
    'Gambia': 'Ouest',
    'Ghana': 'Ouest',
    'Guinea': 'Ouest',
    'Guinea-Bissau': 'Ouest',
    'Mali': 'Ouest',
    'Mauritania': 'Nord',
    'Morocco': 'Nord',
    'Mozambique': 'Australe',
    'Namibia': 'Australe',
    'Nigeria': 'Ouest',
    'Senegal': 'Ouest',
    'South Africa': 'Australe',
    'Tanzania': 'Est',
    'Tunisia': 'Nord',
    'Zambia': 'Australe'
}

    # Ajouter une colonne de région en utilisant le dictionnaire de mapping
    data_teams_attack['Region'] = data_teams_attack['Squad'].map(regions)
    return data_teams_attack