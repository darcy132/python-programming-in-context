def removeMatches(myString,removeString):
    newStr = ""
    for ch in myString:
        if ch not in removeString:
            newStr += ch
    return newStr

def letterFrequency(text):
    text = text.lower()
    nonLetters = removeMatches(text, 'abcdefghijklmnopqrstuvwxyz')
    text = removeMatches(text,nonLetters)
    lCount = {}
    total = len(text)
    for ch in text:
        lCount[ch] = lCount.get(ch,0) + 1
    for ch in lCount:
        lCount[ch] = lCount[ch] /total
    return lCount

if __name__ == "__main__":
    import sys
    sys.stdout = open('letterFrequency.txt',"w")
    with open('pg36.txt','r') as wells:
        text = wells.read()
        print(letterFrequency(text))
    sys.stdout.close()