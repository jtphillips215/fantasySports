import numpy as np
import pandas as pd


class Writers:
  def write_salary_file(df_player_data):
    df_player_data.to_csv('salary.csv')
    return
