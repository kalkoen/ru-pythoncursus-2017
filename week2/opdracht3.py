for i in range(0, 100):
    text = str(i) + " "
    if(i % 3 == 0):
        text += "Fizz"
    if(i % 5 == 0):
        text += "Buzz"
    print(text)