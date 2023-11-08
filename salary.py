from Player import Player


# function for iterating through spreadsheet row by row
def read_file():
  line = player_data.readline()
  for line in player_data:
    create_player(line)


# function for creating player from spreadsheet rows
def create_player(line):
  row = line.split(",")
  whole_name = row[1].split(" ")
  player = Player(whole_name[0], whole_name[1], row[7], row[10])
  print(player.first_name, player.last_name, player.avg_score, player.races)


# file for reading and parsing spreadsheet
player_data = open("player_data.csv", "r")

# testing function
read_file()

player_data.close()