# At start of game present user with main menu.

# Options will include start game and continue game. Continue will not be present if no map file exists.

# Start game will bring up player setup. Then move into the game loop.

# Continue will list the available map files. The file chosen will load and start the game loop.
#
#
#
#
#
#
#
#

from functions import *


player1,worldMap = mainMenu()
realityLoop(player1,worldMap)