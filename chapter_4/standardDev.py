import math

def getRange(alist):
    return max(alist) - min(alist)

def getMax(aList):
    maxSoFar = aList[0]
    for pos in range(1,len(aList)):
        if aList[pos] > maxSoFar:
            maxSoFar = aList[pos]
    return maxSoFar

def mean(aList):
    return sum(aList) / len(aList)




def standardDev(alist):
    theMean = mean(alist)

    total = 0
    for item in alist:
        difference = item - theMean
        diffSq = difference **2
        total += diffSq
    
    sDev = math.sqrt(total / len(alist) - 1)
    return sDev