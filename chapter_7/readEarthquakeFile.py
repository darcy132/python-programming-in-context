import csv

def readEarthquakeFile(filename):
    with open(filename,'r') as dataFile:
        csvReader = csv.reader(dataFile)
        titles = next(csvReader)
        dataDict = {}
        key = 0

        for aLine in csvReader:
            key += 1
            lat = float(aLine[1])
            long = float(aLine[2])
            dataDict[key] = [long,lat]
        return dataDict
    
if __name__ == "__main__":
    a = readEarthquakeFile('all_hour.csv')
    print(a,len(a),sep='\n')