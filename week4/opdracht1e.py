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

coeffs = [3, 3, 4, 0.2]

xlist = np.arange(-40, 30, 0.1)
ylist = genPolynomial(coeffs, xlist)

plt.plot(xlist, ylist)
plt.show()