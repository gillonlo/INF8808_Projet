import numpy as np
import pandas as pd

def get_data(data_teams_attack: pd.DataFrame, 
             data_players: pd.DataFrame, 
             data_tournament: pd.DataFrame, 
             data_teams_defense: pd.DataFrame) -> pd.DataFrame:
    
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
    # Enlever les 3 premiers caractères de la colonne 'Squad' pour la défense
    data_teams_defense['Squad'] = data_teams_defense['Squad'].str.slice(3)
    data_teams_defense['Region'] = data_teams_defense['Squad'].map(regions)


    # Calculer les moyennes pour l'attaque
    attack_means = data_teams_attack.groupby('Region')[['Gls90', 'Ast90', 'Poss']].mean()
    attack_means.rename(columns={'Gls90': 'Avg_Gls90_Attack', 'Ast90': 'Avg_Ast90_Attack', 'Poss': 'Avg_Poss_Attack'}, inplace=True)

    # Calculer les moyennes pour la défense
    defense_means = data_teams_defense.groupby('Region')[['Gls90', 'Ast90', 'Poss']].mean()
    defense_means.rename(columns={'Gls90': 'Avg_Gls90_Defense', 'Ast90': 'Avg_Ast90_Defense', 'Poss': 'Avg_Poss_Defense'}, inplace=True)

    return [data_teams_attack,data_teams_defense,attack_means, defense_means]