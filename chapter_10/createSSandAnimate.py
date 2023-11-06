from planetClass import *
from sun import *
from solarSystem import *
def createSSandAnimate():
    ss = solarSystem(2,2)
    
    sun =Sun("Sun",5000,10,5800)
    ss.addSun(sun)

    m = Planet("Mercury",19.5,1000,.25,0,2,"Blue")
    ss.addPlanet(m)

    m = Planet("Mars",50,9000,0.5,0,1.63,"red")
    ss.addPlanet(m)

    m = Planet("Earth",47.5,5000,0.3,0,2.0,"green")
    ss.addPlanet(m)

    m = Planet("Jupiter",100,49000,0.7,0,1,"black")
    ss.addPlanet(m)

    numTimePeriods = 2000
    for aMove in range(numTimePeriods):
        ss.movePlanets()
    
    ss.freeze()

if __name__ == "__main__":
    createSSandAnimate()