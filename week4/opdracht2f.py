__author__ = 'guest148'

import random
import time

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



def randomList(n):
    randoms = []
    for i in range(n):
        randoms.append(random.randrange(100000))
    return randoms

array = randomList(100000)
array = mergeSort(array)
print(array)

