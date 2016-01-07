# At start of game present user with main menu.

# Options will include start game and continue game. Continue will not be present if no map file exists.

# Start game will bring up player setup. Then move into the game loop.

# Continue will list the available map files. The file chosen will load and start the game loop.


from functions import *

# intro()
player1, worldMap = mainMenu()

firstRun = True
exitGame = False
debug = True

if firstRun == True:
    # first run conditions
    firstRun = False
else:
    while exitGame == False:
        print("You are in a " + worldMap.array[player1.position[0]][player1.position[1]].type) if debug == True else False
        print(player1.position)
        exitGame = determineCommand(player1, input("Enter commands: "), worldMap, debug)

