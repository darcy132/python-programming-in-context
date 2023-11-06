import random
def createCentroids(k,dataDict):
    centroids = []
    centroidsCount = 0
    centroidsKeys = []

    while centroidsCount < k:
        rKey = random.randint(1,len(dataDict))
        if rKey not in centroidsKeys:
            centroids.append(dataDict[rKey])
            centroidsKeys.append(rKey)
            centroidsCount += 1

    return centroids
