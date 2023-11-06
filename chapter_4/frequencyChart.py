import turtle
def frequencyChar(aList):
    countDict = {}

    for item in aList:
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1
    
    itemList = list(countDict.keys())
    minItem = 0
    maxItem = len(itemList) - 1
    itemList.sort()

    countList = countDict.values()
    maxCount = max(countList)

    wn = turtle.Screen()
    chartT = turtle.Turtle()
    wn.setworldcoordinates(-1,-1,maxItem + 1, maxCount + 1)
    chartT.hideturtle()

    chartT.up()
    chartT.goto(0,0)
    chartT.down()
    chartT.goto(maxItem,0)
    chartT.up()

    chartT.goto(-1,0)
    chartT.write(str(maxCount),font = ("Helevticca",16,"bold"))

    for index in range(len(itemList)):
        chartT.goto(index,-1)
        chartT.write(str(itemList[index]),font=("Helvetica",16,"bold"))

        chartT.goto(index,0)
        chartT.down()
        chartT.goto(index,countDict[itemList[index]])
        chartT.up()
    wn.exitonclick()
a = [3,3,5,7,1,2,5,2,3,4,6,3,4,6,3,4,5,6,6]
frequencyChar(a)