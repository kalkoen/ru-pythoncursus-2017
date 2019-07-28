__author__ = 'guest148'
import turtle
import math

def isSquare(num):
    return math.sqrt(num).is_integer()

def digitArray(num):
    array = []
    if(num == 0): return [0]
    length = math.ceil(math.log10(abs(num)))
    for i in range(length):
        mod = num % 10
        array.append(mod)
        num -= mod
        num //= 10
    return array

def isPalindrome(num):
    array = digitArray(num)
    length = len(array)
    for i in range(int(length/2)):
        if(array[i] != array[length-i-1]): return False
    return True

def promptInteger(message, correctionMessage):
    value = input(message)
    while not value.isnumeric():
        value = input(correctionMessage)
    return int(value)

lowerBound = promptInteger("Vul een lowerbound in: ", "Voer een geldig nummer in voor de lowerbound: ")
upperBound = promptInteger("Vul een upperbound in: ", "Voer een geldig nummer in voor de upperbound: ")

n = upperBound - lowerBound
nboth = 0

for i in range(lowerBound, upperBound):
    s = str(i)
    square = isSquare(i)
    palindrome = isPalindrome(i)
    if(square): s+= " square"
    if(palindrome): s+= " palindrome"
    if(square and palindrome):
        s+= " !!"
        nboth += 1
    print(s)
print("Totaal:", nboth, "van de", n, "tussen", lowerBound, "en", upperBound)


#turtle.done()
