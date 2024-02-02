# First we need to read in the input and parse each game to find the max
# count of each cube required. Each pull from the bag is separated by a ';' so
# we'll use the re.split function then iterate over each part of the tuple to
# find our local_max. From there it should be as simple as comparing each of
# our games counts to the red_max, blue_max, and green_max and finding which
# games are impossible. Similar to Day_1 we will use the main loop to keep
# track of our total and avoid needing to keep track of an array/index.

import datetime;

# Determine the local max for a given game.
def local_max(game):

# Determine if the local max is greater than any of red_max, blue_max, or
# green_max. If not the game_id, else return 0 so the count is not changed.
def valid_game_result(game):

def main():
    valid_game_sum = 0
    with open('input') as file:
        for game in file:
            valid_game_sum += valid_game_result(game)
    file.close()
    result=open("result.txt", "a")
    result.write(str(datetime.datetime.now()) + ": " + str(valid_game_sum) + "\n")
    result.close()

if __name__ == "__main__":
    main()
