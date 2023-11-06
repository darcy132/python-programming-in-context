import turtle
class Sun:
    def __init__(self,iName,iRad,iM,iTemp):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__temp = iTemp
        self.__x = 0
        self.__y = 0

        self.__sTurtle =turtle.Turtle()
        self.__sTurtle.shape("circle")
        self.__sTurtle.color("yellow")

    def getMass(self):
        return self.__mass
    
    def getRadius(self):
        return self.__radius
    
    def getTemperature(self):
        return self.__temp
    
    def getVolume(self):
        import math
        return 4/3*math.pi*self.__radius**3
    
    def getSurfaceArea(self):
        import math
        return 4*math.pi*self.__radius**2
    
    def getDensity(self):
        return self.__mass / self.getVolume()
    
    def getXPos(self):
        return self.__x
    
    def getYPos(self):
        return self.__y
    
    def setName(self,newName):
        self.__name = newName
    
    def setRadius(self,newRadius):
        self.__name = newRadius



    
    def __str(self):
        return self.__name