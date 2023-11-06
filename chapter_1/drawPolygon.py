def drawPolygon(myTurtle,sideLength,numsides):
    turnAngle = 360 / numsides
    for i in range(numsides):
        myTurtle.forward(sideLength)
        myTurtle.right(turnAngle)
    
