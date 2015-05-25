__author__ = 'twi'

# a = lower case
# A = upper case
# 0 = number
# # = custom character
# ".." = string
# (..) = set of character sets - example: (aA0) - for permutations of lower, upper case and numbers
patterns = {}
idGen = 0

def removeAllPatterns():
    patterns = {}

def addPattern(pattern):
    global idGen
    patterns[idGen]=pattern
    idGen += 1

def removePattern(id):
    if (len(patterns) > id):
        del patterns[id]

def getPatternAt(id):
    if (len(patterns) > id):
        return patterns[id]

class Pattern:
    def __init__(self,string,start,end,pwdLen):
        if (self.ckeckInput(string,pwdLen)):
            self.string = string
            self.start = start
            self.end = end
        else:
            raise ValueError("wrong fucking input for the pattern")


    def getString(self):
        return self.string

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def checkInput(self,pwdLen):
        string = self.getString()
        if (self.getEnd()-self.getStart() > pwdLen):
            raise ValueError("too long shit and shit - pattern longer than password")
        x = 0
        for i in patterns:
            x = x + (i.getEnd - i.getStart())
        x = x + (self.getEnd()-self.getStart())
        if (x > pwdLen):
            raise ValueError("just too fucking much - this pattern adds too much length")
        amountBrackets = 0
        amountQuotes = 0
        for i in string:
            if (i != "a" and i != "A" and i != "0" and i != "#" and i != "\"" and i != "(" and i != ")"):
                raise ValueError("wrooooong - wrong characters entered")
            if (i == "("):
                amountBrackets = amountBrackets+1
            if (i == ")"):
                amountBrackets = amountBrackets-1
            if (amountBrackets < 0 or amountBrackets > 1):
                raise ValueError("just bullshit - brackets are really wrong")
            if (i == "\""):
                amountQuotes = amountQuotes+1
        if (amountBrackets != 0 or amountQuotes%2 != 0):
            raise ValueError("wrong shit!! - either wrong amount of brackets or quotes or even both. you IDIOT!")
