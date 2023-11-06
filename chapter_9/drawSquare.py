def drawSquare(aTurtle,side):
    for i in range(4):
        aTurtle.forward(side)
        aTurtle.right(90)
def nestedBox(aTurtle,side):
    if side >= 1:
        drawSquare(aTurtle,side)
        nestedBox(aTurtle,side - 5)