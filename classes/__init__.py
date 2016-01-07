############################related to people############################
class Person(object):

    def __init__(self):
        self.name = str
        self.description = str
        self.isAlive = bool
        self.position = []
        self.attacks = list
        self.items = list
        self.hp = int
        self.mp = int
        self.strength = int
        self.defense = int

    def takeDamage(self, damage):
        self.hp -= damage

class Player(Person):

    def moveNorth(self, map):

        if self.position[0] == len(map.array):
            self.position[0] = self.position[0]
        else:
            self.position[0] += 1

    def moveSouth(self, map):

        if self.position[0] == 0:
            self.position[0] = self.position[0]
        else:
            self.position[0] -= 1
    def moveWest(self, map):

        if self.position[1] == 0:
            self.position[1] = self.position[1]
        else:
            self.position[1] -= 1
    def moveEast(self, map):
        if self.position[1] == len(map.array[0]):
            self.position[1] = self.position[1]
        else:
            self.position[1] += 1

class NPC(Person):

    def __init__(self):
        self.messages = list

##############related to items############################

class Item(object):

    def __init__(self):
        self.name = str
        self.description = str
        self.value = int

class Weapon(Item):

    def __init__(self):
        self.damage = int

class Map:
    def __init__(self):
        self.array = list

class Terrain:
    def __init__(self, type):
        self.type = type
        self.hidden = bool
        self.treasure = Item

#############################related to attacks############################
class Attack:
    def __init__(self):
        self.name = str
        self.description = str
        self.damage = int

# TODO: create a class to hold all relavent data for a given save file (EG. name of save file, path to save file, map array, and character data).
