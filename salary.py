import numpy as np
import scipy.stats as stats
from Player import Player
from Readers import Readers

player_data = Readers.read_player_data()

"""
# function for iterating through spreadsheet row by row and appending data to list of players
def read_file():
  line = player_data.readline()
  for line in player_data:
    player = create_player(line)
    players.append(player)


# function for creating player from spreadsheet rows
def create_player(line):
  row = line.split(",")
  whole_name = row[1].strip('\"').split(" ")
  
  if whole_name[1] == 'Hunter':
    whole_name[0] = 'John Hunter'
    whole_name[1] = "Nemechek"
  
  if whole_name[1] == 'van':
    whole_name[1] = 'van Gisbergen'

  player = Player(whole_name[0], whole_name[1], float(row[7].strip('\"')), int(row[10].strip('\"')))
  return player


# file for reading and parsing spreadsheet
player_data = open('player_data.csv', 'r')

# creating list of players and calling function to generate that list by reading through file
players = []
read_file()

# closing the source file
player_data.close()

# creating the output file and writing to it
salary = open('salary.csv', 'w')

salary.write('First Name,Last Name,Average,Races\n')
for player in players:
  salary.write(f'{player.first_name},{player.last_name},{player.avg_score},{player.races}\n')

salary.close()
"""
