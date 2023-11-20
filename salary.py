import numpy as np
import pandas as pd
import scipy.stats as stats


# reading player data from imported csv file
df_player_data = pd.read_csv('player_data.csv')
df_player_data.rename(columns={'FP/G': 'AVG'}, inplace=True)

# programatic access to average scores for drivers running full time
# 29 was minimum races of full time drivers in 2023
df_full_season = df_player_data[df_player_data["RC"] >= 29]

# adding percent rank and calculating new salary based on that pct rank
df_full_season['pct_rank'] = df_full_season.AVG.rank(pct = True)
df_full_season['new_sal'] = round(df_full_season.pct_rank * 28) + 7

# output salary file after calculations completed
df_full_season.to_csv('salary.csv')
