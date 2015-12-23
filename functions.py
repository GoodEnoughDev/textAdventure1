import os
import time
from classes import *
import math
import random


terrainTypes = ["forrest","plain","road","dessert","mountain"]

def clearConsole():
    os.system('clear')


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



def determineTerrain(player,worldMap):
    if (worldMap.size[player.positionx][player.positiony].type) == "":
        print("test")


def generateMap(size):
    size = int(size) * 10
    mapArray = list()
    for i in range(size):
        mapArray.append([])
        for i2 in range(size):
            mapArray[i].append(Terrain("Forest"))

    return mapArray

def randomValue(value):
    return 4 + (random.randrange(0,7) * math.sin(random.randrange(0,5) * value)) + (random.randrange(0,5) * math.sin(random.random() * value)) + (random.randrange(0,3) * math.sin(random.random() * value))


def realityLoop(player,worldMap):
    firstRun = False
    exit = False

    if firstRun == True:
        # first run conditions
        firstRun = False
    else:
        while exit == False:
            print("You are in a " + worldMap.array[player.position[0]][player.position[1]].type)
            determineCommand(player, input("Enter commands: "))

def determineCommand(player, string):
    words = string.upper()
    words = words.split()
    if words[0] == "GO":
        if words[1] == "NORTH":
            player.position[0] +=1
        elif words == "SOUTH":
            player.position[0] -=1
        elif words == "EAST":
            player.position[1] +=1
        elif words == "WEST":
            player.position[1] -=1
   # elif words[0] == ("quit" or "exit"):
        

