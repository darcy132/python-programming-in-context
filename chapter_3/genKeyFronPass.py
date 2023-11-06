def removeDupes(myString):
    newStr = ""
    for ch in myString:
        if ch not in newStr:
            newStr += ch
    return newStr

def removeMatches(myString,removeString):
    newStr = ""
    for ch in myString:
        if ch not in removeString:
            newStr += ch
    return newStr

def genKeyFromPass(password):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    password = password.lower()
    password = removeDupes(password)
    lastChar = password[-1]
    lastIdx = alphabet.find(lastChar)
    afterString = removeMatches(alphabet[lastIdx + 1:],password)
    beforeString = removeMatches(alphabet[:lastIdx],password)
    key = password + afterString + beforeString
    return key