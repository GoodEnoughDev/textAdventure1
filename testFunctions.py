import csv
import random
import math

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

print(numbers(42))