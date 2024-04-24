import numpy as np
import pandas as pd


def get_data(
    data_teams_attack: pd.DataFrame,
    data_players: pd.DataFrame,
    data_tournament: pd.DataFrame,
    data_teams_defense: pd.DataFrame,
) -> pd.DataFrame:

    all_teams = pd.concat([data_tournament["Team1"], data_tournament["Team2"]])
    unique_df = all_teams.drop_duplicates()
    unique_df_sorted = unique_df.sort_values()
    unique_df_sorted.reset_index(drop=True, inplace=True)

    return unique_df_sorted
