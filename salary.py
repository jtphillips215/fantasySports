from Player import Player


# function for iterating through spreadsheet row by row and appending data to list of players
def read_file():
  line = player_data.readline()
  for line in player_data:
    player = create_player(line)
    players.append(player)


# function for creating player from spreadsheet rows
def create_player(line):
  row = line.split(",")
  whole_name = row[1].strip().split(" ")
  player = Player(whole_name[0], whole_name[1], float(row[7].strip('\"')), int(row[10].strip('\"')))
  return player


# file for reading and parsing spreadsheet
player_data = open("player_data.csv", "r")

# creating list of players and calling function to generate that list by reading through file
players = []
read_file()

player_data.close()