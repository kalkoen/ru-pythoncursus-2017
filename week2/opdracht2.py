__author__ = 'guest148'

print("Voer het aantal iteraties in:")
iterations = input()
while (not iterations.isnumeric()):
    print("Voer een geldig getal in...")
    iterations = input()
iterations = int(iterations)

a = 0
b = 1
print(a)
print(b)
for i in range(2, iterations):
    # current = a + b
    # a = b
    # b = current
    b += a
    a = b - a
    print(b)

ratio = b / a

print("De ratio bij", iterations, "iteraties is:", ratio);
