__author__ = 'guest148'

import matplotlib.pyplot as plt
from math import pi, sin
import numpy as np

def calculateTopX(a, b, c):
    return -b/(2*a)


def calculateTopY(a, b, c):
    x = calculateTopX(a, b, c)
    return calcY(a, b, c, x)

def calcY(a, b, c, x):
    return a * x**2 + b * x + c

def genParabola(a, b, c, xlist):
    ylist = []
    for i in range(len(xlist)):
        ylist += [calcY(a, b, c, xlist[i])]
    return ylist

def genTopLine(a, b, c, xlist):
    ylist = []
    for i in range(len(xlist)):
        ylist += [calculateTopY(a, b, c)]
    return ylist

a = 1
b = 3
c = -9

xlist = np.arange(-10, 10, 0.1)
ylist = genParabola(a, b, c, xlist)
topYList = genTopLine(a, b, c, xlist)

plt.plot(xlist, ylist)
plt.plot(xlist, topYList)
plt.show()