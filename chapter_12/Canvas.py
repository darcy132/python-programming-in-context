import turtle
class Canvas:
    def __init__(self,w,h):
        self.__turtle = turtle.Turtle()
        self.__screen = turtle.Screen()

        self.__screen.setup(width = w, height = h)
        self.__turtle.hideturtle()

    def draw(self,gObject):
        self.__turtle.up()
        self.__screen.tracer(0)
        gObject._draw(self.__turtle)
        self.__screen.tracer(1)
        
from abc import *

class GeometricObject(ABC):
    def __init__(self):
        self.__lineColor = 'black'
        self.__lineWidth = 1

    def getColor(self):
        return self.__lineColor
    
    def getWidth(self):
        return self.__lineWidth
    
    def setColor(self,color):
        self.__lineColor = color

    def setWidth(self,width):
        self.__lineWidth = width

    @abstractclassmethod
    def _draw(self,someTurtle):
        pass

class Point(GeometricObject):
    def __init__(self,x,y):
        super().__init__()
        self.__x = x
        self.__y = y

    def getCoord(self):
        return (self.__x,self.__y)
    
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
    
    def _draw(self,turtle):
        turtle.goto(self.__x,self.__y)
        turtle.dot(self.getWidth(),self.getColor())

class Line(GeometircObject):
    def __init__(self,p1,p2):
        super().__init__()
        self.__p1 = p1
        self.__p2 = p2
    
    def getP1(self):
        return self.__p1
    
    def getP2(self):
        return self.__p2
    
    def _draw(self,turtle):
        turtle.color(self.getColor())
        turtle.width(self.getWidth())
        turtle.goto(self.__p1.getCoord())
        turtle.down()
        turtle.goto(self.__p2.getCoord())
          