import numpy as np
import pandas as pd

def get_data(data_teams_attack : pd.DataFrame, 
             data_players : pd.DataFrame, 
             data_tournament : pd.DataFrame, 
             data_teams_defense : pd.DataFrame) -> pd.DataFrame :

    data_teams_attack = data_teams_attack.copy()
    data_teams_defense = data_teams_defense.copy()

    data_teams_defense['Squad'] = data_teams_defense['Squad'].str.replace('vs ', '')
    
    # Attack
    new_df_attack = data_teams_attack[['Squad', 'Poss', 'Gls90', 'Ast90', 'G-PK90']].copy()
    new_names = {'Poss' : 'Attack_Poss',
                 'Gls90' : 'Attack_Goals',
                 'Ast90' : 'Attack_Assists',
                 'G-PK90' : 'Attack_Non_Penalty_Goals'}
    new_df_attack.rename(columns=new_names, inplace=True)
    new_df_attack['Attack_Poss'] = new_df_attack['Attack_Poss']/100
    new_df_attack['Attack_Sum'] = new_df_attack.iloc[:, 1:5].sum(axis=1)
    
    
    # Defense
    new_df_defense = data_teams_defense[['Squad', 'Poss', 'Gls90', 'Ast90', 'G-PK90']].copy()
    new_names = {'Poss' : 'Defense_Poss',
                 'Gls90' : 'Defense_Goals',
                 'Ast90' : 'Defense_Assists',
                 'G-PK90' : 'Defense_Non_Penalty_Goals'}
    new_df_defense.rename(columns=new_names, inplace=True)
    new_df_defense['Defense_Poss'] = (new_df_defense['Defense_Poss'].max() - new_df_defense['Defense_Poss'])/100
    new_df_defense['Defense_Goals'] = new_df_defense['Defense_Goals'].max() - new_df_defense['Defense_Goals']
    new_df_defense['Defense_Assists'] = new_df_defense['Defense_Assists'].max() - new_df_defense['Defense_Assists']
    new_df_defense['Defense_Non_Penalty_Goals'] = new_df_defense['Defense_Non_Penalty_Goals'].max() - new_df_defense['Defense_Non_Penalty_Goals']
    new_df_defense['Defense_Sum'] = new_df_defense.iloc[:, 1:5].sum(axis=1)
    
    # Merge
    merged_df = pd.merge(new_df_attack, new_df_defense, on='Squad')
    
    #print(merged_df)
    
    return merged_df