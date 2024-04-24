import numpy as np
import pandas as pd


def get_data(
    data_teams_attack: pd.DataFrame,
    data_players: pd.DataFrame,
    data_tournament: pd.DataFrame,
    data_teams_defense: pd.DataFrame,
) -> pd.DataFrame:

    data_tournament = data_tournament.copy()

    to_replace = {
        "Round of 16": 1,
        "Quarter-finals": 2,
        "Semi-finals": 3,
        "Third-place match": 3.5,
        "Final": 4,
    }

    data_tournament["Round"] = data_tournament["Round"].map(to_replace)
    new_df = data_tournament[["Round", "Team1", "Team2"]]
    team_df = new_df.melt(
        id_vars=["Round"], value_vars=["Team1", "Team2"], value_name="Team"
    )
    team_df.drop(columns=["variable"], inplace=True)
    team_df.sort_values(by="Round", inplace=True)
    team_df.reset_index(drop=True, inplace=True)
    max_round = team_df.groupby("Team")["Round"].max().reset_index()
    max_round.loc[max_round["Team"] == "Côte d'Ivoire", "Round"] = 5.0
    max_round = max_round.sort_values(by=["Round", "Team"]).reset_index(drop=True)

    return max_round
