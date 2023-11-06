import csv
with open("all_hour.csv","r") as dataFile:
    csvReader = csv.reader(dataFile)
    titles = next(csvReader)
    print("titles:",titles)

    earthquakeLine = next(csvReader)
    print("earthquake:",earthquakeLine)
    print("latitude:",earthquakeLine[1])
    print("longitude:",earthquakeLine[2])