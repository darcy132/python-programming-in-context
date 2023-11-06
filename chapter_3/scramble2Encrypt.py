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
    msg = input('Enter a message to encrypt')
    cipherText = scramble2Encrypt(msg)
    print('The encrypted message is:',cipherText)




if __name__ == "__main__":
    a = "ababababababab"
    b = "Today,I learn coding."
    c = scramble2Encrypt(a)
    d = scramble2Encrypt(b)
    e = scramble2Decrypt(c)
    f = scramble2Decrypt(d)
    print(a,b,c,d,e,f,sep='\n')

