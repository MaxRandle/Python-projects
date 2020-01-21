#CIPHERS

alphaLower = "abcdefghijklmnopqrstuvwxyz"
alphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#<Caesar>
def hackCaesar(message):
    newMessage = ""
    for key in range(0, 25):
        for char in message:
            if char in alphaLower:
                newLetterPosition = (alphaLower.index(char) + key) % 26
                newMessage += alphaLower[newLetterPosition]
            elif char in alphaUpper:
                newLetterPosition = (alphaUpper.index(char) + key) % 26
                newMessage += alphaUpper[newLetterPosition]
            else: newMessage += char
        print(newMessage, "key was {}".format(key))
        newMessage = ""
    return

def encryptCaesar(message, key):
    """To decrypt simply write the negative key"""
    newMessage = ""
    for char in message:
        if char in alphaLower:
            newLetterPosition = (alphaLower.index(char) + key) % 26
            newMessage += alphaLower[newLetterPosition]
        elif char in alphaUpper:
            newLetterPosition = (alphaUpper.index(char) + key) % 26
            newMessage += alphaUpper[newLetterPosition]
        else: newMessage += char
    return newMessage
#</Caesar>

#<Vigenere>
def encryptVigenere(message, key):
    length = getLength(message)
    key = prepKey(key.lower(), length)
    newMessage = ""
    for i in range(0, length):
        if message[i] in alphaLower:
            #the magic encryption statement:
            newMessage += chr(((ord(message[i])+ord(key[i])-194)%26)+97)
        elif message[i] in alphaUpper:
            newMessage += chr(((ord(message[i])+ord(key[i])-130)%26)+65)
        else:
            newMessage += message[i]
    return newMessage

def decryptVigenere(message, key):
    length = getLength(message)
    key = prepKey(key.lower(), length)
    newMessage = ""
    for i in range(0, length):
        if message[i] in alphaLower:
            #the magic decryption statement:
            newMessage += chr(((ord(message[i])-ord(key[i])+26)%26)+97)
        elif message[i] in alphaUpper:
            newMessage += chr(((ord(message[i])-ord(key[i])+26)%26)+65)
        else:
            newMessage += message[i]
    return newMessage

def getLength(message):
    """gets the number of letters in the message, (excluding spaces & punctuation)"""
    length = 0
    for char in message:
        if char in alphaUpper or alphaLower:
            length += 1
    return length

def prepKey(key, length):
    """repeats key untill it is the correct length"""
    keyString = ""
    while len(keyString) < length:
        for char in key:
            if len(keyString) < length:
                keyString += char
    return keyString   
#</Vigenere>
