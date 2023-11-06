import turtle
from drawCircle import *
if __name__ == '__main__':
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor('blue')
    t.up()
    t.backward(200)
    t.left(90)
    t.down()
    t.speed(10)
    for i in range(20,201,20):
        drawCircle(t,i)