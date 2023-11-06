def railDecrypt(cipherText,numRails):
    railLen = len(cipherText) // numRails
    solution = ''
    for col in range(railLen):
        for rail in range(numRails):
            nextLetter = col + (rail*railLen)
            solution += cipherText[nextLetter]
    return solution.split()