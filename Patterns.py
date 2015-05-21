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
    patterns[idGen]=pattern
    idGen = idGen+1

def removePattern(id):
    if (len(patterns) > id):
        del patterns[id]

def getPatternAt(id):
    if (len(patterns) > id):
        return patterns[id]

class Pattern:
    def __init__(self,string,start,end):
        if (self.ckeckInput(string)):
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

    def checkInput(self,string):