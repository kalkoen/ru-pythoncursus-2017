import turtle

turtle.pendown()

rules = [ ["X", "X+YF++YF-FX--FXFX-YF+"],
          ["Y", "-FX+YFYF++YF+FX--FX-Y"]]

angle = 45
length = 10
depth = 5
start = "X"

def rewrite(S):
    result = ""
    for i in range(len(S)):
        result += resultAddition(S[i])
    return result

def resultAddition(C):
    for r in range(len(rules)):
        rChar = rules[r][0]
        rReplace = rules[r][1]
        if(C == rChar):
            return rReplace
    return C

def rewriteDepth(S, depth):
    result = S
    for i in range(depth):
        result = rewrite(result)
    return result

def draw(S):
    for i in range(len(S)):
        char = S[i]
        if(char == "F"):
            turtle.forward(length)
        elif(char == "-"):
            turtle.left(angle)
        elif(char == "+"):
            turtle.right(angle)

turtle.speed(0)
turtle.delay(0.1)
turtle.screensize(5000, 5000)

end = rewriteDepth(start, depth)
print(end)
draw(end)


turtle.done()
