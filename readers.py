import numpy as np
import pandas as pd

class Readers:
  def read_player_data():
    df_player_data = pd.read_csv('player_data.csv')
    return df_player_data
    