def tree(t,trunkLength):
    if trunkLength < 5:
        return 
    else:
        t.forward(trunkLength)
        t.right(30)
        tree(t,trunkLength - 15)
        t.left(60)
        tree(t,trunkLength - 15)
        t.right(30)
        t.backward(trunkLength)
    
if __name__ == "__main__":
    import turtle
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.up()
    t.goto(0,-255)
    t.down()
    t.color("green","green")
    t.left(90)
    tree(t,115)
    t.hideturtle()
    wn.exitonclick()