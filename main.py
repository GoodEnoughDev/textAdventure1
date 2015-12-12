from classes import *
from functions import *
import time                     #required for sleep function


print("You are about to embark on an adventure!")
for i in range(5):
    print(".")
    time.sleep(1)

print("In text!\n\n")
time.sleep(5)
clearConsole()

print("Before you embark I need to know a little bit about you...")

player1 = Player(input("What is your name? "))
player1.weapon = input(player1.name + ", what is your weapon of choice? ")

input("")