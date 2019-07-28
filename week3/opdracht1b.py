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

width = input("Geef een breedte in: ")
while not width.isnumeric():
    width = input("Geef een nummer in voor de breedte: ")
width = int(width);

lineColor = getcolor(input("Geef een lijnkleur in: "))
while(lineColor == None):
    lineColor = getcolor(input("Geef een ondersteunde lijnkleur in in: "))

fillColor = getcolor(input("Geef een vulkleur in: "))
while(fillColor == None):
    fillColor = getcolor(input("Geef een ondersteunde vulkleur in in: "))


turtle.pencolor(lineColor)
turtle.fillcolor(fillColor)
turtle.begin_fill()
square(width)
turtle.end_fill()

turtle.done()