import Player


# function for iterating through spreadsheet row by row
def read_file():
  line = player_data.readline()
  for line in player_data:
    create_player(line)


# function for creating player from spreadsheet rows
def create_player(line):
  row = line.split(",")
  whole_name = row[1].split(" ")
  print(whole_name)


# file for reading and parsing spreadsheet
player_data = open("player_data.csv", "r")

# testing function
read_file()

player_data.close()