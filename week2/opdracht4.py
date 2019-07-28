print("Voer een getal in:")
x = input()
while not x.isnumeric():
    print("Voer een geldig getal in...")
    x = input()
x = int(x)

print("Voer een foutmarge in:")
errorMargin = float(input())

lowerBound = 0
upperBound = x

estimate = 0.5 * (upperBound + lowerBound)
while upperBound - lowerBound > errorMargin:
    estimateSquare = pow(estimate, 2)
    if estimateSquare > x:
        upperBound = estimate
    elif estimateSquare < x:
        lowerBound = estimate
    else:
        errorMargin = 0;
        break;
    estimate = 0.5 * (upperBound + lowerBound)

print("De wortel is", estimate, "met een foutmarge van", errorMargin)