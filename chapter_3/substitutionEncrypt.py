def substitutionEncrypt(plainText,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText


def removeChar(string,idx):
    return string[:idx] + string[idx+1:]


def keyGen():
    import random
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    key = ''
    for i in range(len(alphabet)-1,-1,-1):
        idx = random.randint(0,i)
        key +=alphabet[idx]
        alphabet = removeChar(alphabet,idx)
    return key
for i in range(3):
    print(keyGen())