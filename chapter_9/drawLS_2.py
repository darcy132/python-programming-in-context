import turtle
aTurtle = turtle.Turtle()
def drawLS(aTurtle,instructions,angle,distance):
    stateSaver = []
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            pos = aTurtle.position()
            head = aTurtle.heading()
            stateSaver.append((pos,head))
        elif cmd == ']':
            pos,head = stateSaver.pop()
            aTurtle.up()
            aTurtle.setposition(pos)
            aTurtle.setheading(head)
            aTurtle.down()

def applyProduction(axiom,rules,n):
    for i in range(n):
        newString = ''
        for ch in axiom:
            newString = newString + rules.get(ch,ch)
        axiom = newString
    return axiom

def lSystem(axiom,rules,depth,initialPosition,heading,angle,length):
    win = turtle.Screen()
    win.screensize(1000,800)
    aTurtle = turtle.Turtle()
    aTurtle.speed(0)
    win = turtle.Screen()
    aTurtle.up()
    aTurtle.setposition(initialPosition)
    aTurtle.down()
    aTurtle.setheading(heading)
    newRules = applyProduction(axiom,rules,depth)
    drawLS(aTurtle,newRules,angle,length)
    win.exitonclick()

if __name__ == "__main__":
    myRules = {'X':'F[-X]+X','F':'FF'}
    axiom = 'X'
    lSystem(axiom,myRules,7,(0,-200),90,30,2)