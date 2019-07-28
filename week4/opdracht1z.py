__author__ = 'guest148'

import matplotlib.pyplot as plt
from math import pi, sin
import numpy as np

coeffs = [9, 6, 1]

def calcY(coeffs, x):
    y = 0;
    for i in range(len(coeffs)):
        y += coeffs[i] * x**i
    return y

def genPolynomial(coeffs, xlist):
    ylist = []
    for i in range(len(xlist)):
        ylist += [calcY(coeffs, xlist[i])]
    return ylist

def genDerivative(coeffs):
    derivative = []
    for i in range(1, len(coeffs)):
        derivative += [coeffs[i]*i]
    return derivative

def coolFunction(x):
    return calcY(coeffs, x)

def genFunction(function, xlist):
    ylist = []
    for i in range(len(xlist)):
        ylist += [function(xlist[i])]
    return ylist

def genDerivativeApproximation(function, xlist, margin):
    ylist = []
    for i in range(len(xlist)):
        x = xlist[i]
        xBefore = function(x-margin/2)
        xAfter = function(x+margin/2)

        ylist += [(xAfter-xBefore)/margin]
    return ylist

xlist = np.arange(-10, 10, 0.1)
ylist = genFunction(sin, xlist)

ylistDerivative = genDerivativeApproximation(sin, xlist, 0.0001)

plt.plot(xlist, ylist)
plt.plot(xlist, ylistDerivative)
plt.grid(True)
plt.show()