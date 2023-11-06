def createWordDict(dName):
    myDict = {}
    with open(dName,'r') as myFile:
        for line in myFile:
            myDict[line[:-1]] = True
        return myDict

if __name__ == "__main__":
    import sys
    sys.stdout = open('Dict.txt','w')
    print(createWordDict('wordlist.txt'))
    sys.stdout.close()