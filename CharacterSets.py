__author__ = 'Shadow'

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphaBig = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['0','1','2','3','4','5','6','7','8','9']
custom = []
manditory = []

def setCustom(string):
    custom = []
    for x in string:
        custom.append(x)
    #print(custom)

def setManditory(string):
    manditory = []
    for x in string:
        manditory.append(x)
    #print(manditory)

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