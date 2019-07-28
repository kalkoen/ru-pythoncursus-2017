__author__ = 'guest148'

import random
import turtle
import math

def gallow(width):
    turtle.width(3)
    turtle.left(180)
    turtle.pendown()
    turtle.pencolor("darkred")
    turtle.forward(width)
    turtle.penup()
    turtle.left(180)
    turtle.left(90)
    yield
    turtle.pendown()
    turtle.forward(width*1.5)
    turtle.penup()
    yield
    turtle.left(180)
    turtle.forward(width*1.5)
    turtle.left(90)
    turtle.forward(width*0.3)
    turtle.left(135)
    turtle.pendown()
    turtle.forward(width*0.3*math.sqrt(2))
    turtle.penup()
    turtle.right(45)
    turtle.forward(width*0.7)
    turtle.right(90)
    yield
    turtle.pendown()
    turtle.forward(width*0.6)
    turtle.penup()
    turtle.right(90)
    yield
    turtle.pendown()
    turtle.forward(width * 0.15)
    turtle.penup()
    yield
    turtle.width(1)
    turtle.pencolor("black")
    turtle.forward(width * 0.1)
    turtle.pendown()
    turtle.circle(width * 0.05)
    turtle.penup()
    turtle.forward(width * 0.05)
    yield
    turtle.left(190)
    turtle.pendown()
    turtle.forward(width * 0.10)
    turtle.penup()
    turtle.right(180)
    turtle.forward(width*0.10)
    turtle.left(20)
    yield
    turtle.pendown()
    turtle.forward(width * 0.10)
    turtle.penup()
    turtle.left(180)
    turtle.forward(width * 0.10)
    turtle.left(80)
    yield
    turtle.pendown()
    turtle.forward(width * 0.12)
    turtle.penup()
    yield
    turtle.left(20)
    turtle.pendown()
    turtle.forward(width * 0.15)
    turtle.penup()
    turtle.left(180)
    turtle.forward(width * 0.15)
    turtle.left(320)
    yield
    turtle.forward(width * 0.15)

def promptUniqueCharacter(excludeArray, message, correctionMessage, duplicateMessage):
    value = input(message)
    while True:
        if(len(value) > 1):
            value = input(correctionMessage)
        elif (value in excludeArray):
            value = input(duplicateMessage)
        else: break
    return value

def indexesOf(c, string):
    indexes = []
    for i in range(len(string)):
        if(string[i] == c): indexes.append(i)
    return indexes

def replace(word, n, c):
    s = list(word)
    s[n] = c
    return "".join(s)

triesLeft = 11

file = open("woordenlijst.txt")
words = file.read().splitlines()
correctWord = random.choice(words)

guessedWord = ""
for i in range(len(correctWord)):
    guessedWord += "."
guessedLetters = []

#0 = playing, means lost if while is over, 1 = won
gameState = 0

generator = gallow(200)
while triesLeft > 0 and gameState == 0:
    print("Je hebt", triesLeft, "kansen over. Tot nu toe is het woord:", guessedWord)
    print("Geprobeerde letters:", ", ".join(guessedLetters))
    letter = promptUniqueCharacter(guessedLetters, "Vul een letter in: ", "Vul 1 letter in: ", "Deze letter heb je al geprobeerd, probeer een andere: ")
    guessedLetters.append(letter)
    if letter in correctWord:
        indexes = indexesOf(letter, correctWord)
        for index in indexes:
            guessedWord = replace(guessedWord, index, letter)
        print("Hij zit erin!")
    else:
        triesLeft-=1
        print("Helaas, hij zit er niet in")
        next(generator)

    if(guessedWord == correctWord):
        gameState = 1

if(gameState == 1):
    print("Gefeliciteerd, het woord was", correctWord)
else:
    print("Helaas! Het correcte woord was", correctWord)