from turtle import *
def drawSquare(t,sideLength):
    for i in range(4):
        t.forward(sideLength)
        t.right(90)
if __name__ == "__main__":
    wn = Screen()
    # t = Turtle()
    # t.color('red')
    # drawSquare(t,100)
    # t.up()
    # t.goto(100,100)
    # t.dot('blue')
    wn.exitonclick()