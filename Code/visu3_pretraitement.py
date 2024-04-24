import numpy as np
import pandas as pd

# On récupère simplement les données du tournoi pour la préparation de la visualisation 3  
def get_data(
    data_teams_attack: pd.DataFrame,
    data_players: pd.DataFrame,
    data_tournament: pd.DataFrame,
    data_teams_defense: pd.DataFrame,
) -> list[pd.DataFrame]:

    data_players = data_players.copy()
    data_tournament = data_tournament.copy()

    # Performance des équipes
    to_replace = {
        "Round of 16": 1,
        "Quarter-finals": 2,
        "Semi-finals": 3,
        "Third-place match": 3.5,
        "Final": 4,
    }
    
    # Remplacer les valeurs de la colonne 'Round' par des valeurs numériques
    data_tournament["Round"] = data_tournament["Round"].map(to_replace)
    new_df = data_tournament[["Round", "Team1", "Team2"]]
    team_df = new_df.melt(
        id_vars=["Round"], value_vars=["Team1", "Team2"], value_name="Team"
    )
    
    # Supprimer la colonne 'variable', trier les valeurs par 'Round' et réinitialiser l'index
    team_df.drop(columns=["variable"], inplace=True)
    team_df.sort_values(by="Round", inplace=True)
    team_df.reset_index(drop=True, inplace=True)
    max_round = team_df.groupby("Team")["Round"].max().reset_index()
    max_round.loc[max_round["Team"] == "Côte d'Ivoire", "Round"] = 5.0
    max_round = max_round.sort_values(by=["Round", "Team"]).reset_index(drop=True)

    # Préparation des données des joueurs
    new_df_player = data_players[
        ["Player", "Pos", "Squad", "Age", "MP", "Min", "Gls90", "Ast90", "G-PK90"]
    ].copy()
    new_df_player["Fatigue"] = new_df_player["Min"] / new_df_player["MP"]
    new_df_player["Score"] = (
        new_df_player["Gls90"] + new_df_player["Ast90"] + new_df_player["G-PK90"]
    )
    new_df_player.drop(["Gls90", "Ast90", "G-PK90"], axis=1, inplace=True)

    # On merge les datasets et on remplace les valeurs infinies par des NaN
    merged_df = pd.merge(
        new_df_player, max_round, left_on="Squad", right_on="Team", how="outer"
    )
    merged_df.drop("Team", axis=1, inplace=True)
    merged_df.fillna(0.0, inplace=True)

    # Ajout des données pour les matchs (équipes adverses)
    adv = pd.concat(
        [
            data_tournament,
            data_tournament.rename(columns={"Team1": "Team2", "Team2": "Team1"}),
        ],
        ignore_index=True,
    )[["Round", "Team1", "Team2"]].sort_values(by="Round")

    return [merged_df, adv]
