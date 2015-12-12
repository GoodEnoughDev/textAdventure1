from classes import Player

print("You are about to embark on an adventure!\n"
      "In text!\n\n")

player1 = Player(input("What is your name? "))

player1.weapon = input(player1.name + ", what is your weapon of choice? ")