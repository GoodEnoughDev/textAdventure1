#TODO: rearrange functions

import os
import time
from classes import *
import math
import random
import _pickle


def clearConsole():
    os.system('clear')

def mainMenu():
    print("Welcome to text adventure!\n\n\n")
    mapFiles = getFiles()
    repeat = True
    while repeat:
        if mapFiles:
            msg = input("[S]tart game or [C]ontinue game?")
        else:
            msg = input("[S]tart game?")

        if msg.upper() == 'S':
            player1 = playerSetup()
            worldMap = Map()
            worldMap.array = generateMap()
            return player1,worldMap
            repeat = False
        elif msg.upper() == 'C':
            print(mapFiles)
            loadGame(input("Choose a map to load"))
            repeat = False
        else:
            repeat == True

# initialize world
def intro():
    print("You are about to embark on an adventure!")
    for i in range(5):
        print(".")
        time.sleep(1)
    print("In text!")
    time.sleep(2)
    # TODO:fix clear console
    # clearConsole()
    print("\nBefore you embark I need to know a little bit about you...")


def playerSetup():
    player = Player()
    player.name = input("What is your name? ")
    player.weapon = input(player.name + ", what is your weapon of choice? ")
    player.position.append(3)
    player.position.append(3)
    return player



#def determineTerrain(player,worldMap):
#    if (worldMap.size[player.positionx][player.positiony].type) == "":
#        print("test")


def generateMap():
    size = input("How large is your world? (on a scale from 1 to 10: ")
    size = int(size) * 10
    mapArray = list()
    for i in range(size):
        mapArray.append([])
        for i2 in range(size):
            mapArray[i].append(Terrain("Forest"))

    return mapArray

def randomValue(value):
    return 4 + (random.randrange(2,7) * math.sin(random.randrange(0,5) * value)) + (random.randrange(0,5) * math.sin(random.random() * value)) + (random.randrange(0,3) * math.sin(random.random() * value))

#TODO: Possibly move this to the main file
def realityLoop(player,worldMap):
    firstRun = False
    exit = False

    if firstRun == True:
        # first run conditions
        firstRun = False
    else:
        while exit == False:
            print("You are in a " + worldMap.array[player.position[0]][player.position[1]].type)
            print(player.position)
            exit = determineCommand(player, input("Enter commands: "),worldMap)
            print(exit)

def determineCommand(player, string, worldMap,debug):
    words = string.upper()
    words = words.split()
    print(words)
    if words[0] == "GO":
        if words[1] == "NORTH":
            player.moveNorth(worldMap)
            return False
        elif words[1] == "SOUTH":
            player.moveSouth(worldMap)
            return False
        elif words[1] == "EAST":
            player.moveEast(worldMap)
            return False
        elif words[1] == "WEST":
            player.moveWest(worldMap)
            return False
        else:
            print("That is not a valid command")
    elif words[0] == "SAVE":
        saveGame(worldMap)
        if input("Continue? ").upper() == ("YES" or "Y"):
            return False
        else:
            return True
    elif words[0] == ("QUIT" or "EXIT"):
        return True
    else:
        print("That is not a valid command")
        return False

#TODO: finish save and load function
def saveGame(map):
    msg = input("Input the name of your world: ")
    with open(msg + ".dat", "wb") as f:
        _pickle.dump(map, f)


def loadGame(mapName):
    map = mapName + ".dat"
    print(map)
    with open(map, "wb") as f:
        _pickle.load(map, f)

def getFiles():
    files = os.listdir(os.curdir)
    mapFiles = []
    for item in files:
        if item[-4:] == '.dat':
            mapFiles.append(item[:-4])
    return mapFiles
