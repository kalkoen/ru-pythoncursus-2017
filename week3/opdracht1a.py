__author__ = 'guest148'

import turtle

def square(width):
    for i in range(4):
        turtle.right(90)
        turtle.forward(width)

square(20)

turtle.done()