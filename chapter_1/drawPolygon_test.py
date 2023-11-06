from drawPolygon import *
import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.up()
t.backward(200)
t.left(90)
t.down()
t.color('blue')
for i in range(3,13):
    drawPolygon(t,100,i)
wn.exitonclick()