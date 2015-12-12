import os
import time
import random
from classes import *

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
    player.weapon = input(player1.name + ", what is your weapon of choice? ")
    return player

def initializeWorld(size):
    worldMap = Map()
    for i in range(int(size)*10):
        worldMap.size.append([])
        for i2 in range(int(size)*10):
            worldMap.size[i].append(Terrain)
    return worldMap

# TODO: figure out how to determine terrain attributes

def realityLoop(player,worldMap):
    firstRun = True
    exit = False

    if firstRun == True:
        player.positionx = 10
        player.positiony = 10
    else:
        while exit == False:
            determineTerrain(player,worldMap)
            print("You are in a " + worldMap.size[player.positionx][player.positiony].type)

def determineTerrain(player,worldMap):
    if worldMap.size[player.positionx][player.positiony].type =="":
