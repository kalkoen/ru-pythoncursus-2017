__author__ = 'guest148'

import random

def flip(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1, i, -1):
            val = array[j]
            valPrevious = array[j-1]
            if(valPrevious > val):
                flip(array, j, j-1)

array = [5, 2, 10, 9, 3, 4]
sort(array)
print(array)

def randomList(n):
    randoms = []
    for i in range(n):
        randoms.append(random.randrange(1000000))
    return randoms

array = randomList(1000000)
sort(array)
print(array)
