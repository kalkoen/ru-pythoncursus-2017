__author__ = 'guest148'

import matplotlib.pyplot as plt
from math import pi, sin
from numpy import arange

def getSin(xlist):
    ylist = []
    for i in range(len(xlist)):
        ylist += [sin(xlist[i])]
    return ylist

xlist = arange(0, 2*pi, 0.1)
ylist = getSin(xlist)

plt.plot(xlist, ylist)
plt.show()