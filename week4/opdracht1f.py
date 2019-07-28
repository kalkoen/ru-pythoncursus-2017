__author__ = 'guest148'

import matplotlib.pyplot as plt
from math import pi, sin
import numpy as np


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

coeffs = [0, 1]

xlist = np.arange(-10, 10, 0.1)
ylist = genPolynomial(coeffs, xlist)
derivative = genDerivative(coeffs)
ylistDerivative = genPolynomial(derivative, xlist)

plt.plot(xlist, ylist)
plt.plot(xlist, ylistDerivative)
plt.show()