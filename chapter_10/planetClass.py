import turtle
class Planet:
    def __init__(self,iName,iRad,iM,iDist,iVx,iVy,iC):
        self.__name = iName 
        self.__radius = iRad 
        self.__mass = iM 
        self.__distance = iDist
        self.__x =self.__distance
        self.__y = 0
        self.__velX = iVx
        self.__velY = iVy
        self.__color = iC

        self.__pTurtle = turtle.Turtle()

        self.__pTurtle.color(self.__color)
        self.__pTurtle.shape("circle")

        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x,self.__y)
        self.__pTurtle.down()
#ACCESSOR METHOD

    def getName(self):
        return self.__name
    
    def getRadius(self):
        return self.__radius
    
    def getMass(self):
        return self.__mass
    
    def getDistance(self):
        return self.__distance
    
    def getVolume(self):
        import math
        return 4/3 * math.pi *self.__radius**3
    
    def getSurfaceArea(self):
        import math
        sa = 4*math.pi*self.__radius**2
        return sa
    
    def getDensity(self):
        return self.__mass / self.getVolume()

    def getXPos(self):
        return self.__x
    
    def getYPos(self):
        return self.__y
    def moveTo(self,newX,newY):
        self.__x = newX
        self.__y = newY
        self.__pTurtle.goto(self.__x,self.__y)

    def getXVel(self):
        return self.__velX
    def getYVel(self):
        return self.__velY
    
#MUTATOR METHOD
    def setName(self,newName):
        self.__name = newName
    def setRadius(self,newRadius):
        self.__radius = newRadius
    def setMass(self,newMass):
        self.__mass = newMass
    def setDistance(self,newDistance):
        self.__distance = newDistance
    def setXVel(self,newVx):
        self.__velX = newVx
    def setYVel(self,newVy):
        self.__velY = newVy

        
#MAGIC METHOD

    def __str__(self):
        return self.__name
    
    def __lt__(self,otherPlanet):
        return self.__distance < otherPlanet.__distance
    
    def __gt__(self,otherPlanet):
        return self.__distance > otherPlanet.__distcane
