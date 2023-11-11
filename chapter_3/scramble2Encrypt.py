def scramble2Encrypt(plaintxt):
    evenChars = ''
    oddChars = ''
    charCount = 0
    for ch in plaintxt:
        if charCount % 2 == 0:
            evenChars += ch
        else:
            oddChars += ch
        charCount +=1
    cipherText = oddChars + evenChars
    return cipherText
def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plainText = ""
    for i in range(halfLength):
        plainText += evenChars[i]
        plainText += oddChars[i]
    
    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]
    return plainText

def stripSpaces(myString):
    newString =''
    for i in range(len(myString)):
        if myString[i] != ' ':
            newString +=myString[i]
    return newString
def encryptMessage():
    msg = input('Enter a message to encrypt:')
    cipherText = scramble2Encrypt(msg)
    print('The encrypted message is:',cipherText)
    return cipherText




if __name__ == "__main__":
    def test():
        a = encryptMessage()
        b = scramble2Decrypt(a)
        print(a)
        print(b)
    test()
