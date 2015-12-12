import os
import time

from classes import Player


def clearConsole():
    os.system('clear')


def intro():
    print("You are about to embark on an adventure!")
    for i in range(5):
        print(".")
        time.sleep(1)
    print("In text!")
    time.sleep(5)
    # TODO:fix clear console
    # clearConsole()
    print("\nBefore you embark I need to know a little bit about you...")


def playerSetup():
    player1 = Player()
    player1.name = input("What is your name? ")
    player1.weapon = input(player1.name + ", what is your weapon of choice? ")
    input("")