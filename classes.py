
class Player:
    def __init__(self):
        self.name = str()
        self.weapon = str()
        self.items = []

class Item:
    def __init__(self):
        self.name = str()
        self.statAffected = str()
        self.value = int()

class Map:
    def __init__(self,size):
        self.size = size

class Terrain:
    def __init__(self):
        self.type = str()
        self.hidden = bool()
        self.treasure = Item


