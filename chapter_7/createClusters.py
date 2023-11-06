from edulidD import *
def createClusterss(k,centroids,dataDict,repeats):
    for aPass in range(repeats):
        print("****PASS",aPass + 1, "****")
        clusters = []           #Create a list containing k empty lists
        for i in range(k):
            clusters.append([])

        for aKey in dataDict:   #Calculate the distance to the center point
            distances = []          
            for clusterIndex in range(k):
                dToC = edulidD(dataDict[aKey],centroids[clusterIndex])
                distances.append(dToC)
            minDist = min(distances)    #Find the minimun
            index = distances.index(minDist)

            clusters[index].append(aKey)    #Add to cluster
        
        dimensions = len(dataDict[1])   #Recalculate clustering
        for clusterIndex in range(k):
            sums = [0] * dimensions        #Initialize the sum of each dimension
            for aKey in clusters[clusterIndex]:
                dataPoints = dataDict[aKey]
                for ind in range(len(dataPoints)):      #Calculate sums
                    sums[ind] += dataPoints[ind]        
                for ind in range(len(sums)):        #Calculate the average
                    clusterLen = len(clusters[clusterIndex])
                    if clusterLen != 0:         #Make sure not to divide by 0
                        sums[ind] = sums[ind] / clusterLen  
                centroids[clusterIndex] = sums      #Assign avg to the center point

        for c in clusters:      #Output cluster
            print("CLUSTER")
            for key in c:
                print(dataDict[key],end = " ") 
            print()

    return clusters               
