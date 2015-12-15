import csv
import random
import math

map = list

def generateMap(size):
    mapArray = list()
    for i in range(size):
        mapArray.append([])
        for i2 in range(size):
            mapArray[i].append(int(randomValue(i2)))
    return mapArray

def randomValue(previousValue):
    return random.gauss((previousValue * random.random()),random.random())

map = generateMap(20)

with open('map.csv','w') as f:
    for sublist in map:
        for item in sublist:
            f.write(str(item) + ',')
        f.write('\n')

print(map)