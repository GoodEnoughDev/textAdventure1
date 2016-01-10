# At start of game present user with main menu.

# Options will include start game and continue game. Continue will not be present if no map file exists.

# Start game will bring up player setup. Then move into the game loop.

# Continue will list the available map files. The file chosen will load and start the game loop.


from functions import *

# intro()
player1, world_map = main_menu()

firstRun = False
exitGame = False
debug = True

if firstRun:
    # first run conditions
    firstRun = False
else:
    while not exitGame:
        print("You are in a " + world_map.array[player1.position[0]][player1.position[1]].type) if debug else False
        print(player1.position)
        exitGame = determine_command(player1, input("Enter commands: "), world_map, debug)

