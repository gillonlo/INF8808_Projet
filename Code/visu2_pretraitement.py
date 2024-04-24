import numpy as np
import pandas as pd

# On récupère simplement les données du tournoi pour la préparation de la visualisation 2
def get_data(
    data_teams_attack: pd.DataFrame,
    data_players: pd.DataFrame,
    data_tournament: pd.DataFrame,
    data_teams_defense: pd.DataFrame,
) -> pd.DataFrame:

    data_teams_attack = data_teams_attack.copy()
    data_teams_defense = data_teams_defense.copy()

    data_teams_defense["Squad"] = data_teams_defense["Squad"].str.replace("vs ", "")

    # Données offensives
    new_df_attack = data_teams_attack[
        ["Squad", "Poss", "Gls90", "Ast90", "G-PK90"]
    ].copy()
    new_names = {
        "Poss": "Possession",
        "Gls90": "Buts marqués",
        "Ast90": "Passes décisives",
        "G-PK90": "Buts hors pénalty",
    }
    # On renomme les colonnes pour plus de clarté et on normalise la colonne 'Possession'
    new_df_attack.rename(columns=new_names, inplace=True)
    new_df_attack["Possession"] = (
        new_df_attack["Possession"] / (new_df_attack["Possession"].max())
    ) * 2.5
    new_df_attack["Attack_Sum"] = new_df_attack.iloc[:, 1:5].sum(axis=1)



    # Données défensives
    new_df_defense = data_teams_defense[
        ["Squad", "Poss", "Gls90", "Ast90", "G-PK90"]
    ].copy()
    new_names = {
        "Poss": "Possession moy",
        "Gls90": "Buts non reçus",
        "Ast90": "Passes adv. contrées",
        "G-PK90": "Buts hors pénalty non reçus",
    }
    # On renomme les colonnes pour plus de clarté et on normalise les colonnes 
    new_df_defense.rename(columns=new_names, inplace=True)
    new_df_defense["Possession moy"] = new_df_attack["Possession"]
    new_df_defense["Buts non reçus"] = (
        new_df_defense["Buts non reçus"].max() - new_df_defense["Buts non reçus"]
    )
    new_df_defense["Passes adv. contrées"] = (
        new_df_defense["Passes adv. contrées"].max()
        - new_df_defense["Passes adv. contrées"]
    )
    new_df_defense["Buts hors pénalty non reçus"] = (
        new_df_defense["Buts hors pénalty non reçus"].max()
        - new_df_defense["Buts hors pénalty non reçus"]
    )
    new_df_defense["Defense_Sum"] = new_df_defense.iloc[:, 1:5].sum(axis=1)


    # On va fusionner les deux dataframes (offensif et défensif)
    merged_df = pd.merge(new_df_attack, new_df_defense, on="Squad")

    return merged_df
