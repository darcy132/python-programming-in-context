def readFile(filename):
    with open(filename,"r") as dataFile:
        dataDict = {}

        key = 0
        for aLine in dataFile:
            key += 1
            score = int(aLine)
            dataDict[key] = [score]
        
    return dataDict
