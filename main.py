from functions import *

#intro()
player1 = playerSetup()
worldMap = Map()
worldMap.array = generateMap(input("How large is your world? (on a scale from 1 to 10: "))
realityLoop(player1,worldMap)