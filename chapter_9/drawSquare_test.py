import turtle
from drawSquare import *
t = turtle.Turtle()
t.speed(0)
t.color('red','red')
wn = turtle.Screen()
nestedBox(t,100)
t.hideturtle()
wn.exitonclick()