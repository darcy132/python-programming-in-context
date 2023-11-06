import turtle
class solarSystem:
    def __init__(self,width,height):
        self.__theSun = None
        self.__planets = []
        self.__ssTurtle = turtle.Turtle()
        self.__ssTurtle.hideturtle()
        self.__ssScreen = turtle.Screen()
        self.__ssScreen.setworldcoordinates(-width/2.0,-height/2.0,
                                            width/2.0,height/2.0)
        
    def addPlanet(self,aPlanet):
        self.__planets.append(aPlanet)

    def showPlanets(self):
        for aPlanet in self.__planets:
            print(aPlanet)

    def addSun(self,aSun):
        self.__theSun = aSun
    
    def freeze(self):
        self.__ssScreen.exitonclick()
    
    def movePlanets(self):
        import math
        G = .1
        dt = .001

        for p in self.__planets:
            p.moveTo(p.getXPos() + dt * p.getXVel(),
                     p.getYPos() + dt * p.getYVel())
            
            rX = self.__theSun.getXPos() - p.getYPos()
            rY = self.__theSun.getYPos() - p.getYPos()
            r = math.sqrt(rX**2 + rY**2)

            accX = G * self.__theSun.getMass() * rX / r**3
            accY = G * self.__theSun.getMass() * rY / r**3

            p.setXVel(p.getXVel() + dt * accX)
            p.setYVel(p.getYVel() + dt * accY)

