__author__ = 'guest148'

import random
import time
import matplotlib.pyplot as plt
from math import pi, sin
import numpy as np

def mergeSorted(array1, array2):
    sorted = []
    comparisonIndex = 0
    comparisonVal = array2[comparisonIndex]
    lengthArray2 = len(array2)
    for i in range(len(array1)):
        val = array1[i]
        while(comparisonIndex < lengthArray2 and comparisonVal < val):
            sorted.append(comparisonVal)
            comparisonIndex += 1
            if(comparisonIndex < lengthArray2):
                comparisonVal = array2[comparisonIndex]
        sorted.append(val)
    if comparisonIndex <lengthArray2 :
        for i in range(comparisonIndex, lengthArray2):
            sorted.append(array2[comparisonIndex])
    return sorted

def mergeSort(array):
    length = len(array)
    if(length <= 1):
        return array
    middle = int(length/2)
    firstHalf = array[:middle]
    secondHalf = array[middle:]
    firstHalf = mergeSort(firstHalf)
    secondHalf = mergeSort(secondHalf)
    #print(array)
    #print(firstHalf)
    #print(secondHalf)
    return mergeSorted(firstHalf, secondHalf)

def flip(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1, i, -1):
            val = array[j]
            valPrevious = array[j-1]
            if(valPrevious > val):
                flip(array, j, j-1)

def randomList(n):
    randoms = []
    for i in range(n):
        randoms.append(random.randrange(100000))
    return randoms

def testBubble(n):
    array = randomList(n)
    t = time.time()
    bubbleSort(array)

    return time.time() - t

def testMerge(n):
    array = randomList(n)
    t = time.time()
    mergeSort(array)

    return time.time() - t

def genFunction(function, xlist):
    ylist = []
    for i in range(len(xlist)):
        ylist += [function(xlist[i])]
    return ylist

xlist = [1, 5, 10, 20, 50, 100, 500, 1000, 2500, 5000, 10000]
ylistBubble = genFunction(testBubble, xlist)
ylistMerge = genFunction(testMerge, xlist)

plt.plot(xlist, ylistBubble)
plt.plot(xlist, ylistMerge)

plt.grid(True)
plt.show()
