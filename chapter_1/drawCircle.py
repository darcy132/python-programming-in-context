from drawPolygon import *
def drawCircle(myTurtle,radius):
    circumference =2 * 3.1415926 * radius
    sideLength = circumference / 360
    drawPolygon(myTurtle,sideLength,360)