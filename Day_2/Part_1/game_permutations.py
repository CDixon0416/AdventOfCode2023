# First we need to read in the input and parse each game to find the max
# count of each cube required. Each pull from the bag is separated by a ';' so
# we'll use the re.split function then iterate over each part of the tuple to
# find our local_max. From there it should be as simple as comparing each of
# our games counts to the red_max, blue_max, and green_max and finding which
# games are impossible. Similar to Day_1 we will use the main loop to keep
# track of our total and avoid needing to keep track of an array/index.

import datetime;
import re;

# Determine the local max for a given game.
def local_max(game, log):
    red_local_max = 0
    green_local_max = 0
    blue_local_max = 0

    color_regex = re.findall("[0-9]+\\sred|[0-9]+\\sblue|[0-9]+\\sgreen", game)
    for color in color_regex:
        if color[-1] == "d":
            value = re.findall("[0-9]+", color)
            if int(value[0]) > int(red_local_max):
                log.write("\tred_local_max changed from " + str(red_local_max) + " to " + value[0] + "\n")
                red_local_max = int(value[0])
        elif color[-1] == "e":
            value = re.findall("[0-9]+", color)
            if int(value[0]) > int(blue_local_max):
                log.write("\tblue_local_max changed from " + str(blue_local_max) + " to " + value[0] + "\n")
                blue_local_max = int(value[0])
        # Assume green, probably needs a base case but that's for the next guy.
        else:
            value = re.findall("[0-9]+", color)
            if int(value[0]) > int(green_local_max):
                log.write("\tgreen_local_max changed from " + str(green_local_max) + " to " + value[0] + "\n")
                green_local_max = int(value[0])
    log.write("\t\tlocal_max_tuple set to: " + str([red_local_max, blue_local_max, green_local_max]) + "\n")
    return [red_local_max, blue_local_max, green_local_max]

# Determine if the local max is greater than any of red_max, blue_max, or
# green_max. If not the game_id, else return 0 so the count is not changed.
def valid_game_result(game, log):
    game_id = re.findall("[0-9]+", game)
    log.write("Beginning analysis of Game " + game_id[0] + ":\n")

    max_tuple = [12, 14, 13]
    local_max_tuple = local_max(game, log)

    log.write("\t\tIs it smaller than max_tuple?: " + str(max_tuple) + "\n")

    if local_max_tuple[0] < max_tuple[0] and local_max_tuple[1] < max_tuple[1] and local_max_tuple[2] < max_tuple[2]:
        log.write("\t" + game_id[0] + " is a valid game.\n")
        return game_id[0]
    else:
        log.write("\t" + game_id[0] + " is NOT a valid game.\n")
        return 0

def main():
    valid_game_sum = 0
    log=open("audit_log.txt", "a")
    log.write(str(datetime.datetime.now()) + "\n")

    with open('input') as file:
        for game in file:
            valid_game_sum += int(valid_game_result(game, log))

    file.close()
    result=open("result.txt", "a")
    result.write(str(datetime.datetime.now()) + ": " + str(valid_game_sum) + "\n")
    result.close()
    log.close()


if __name__ == "__main__":
    main()
