def drawLS(t,instructions,angle,distance):
    for cmd in instructions:
        if cmd == "F":
            t.forward(distance)
        elif cmd == "B":
            t.backward(distance)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)
        else:
            print('Error:',cmd,'is an unknown command')

def applyProduction(axiom,rules,n):
    for i in range(n):
        newString = ''
        for ch in axiom:
            newString = newString + rules.get(ch,ch)
        axiom = newString
    return axiom

if __name__ == "__main__":
    import turtle
    t = turtle.Turtle()
    t.hideturtle()
    axiom = "F"
    myRules = {'F':'F-F++FF-F'} 
    res = applyProduction(axiom,myRules,5)
    drawLS(t,res,60,3)