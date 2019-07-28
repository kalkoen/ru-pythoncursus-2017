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

def triangle(a, b, ab, lineColor, fillColor):
    turtle.pendown()
    turtle.pencolor(lineColor)
    turtle.fillcolor(fillColor)
    turtle.begin_fill()

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
    turtle.left(180-a)

    turtle.end_fill()
    turtle.penup()

def triangleEquilateral(length, lineColor, fillColor):
    triangle(60, 60, length, lineColor, fillColor)

width = input("Geef een breedte in: ")
while not width.isnumeric():
    width = input("Geef een nummer in voor de breedte: ")
width = int(width)

lineWidth = input("Geef een lijnbreedte in: ")
while not lineWidth.isnumeric():
    lineWidth = input("Geef een nummer in voor de lijnbreedte: ")
lineWidth = int(lineWidth)

height = width/2*math.sqrt(3)

turtle.width(lineWidth)

triangleEquilateral(width, "red", "blue")
turtle.forward(width)
triangleEquilateral(width, "lime", "blue")
turtle.forward(width)
triangleEquilateral(width, "blue", "yellow")
turtle.left(180)
turtle.forward(width*1.5)
turtle.right(90)
turtle.forward(height)
turtle.right(90)
triangleEquilateral(width, "yellow", "yellow")
turtle.forward(width)
triangleEquilateral(width, "lime", "red")
turtle.left(180)
turtle.forward(width*0.5)
turtle.right(90)
turtle.forward(height)
turtle.right(90)
triangleEquilateral(width, "red", "lime")

turtle.done()