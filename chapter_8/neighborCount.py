def maybeAdd(ch,toDict):
    if ch in 'abcdefghijklmnopqrstuvwxyz':
        toDict[ch] = toDict.setdefault(ch,0) + 1

def neighborCount(text):
    nbDict = {}
    text = text.lower()
    for i in range(len(text) - 1):
        nbList = nbDict.setdefault(text[i],{})
        maybeAdd(text[i + 1],nbList)
        nbList = nbDict.setdefault(text[i + 1],{})
        maybeAdd(text[i],nbList)
    return nbDict

def checkWord(unused,pattern):
    import re
    resList = []
    with open("wordlist.txt",'r') as wordFile:
        rePat = '['+unused+']'
        regex = re.sub('[a-z]',rePat,pattern) + '$'
        regex = regex.lower()
        print('matching',regex)
        for line in wordFile:
            if re.match(regex,line[:-1]):
                resList.append(line[:-1])
        return resList
    
def findLetters(unused,pattern):
    pass