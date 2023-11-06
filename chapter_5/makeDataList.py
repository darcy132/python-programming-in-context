def makeDataList(dataName):
    import csv
    with open('/home/brown/Downloads/all_hour.csv','r') as inFile:
        dataList = []

        csvReader = csv.reader(inFile)
        titles = next(csvReader)

        colNum = 0
        while colNum < len(titles) and titles[colNum] != dataName:
            colNum += 1
        
        if colNum == len(titles):
            print("Error:",dataName, " not found.")
        else:
            for line in csvReader:
                dataList.append(float(line[colNum]))
    return dataList

magList = makeDataList("mag")
print(len(magList))
for i in range(10):
    print(magList[1],end = " ")
import statistics
print(max(magList),min(magList),statistics.mean(magList)\
      ,statistics.median(magList),statistics.stdev(magList))