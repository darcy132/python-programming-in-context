def substitutionEncrypt(plainText,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText

def Dncrypt(cipherText,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    plainText = ""
    for ch in cipherText:
        idx = key.find(ch)
        plainText += alphabet[idx]
    return plainText


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

if __name__ == "__main__":
    def main():
        plaintxt = input("Enter the message to encrypt:")
        a = len(plaintxt)
        key = keyGen()
        chipertxt = substitutionEncrypt(plaintxt,key)
        b = len(chipertxt)
        c = len(plaintxt)
        d = len(key)
        decryptText = Dncrypt(chipertxt,key)
        print(key,chipertxt,sep="\n")
        print(a,b,c,d)
        print(decryptText)
    main()