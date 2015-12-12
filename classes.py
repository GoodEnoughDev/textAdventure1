
class Player:
    def __init__(self):
        self.name = str()
        self.weapon = str()
        self.items = []
        self.positionx = int()
        self.positiony = int()

    def move(self, direction):
        if direction.upper() == "N" or "NORTH":
            self.positiony +=1
        elif direction.upper() == "S" or "SOUTH":
            self.positiony -=1
        elif direction.upper() == "E" or "EAST":
            self.positionx +=1
        elif direction.upper() == "W" or "WEST":
            self.positionx -=1
        else:
            return 0

class Item:
    def __init__(self):
        self.name = str()
        self.statAffected = str()
        self.value = int()

class Map:
    def __init__(self):
        self.size = list()

class Terrain:
    def __init__(self):
        self.type = str()
        self.hidden = bool()
        self.treasure = Item


