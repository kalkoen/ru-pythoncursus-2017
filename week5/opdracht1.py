import turtle

turtle.pendown()

replaceChar = "F"
replaceRule = "F-F++F+F-F-F"

angle = 72
length = 10
depth = 1
start = "F-F-F-F-F"

def rewrite(S):
    result = ""
    for i in range(len(S)):
        char = S[i]
        if(char == replaceChar):
            result += replaceRule
        else:
            result += char
    return result

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

#turtle.speed(0)
#turtle.delay(0)

end = rewriteDepth(start, depth)
print(end)
draw(end)


turtle.done()
