__author__ = 'guest148'

import time

print("Voer een getal in: ", end="")
number = int(input())
print(number, "= ", end="")

beginTime = time.time()

x = 2
while x < number/2:
    if number % x == 0:
        print(x, "* ", end="")
        number //= x
    #    x = 2
    else:
        x += 1

endTime = time.time()
duration = endTime - beginTime

print(number)
print("Deze bereking duurde", duration, "seconden")
