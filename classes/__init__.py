############################related to people############################


# noinspection PyPep8Naming
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


class Enemy(object):
    def __init__(self):
        self.name = str
        self.description = str
        self.isAlive = bool
        self.attacks = list
        self.items = list
        self.hp = int
        self.mp = int
        self.strength = int
        self.defense = int

    def take_damage(self, damage):
        self.hp -= damage


# noinspection PyPep8Nami ng
class Player(Person):

    def move_north(self, map):

        if self.position[0] == len(map.array):
            self.position[0] = self.position[0]
        else:
            self.position[0] += 1

    def move_south(self, map):

        if self.position[0] == 0:
            self.position[0] = self.position[0]
        else:
            self.position[0] -= 1

    def move_west(self, map):

        if self.position[1] == 0:
            self.position[1] = self.position[1]
        else:
            self.position[1] -= 1

    def move_east(self, map):
        if self.position[1] == len(map.array[0]):
            self.position[1] = self.position[1]
        else:
            self.position[1] += 1


class NPC(Person):

    def __init__(self):
        super().__init__()
        self.messages = list

##############related to items############################


class Item(object):

    def __init__(self):
        self.name = str
        self.description = str
        self.value = int


class Weapon(Item):

    def __init__(self):
        super().__init__()
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
class SaveFile:
    def __init__(self,name, player, world):
        name = name
        path = str
        player = player
        world = world


