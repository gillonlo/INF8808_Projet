import numpy as np
import pandas as pd


def get_data(data_teams_attack: pd.DataFrame,
             data_players: pd.DataFrame,
             data_tournament: pd.DataFrame,
             data_teams_defense: pd.DataFrame) -> pd.DataFrame:

    data_teams_attack = data_teams_attack.copy()
    data_teams_defense = data_teams_defense.copy()

    data_teams_defense['Squad'] = data_teams_defense['Squad'].str.replace(
        'vs ', '')

    # Attack
    new_df_attack = data_teams_attack[[
        'Squad', 'Poss', 'Gls90', 'Ast90', 'G-PK90']].copy()
    new_names = {'Poss': 'Passes tentées',
                 'Gls90': 'Buts marqués',
                 'Ast90': 'Passes décisives',
                 'G-PK90': 'Buts sans pénalité'}
    new_df_attack.rename(columns=new_names, inplace=True)
    new_df_attack['Passes tentées'] = new_df_attack['Passes tentées']/100
    new_df_attack['Attack_Sum'] = new_df_attack.iloc[:, 1:5].sum(axis=1)

    # Defense
    new_df_defense = data_teams_defense[[
        'Squad', 'Poss', 'Gls90', 'Ast90', 'G-PK90']].copy()
    new_names = {'Poss': 'Passes adverses tentées',
                 'Gls90': 'Buts reçus',
                 'Ast90': 'Passes décisives adverses',
                 'G-PK90': 'Buts sans pénalités reçus'}
    new_df_defense.rename(columns=new_names, inplace=True)
    new_df_defense['Passes adverses tentées'] = 1 - \
        new_df_attack['Passes tentées']/100
    new_df_defense['Buts reçus'] = new_df_defense['Buts reçus'].max(
    ) - new_df_defense['Buts reçus']
    new_df_defense['Passes décisives adverses'] = new_df_defense['Passes décisives adverses'].max(
    ) - new_df_defense['Passes décisives adverses']
    new_df_defense['Buts sans pénalités reçus'] = new_df_defense['Buts sans pénalités reçus'].max(
    ) - new_df_defense['Buts sans pénalités reçus']
    new_df_defense['Defense_Sum'] = new_df_defense.iloc[:, 1:5].sum(axis=1)

    # Merge
    merged_df = pd.merge(new_df_attack, new_df_defense, on='Squad')

    print(merged_df)

    return merged_df
