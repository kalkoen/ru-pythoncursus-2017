__author__ = 'guest148'

import turtle
import math


def ray(width, height):
    halfDiagonal = height*math.sqrt(2)/2
    turtle.forward(width)
    turtle.left(45)
    turtle.forward(halfDiagonal)
    turtle.left(90)
    turtle.forward(halfDiagonal)
    turtle.left(45)
    turtle.forward(width)

rays = input("Geef een aantal stralen in: ")
while not rays.isnumeric():
    rays = rays("Geef een nummer in voor het aantal stralen: ")
rays = int(rays)


turtle.pencolor("black")
turtle.fillcolor("yellow")

turtle.speed(100)

angle = 360 / rays

turtle.begin_fill()
for i in range(rays):
    ray(40, 10)
    turtle.right(180 - angle)
turtle.end_fill()

turtle.done()