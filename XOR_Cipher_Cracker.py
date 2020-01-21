#one time pad assignment

cipherHexList = [
 "12 08 92 66 87 F7 10 2B 04 04 9B 7A 60 28 8D BD 70 85 ED FF A6 AA E1 78 C1 2F",
 "11 04 9E 79 94 E5 5C 6A 1F 15 DE 79 7C 7C DA A9 77 89 B9 E9 F2 A2 E2 72 CB 2F",
 "06 0E C8 65 89 F1 10 21 18 0E CC 34 78 34 C2 EC 76 84 F6 EE A6 B9 E6 72 C8 3E",
 "04 00 9B 74 8F EB 5E 6A 02 13 DE 7A 6B 2F 8D A0 6C 9A FC BA F5 A5 E1 65 D1 2F",
 "10 04 8C 3C 85 E5 42 2E 56 08 C8 34 61 33 D9 EC 64 82 B9 F5 F6 B9 E7 78 CB 2F",
 "07 0F 8D 71 9F A4 58 2B 05 41 D8 78 6E 35 C0 A9 61 CC EF F3 E5 B9 E1 65 DC 2F",
 "07 17 8D 6E 9F A4 5F 2C 10 08 D8 71 7D 7C C5 AD 76 CC F8 BA EB A8 EA 76 C9 2F"]

plainTextList = [
    "Pizzas are not quite good",
    "Several items were stolen",
    "Do you know who shot them",
    "Fashion trends live short",
    "Red card is not an option",
    "Enemy has claimed victory",
    "Every officer has a medal"]

allowedCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.?!'"

def crack(colNum):
    col = getCol(colNum)
    keyList = generateKeyList()
    resultString = ""
    for key in keyList:
        for char in col:
            result = chr(key ^ char)
            if result in allowedCharacters:
                resultString += result
        if len(resultString) == 7:
            print("Key: " + str(key))
            for i in range(0, len(resultString)):
                print(plainTextList[i] + resultString[i])
            print("--------")
        resultString = ""

##def add(colNum, key):
##    col = getCol(colNum)
##    for c in range(0, len(col)):
##        result = chr(key ^ col[c])
##        plainTextList += [result]
    
def generateKeyList():
    """return a list of numbers from 0-255"""
    keyList = []
    for i in range(0, 255):
        keyList += [i]
    return keyList

def getCol(colNum):
    """gets the column as an int list"""
    col = []
    for row in cipherHexList:
        rowList = row.split(" ")
        col += [int(rowList[colNum], 16)]
    return col
