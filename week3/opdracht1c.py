__author__ = 'guest148'

import turtle
import math

def getcolor(dutch):
    if(dutch == "geel"):
        return "yellow"
    elif(dutch == "groen"):
        return "green"
    elif(dutch == "rood"):
        return "red"
    elif(dutch == "blauw"):
        return "blue"
    elif(dutch == "paars"):
        return "purple"
    else: return None

def square(width):
    for i in range(4):
        turtle.right(90)
        turtle.forward(width)

def triangle(a, b, ab):
    pos = turtle.position()
    c = 180 - a - b
    bc = ab * math.sin(a) / math.sin(c)
    ac = ab * math.sin(b) / math.sin(a)
    turtle.forward(ab)
    turtle.left(180 - b)
    turtle.forward(bc)
    turtle.left(180 - c)
    turtle.forward(ac)
    turtle.setposition(pos)

def triangleEquilateral(length):
    triangle(60, 60, length)

width = input("Geef een breedte in: ")
while not width.isnumeric():
    width = input("Geef een nummer in voor de breedte: ")
width = int(width);


turtle.pencolor("red")
turtle.fillcolor("red")
turtle.begin_fill()
triangleEquilateral(width)
turtle.end_fill()

turtle.done()