import csv
import random
import math
import os

#map = list


#map = generateMap(200)

#with open('map.csv','w') as f:
#    for sublist in map:
#        for item in sublist:
#            f.write(str(item) + ',')
#        f.write('\n')

def numbers(n):
    for i in range(2,1000):
        if isPal(convertBase(n,i)):
            return i

def convertBase(number,base):
    num = number
    numString = ""
    while (num > base):
        numString = str(num % base) + numString
        num = int(num/base)
    numString = str(num) + numString
    return numString

def isPal(number):
    for i in range(len(number)):
        if number[0] == number[i]:
            return True
        else:
            return False

#print(numbers(42))

def getFiles():
    files = os.listdir(os.curdir)
    mapFiles = []
    for item in files:
        if item[-4:] == '.dat':
            mapFiles.append(item[:-4])
    return mapFiles

def generate_map():
    size = input("How large is your world? (on a scale from 1 to 10: ")
    size = int(size) * 10
    map_array = list()
    for i in range(size):
        map_array.append([])
        for i2 in range(size):
            map_array[i].append(Terrain("Forest"))
    return map_array


def random_value(value):
    # returns a sudo random value that follows a sine wave series in order to simulate a landscape.
    return 4 + (random.randrange(2, 7) * math.sin(random.randrange(0, 5) * value)) + (random.randrange(0, 5) * math.sin(random.random() * value)) + (random.randrange(0, 3) * math.sin(random.random() * value))