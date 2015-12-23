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

    def move(self, direction):
        if direction.upper() == "N" or "NORTH":
            self.position[2] +=1
        elif direction.upper() == "S" or "SOUTH":
            self.position[2] -=1
        elif direction.upper() == "E" or "EAST":
            self.position[1] +=1
        elif direction.upper() == "W" or "WEST":
            self.position[1] -=1
        else:
            return 0



class NPC(Person):

    def __init__(self):
        self.messages = list

#############################related to items############################

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
    def __init__(self,type):
        self.type = type
        self.hidden = bool
        self.treasure = Item

#############################related to attacks############################
class Attack:
    def __init__(self):
        self.name = str
        self.description = str
        self.damage = int

