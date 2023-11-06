def letterToIndex(letter):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    idx = alphabet.find(letter)
    if idx == -1:
        print("error:",letter,"is not in the alphabet")
    return idx

def indexToLetter(idx):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    letter = ''
    if idx >= len(alphabet):
        print("error:",idx,"is to large")
    elif id < 0:
        print("error:",id,"is less then 0")
    else:
        letter = alphabet[idx]
    return letter

