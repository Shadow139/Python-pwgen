__author__ = 'twi'

alphaF = 'abcdefghijklmnopqrstuvwxyz'
alphaBigF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numF = '0123456789'

alpha = False
alphaBig = False
num = False
custom = []
mandatory = []

def addAlpha():
    alpha = True

def removeAlpha():
    alpha = False

def addAlphaBig():
    alphaBig = True

def removeAlphaBig():
    alphaBig = False

def setCustom(string):
    global custom
    custom = checkIfUnique(string)

def removeCustom():
    custom = []

def setMandatory(string):
    global mandatory
    charSet = []
    if alpha:
        charSet.append(alphaF)
    if alphaBig:
        charSet.append(alphaBigF)
    if num:
        charSet.append(numF)
    charSet.append(custom)
    for x in string:
        if x not in charSet:
            raise ValueError("characters that are mandatory have to be actually used you fucking idiot.")
    mandatory = string

def getAlpha():
    return alpha

def getAlphaBig():
    return alphaBig

def getNum():
    return num

def getCustom():
    return custom

def getMandatory():
    return mandatory

def getCharSet():
    charSet = []
    if alpha:
        charSet.append(alphaF)
    if alphaBig:
        charSet.append(alphaBigF)
    if num:
        charSet.append(numF)
    charSet.append(custom)
    charSet.append(mandatory)
    return charSet

# for custom - if characters are not unique, then it will return a string where all characters exist once
def checkIfUnique(string):
    newString = ""
    for x in string:
        if countLetter(newString,x) == 0:
            newString = newString + x
    return newString

def countLetter(string,char):
    count = 0
    for x in string:
        if x == char:
            count += 1
    return count

constraints = []

def initConstraints(length):
    charSet = getCharSet()
    i = 0
    while i < length:
        constraints[i] = charSet
        i += 1