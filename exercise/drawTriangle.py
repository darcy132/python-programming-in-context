import turtle
def drawTriangle(t,sideLength):
    i = 0
    while(i<3):
        t.forward(sideLength)
        t.right(120)
        i += 1
t = turtle.Turtle()
wn = turtle.Screen()
drawTriangle(t,100)
