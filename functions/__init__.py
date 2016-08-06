# TODO: rearrange functions


import os
import time
from classes import *
import math
import random
import _pickle


def clear_console():
    os.system('clear')


def main_menu():
    print("Welcome to text adventure!\n\n\n")
    map_files = get_files()
    repeat = True
    while repeat:
        if map_files:
            msg = input("[S]tart game or [C]ontinue game?")
        else:
            msg = input("[S]tart game?")

        if msg.upper() == 'S':
            player1 = player_setup()
            world_map = Map()
            world_map.array = generate_map()
            return player1, world_map
            repeat = False
        elif msg.upper() == 'C':
            print(mapFiles)
            loadGame(input("Choose a map to load"))
            repeat = False
        else:
            repeat = True


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


def player_setup():
    player = Player()
    player.name = input("What is your name? ")
    player.weapon = input(player.name + ", what is your weapon of choice? ")
    player.position.append(3)
    player.position.append(3)
    return player

# TODO: move playerSetup() into player class


def generate_map():
    size = input("How large is your world? (on a scale from 1 to 10: ")
    size = int(size) * 10
    map_array = list()
    for i in range(size):
        map_array.append([])
        for i2 in range(size):
            map_array[i].append(Terrain("Forest"))
    return map_array


def random_value(value):
    # returns a sudo random value that follows a sine wave series in order to simulate a landscape.
    return 4 + (random.randrange(2, 7) * math.sin(random.randrange(0, 5) * value)) + (random.randrange(0, 5) * math.sin(random.random() * value)) + (random.randrange(0, 3) * math.sin(random.random() * value))


def determine_command(player, string, world_map, debug):
    words = string.upper()
    words = words.split()
    print(words)
    if words[0] == "GO":
        if words[1] in ('NORTH', 'N'):
            print('You have gone NORTH.')
            player.move_north(world_map)
            return False
        elif words[1] in ('SOUTH', 'S'):
            print('You have gone SOUTH')
            player.move_south(world_map)
            return False
        elif words[1] in ('EAST', 'E'):
            print('You have gone EAST')
            player.move_east(world_map)
            return False
        elif words[1] in ('WEST', 'W'):
            print('You have gone WEST')
            player.move_west(world_map)
            return False
        else:
            print("That is not a valid command")
    elif words[0] == "SAVE":
        save_game(world_map)
        if input("Continue? ").upper() == ("YES" or "Y"):
            return False
        else:
            return True
    elif words[0] in ('QUIT', 'EXIT'):
        return True
    else:
        print("That is not a valid command")
        return False


def save_game(map):
    msg = input("Input the name of your world: ")
    with open(msg + ".dat", "wb") as f:
        _pickle.dump(map, f)


def load_game(map_name):
    # TODO: fix this
    map = map_name + ".dat"
    print(map)
    with open(map, "wb") as f:
        _pickle.load(map, f)


def get_files():
    files = os.listdir(os.curdir)
    map_files = []
    for item in files:
        if item[-4:] == '.dat':
            map_files.append(item[:-4])
    return map_files