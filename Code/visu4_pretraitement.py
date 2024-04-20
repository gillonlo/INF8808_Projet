import numpy as np
import pandas as pd

def get_data(data_teams_attack: pd.DataFrame, 
             data_players: pd.DataFrame, 
             data_tournament: pd.DataFrame, 
             data_teams_defense: pd.DataFrame) -> pd.DataFrame:
    
    regions = {
    'Algérie': 'Nord',
    'Angola': 'Australe',
    'Burkina Faso': 'Ouest',
    'Cameroun': 'Centrale',
    'Cap Vert': 'Ouest',
    'RD Congo': 'Centrale',
    "Côte d'Ivoire": 'Ouest',
    'Égypte': 'Nord',
    'Guinée Equ.': 'Centrale',
    'Gambie': 'Ouest',
    'Ghana': 'Ouest',
    'Guinée': 'Ouest',
    'Guinée-Bissau': 'Ouest',
    'Mali': 'Ouest',
    'Mauritanie': 'Nord',
    'Maroc': 'Nord',
    'Mozambique': 'Australe',
    'Namibie': 'Australe',
    'Nigéria': 'Ouest',
    'Sénégal': 'Ouest',
    'Afrique du Sud': 'Australe',
    'Tanzanie': 'Est',
    'Tunisie': 'Nord',
    'Zambie': 'Australe'
    }

   
    # Ajouter une colonne de région en utilisant le dictionnaire de mapping
    data_teams_attack['Region'] = data_teams_attack['Squad'].map(regions)
    # Enlever les 3 premiers caractères de la colonne 'Squad' pour la défense
    data_teams_defense['Squad'] = data_teams_defense['Squad'].str.slice(3)
    data_teams_defense['Region'] = data_teams_defense['Squad'].map(regions)


    # Calculer les moyennes pour l'attaque
    attack_means = data_teams_attack.groupby('Region')[['Gls90', 'Ast90', 'Poss','G-PK90']].mean()
    attack_means.rename(columns={'Gls90': 'Avg_Gls90_Attack', 'Ast90': 'Avg_Ast90_Attack', 'Poss': 'Avg_Poss_Attack','G-PK90':'Avg_G-PK90_Attack'}, inplace=True)

    # Calculer les moyennes pour la défense
    defense_means = data_teams_defense.groupby('Region')[['Gls90', 'Ast90', 'Poss','G-PK90']].mean()
    defense_means.rename(columns={'Gls90': 'Avg_Gls90_Defense', 'Ast90': 'Avg_Ast90_Defense', 'Poss': 'Avg_Poss_Defense','G-PK90':'Avg_G-PK90_Defense'}, inplace=True)

    # Ramener la colonne 'Poss' à une échelle de 0 à 1
    attack_means['Avg_Poss_Attack'] /= 100
    defense_means['Avg_Poss_Defense'] /= 100

    return [data_teams_attack,data_teams_defense,attack_means, defense_means]
