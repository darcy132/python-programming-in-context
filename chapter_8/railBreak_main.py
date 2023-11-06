from createWordDict import *
from railDecrypt import *
def railBreak(cipherText):
    wordDict = createWordDict('wordlist.txt')
    cipherLen = len(cipherText)
    maxGoodSoFar = 0
    bestGuess = "No words found in dictionary"
    for i in range(2,cipherLen+1):
        words = railDecrypt(cipherText,i)
        goodCount = 0
        for w in words:
            if w in wordDict:
                goodCount += 1
        if goodCount > maxGoodSoFar:
            maxGoodSoFar = goodCount
            bestGuess = " ".join(words)
    return bestGuess