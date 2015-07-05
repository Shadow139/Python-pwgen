__author__ = 'twi'

import re

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
pattern = re.compile("^[aA0#$]+$")

def initConstraints(length):
    charSet = getCharSet()
    i = 0
    while i < length:
        constraints[i] = charSet
        i += 1

def changeConstraint(id,string):
    charSet = getCharSet()
    if len(string) == 3 and string[0] == "\"" and string[2] == "\"" and string[1] in getCharSet():
        constraints[id] = string[1]
    elif pattern.match(string):
        chars = ""
        for i in string:
            if i in charSet:
                chars += i
            else:
                raise ValueError("you are so fuuucked. stuff that is not in charset is here. ya know.")
            constraints[id] = chars
    else:
        raise ValueError("wrong input. idiots!! how did this happen. =(")