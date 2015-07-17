__author__ = 'twi'

import re

class CharacterSet:

    alphaF = 'abcdefghijklmnopqrstuvwxyz'
    alphaBigF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numF = '0123456789'

    alpha = False
    alphaBig = False
    num = False
    custom = []
    mandatory = []

    def __init__(self,alpha,alphaBig,num,custom,mandatory):
        self.alpha = alpha
        self.alphaBig = alphaBig
        self.num = num
        self.custom = custom
        self.mandatory = mandatory

    def setAlpha(self,bool):
        self.alpha = bool

    def setAlphaBig(self,bool):
        self.alphaBig = bool

    def setNum(self,bool):
        self.num = bool

    def setCustom(self,string):
        self.custom = self.checkIfUnique(string)
        #print(self.getCustom())

    def setMandatory(self,string):
        charSet = self.getCharSet()
        for x in string:
            if x not in charSet:
                raise ValueError("characters that are mandatory have to be actually used you fucking idiot.")
        self.mandatory = string

    def getAlpha(self):
        return self.alpha

    def getAlphaBig(self):
        return self.alphaBig

    def getNum(self):
        return self.num

    def getCustom(self):
        #print(self.custom)
        return self.custom

    def getMandatory(self):
        return self.mandatory

    def getCharSet(self):
        charSet = []
        if self.alpha:
            charSet.extend(self.alphaF)
        if self.alphaBig:
            charSet.extend(self.alphaBigF)
        if self.num:
            charSet.extend(self.numF)
        charSet.extend(self.custom)
        charSet.extend(self.mandatory)
        return charSet

    def checkIfUnique(self,string):
        newString = ""
        for x in string:
            if self.countLetter(newString,x) == 0:
                newString = newString + x
        return newString

    def countLetter(self,string,char):
        if len(string) == 0:
            return 0
        count = 0
        for x in string:
            if x == char:
                count += 1
        return count

class Constraints:

    def __init__(self,pwlength,characterSet):
        self.constraints = []
        self.pattern = re.compile("^[aA0#$]+$")
        self.pwlength = pwlength
        self.characterSet = characterSet
        self.initConstraints()

    def initConstraints(self):
        charSet = self.characterSet.getCharSet()
        self.constraints = []
        i = 0
        while i < self.pwlength:
            self.constraints.append("")
            i += 1
        i = 0
        while i < self.pwlength:
            self.constraints[i] = charSet
            i += 1

    def updateConstraints(self,pwlength,dictSpecials):
        self.pwlength = pwlength
        self.initConstraints()
        for key in dictSpecials.keys():
            self.constraints[key] = dictSpecials[key]

    def changeConstraint(self,id,string):
        if id >= self.pwlength:
            raise ValueError("too big value. IDIOT. id. thing.")
        charSet = self.characterSet.getCharSet()
        if len(string) == 3 and string[0] == "{" and string[2] == "}" and string[1] in self.characterSet.getCharSet():
            self.constraints[id] = string[1]
        elif self.pattern.match(string):
            chars = ""
            for i in string:
                if i in charSet:
                    if i in chars:
                        raise ValueError("you be stupid. because. not more than once everythingieee! dont know how you did it..")
                    chars += i
                else:
                    raise ValueError("you are so fuuucked. stuff that is not in charset is here. ya know.")
            actualChars = ""
            for i in chars:
                if i == "a":
                    actualChars += self.characterSet.alphaF
                elif i == "A":
                    actualChars += self.characterSet.alphaBigF
                elif i == "0":
                    actualChars += self.characterSet.numF
                elif i == "#":
                    actualChars += self.characterSet.custom
                else:
                    raise ValueError("you did the undoable..")
            self.constraints[id] = actualChars
        else:
            raise ValueError("wrong input. idiots!! how did this happen. =(")

    def setConstraint(self,id,string):
        self.constraints[id-1] = string