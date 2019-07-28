__author__ = 'guest148'


euros = 6
cents = 10

print("Voer een aantal euros in:")


userEuros = input()
while(not userEuros.isnumeric()):
    print("Voer een geldig aantal euro's in!..")
    userEuros = input()

userEuros = int(userEuros)
print("Voer het aantal centen in:")
centsInput = input()
while (not centsInput.is()):
    print("Voer een geldig aantal centen in in!..")
    centsInput = input()

userCents = int(centsInput[0:2])
if(len(centsInput) >= 3 and int(centsInput[2]) >= 5):
    userCents += 1
print("Jouw getal: €" + str(userEuros) + "." + str(userCents))

sumEuros = euros + userEuros
sumCents = cents + userCents

if(sumCents > 100):
    sumCents-=100
    sumEuros+=1

if(sumCents < 10):
    sumCents = "0" + str(sumCents)

print("Som: €" + str(sumEuros) + "." + str(sumCents))

