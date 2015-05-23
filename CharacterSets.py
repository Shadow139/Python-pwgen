__author__ = 'Shadow'

charSet = []
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphaBig = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['0','1','2','3','4','5','6','7','8','9']
custom = []
manditory = []

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

def setCustom(string):
    global custom
    custom = checkIfUnique(string)
    #print(custom)

def setManditory(string):
    global manditory
    manditory = string
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

# for custom and manditory - if chracters are not unique, then it will return a string where all characters exist once
def checkIfUnique(self,string):
    newString = ""
    len = len(string)
    count = 0
    while count < len:
        if self.countLetter(newString,string[count]) == 0:
            newString = newString + string[count]
        count += 1
    return string

def countLetter(self,string,char):
    count = 0
    for x in string:
        if x == char:
            count += 1
    return count