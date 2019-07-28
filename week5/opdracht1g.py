import turtle

fileName = "ihavenolife2.lst"


rules = []
angle = 0
length = 0
depth = 0
start = ""

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


stackPosition = []
stackHeading = []
def draw(S):
    for i in range(len(S)):
        char = S[i]
        if(char == "F"):
            turtle.forward(length)
        elif(char == "-"):
            turtle.left(angle)
        elif(char == "+"):
            turtle.right(angle)
        elif(char == "["):
            stackPosition.append(turtle.position())
            stackHeading.append(turtle.heading())
        elif(char == "]"):
            turtle.penup()
            turtle.setposition(stackPosition.pop())
            turtle.setheading(stackHeading.pop())
            turtle.pendown()

def parseRule(line):
    separatorIndex = 0
    for i in range(len(line)):
        if(line[i] == ":"):
            separatorIndex = i
            break
    return [line[:separatorIndex], line[separatorIndex+1:]]

with open(fileName) as f:
    angle = int(f.readline())
    length = int(f.readline())
    depth = int(f.readline())
    start = f.readline()
    for line in f:
        rules.append(parseRule(line))

print(angle)
print(length)
print(depth)
print(start)
print(rules)


#depth = 1
length/=4

end = rewriteDepth(start, depth)

turtle.speed(0)
turtle.delay(0)
turtle.screensize(10000, 10000)
turtle.pendown()
draw(end)
turtle.done()
