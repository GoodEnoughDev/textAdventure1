import csv
import random
import math

map = list

def generateMap(size):
    mapArray = list()
    for i in range(size):
        mapArray.append([])
        for i2 in range(size):
            mapArray[i].append(int(randomValue(i+i2)))
    for j in range(10):
        for i in range(size):
            for i2 in range(size):
                if mapArray[i][i2] > 5:
                    mapArray[i][i2] = int(mapArray[i][i2]/ 2)

    return mapArray

def randomValue(value):
    return 4 + (random.randrange(0,7) * math.sin(random.randrange(0,5) * value)) + (random.randrange(0,5) * math.sin(random.random() * value)) + (random.randrange(0,3) * math.sin(random.random() * value))

map = generateMap(200)

with open('map.csv','w') as f:
    for sublist in map:
        for item in sublist:
            f.write(str(item) + ',')
        f.write('\n')

print(map)