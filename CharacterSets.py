__author__ = 'Shadow'

charSet = []
alpha = 'abcdefghijklmnopqrstuvwxyz'
alphaBig = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
custom = []
mandatory = []

def addAlpha():
    global charSet
    global alpha
    if alpha not in charSet:
        charSet.append(alpha)

def removeAlpha():
    global charSet
    global alpha
    if alpha in charSet:
        charSet.remove(alpha)

def addAlphaBig():
    global charSet
    global alphaBig
    if alphaBig not in charSet:
        charSet.append(alphaBig)

def removeAlphaBig():
    global charSet
    global alphaBig
    if alphaBig in charSet:
        charSet.remove(alphaBig)

def setCustom(string):
    global custom
    global charSet
    if custom in charSet:
        charSet.remove(custom)
    custom = checkIfUnique(string)
    charSet.append(custom)

    #print(custom)

def removeCustom():
    global custom
    global charSet
    if custom in charSet:
        charSet.remove(custom)

def setMandatory(string):
    global mandatory
    global charSet
    for x in mandatory:
        if x not in charSet:
            raise ValueError("characters that are mandatory have to be in the charSet...")
    mandatory = string

    #print(mandatory)

def getAlpha():
    return alpha

def getAlphaBig():
    return alphaBig

def getNum():
    return num

def getCustom():
    return custom

def getManditory():
    return manditory

def getCharSet():
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