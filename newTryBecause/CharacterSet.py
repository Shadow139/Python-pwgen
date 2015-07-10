__author__ = 'twi'

import re

class CharacterSet:

    alphaF = 'abcdefghijklmnopqrstuvwxyz'
    alphaBigF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numF = '0123456789'

    #alphaF = 'abcnopqrstuxyz'
    #alphaBigF = 'ABCOPQRSTUVWXYZ'
    #numF  = '0123789'

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
        global custom
        custom = self.checkIfUnique(string)

    def setMandatory(self,string):
        global mandatory
        charSet = []
        if self.alpha:
            charSet.append(self.alphaF)
        if self.alphaBig:
            charSet.append(self.alphaBigF)
        if self.num:
            charSet.append(self.numF)
        charSet.append(custom)
        for x in string:
            if x not in charSet:
                raise ValueError("characters that are mandatory have to be actually used you fucking idiot.")
        mandatory = string

    def getAlpha(self):
        return self.alpha

    def getAlphaBig(self):
        return self.alphaBig

    def getNum(self):
        return self.num

    def getCustom(self):
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

    # for custom - if characters are not unique, then it will return a string where all characters exist once
    def checkIfUnique(self,string):
        newString = ""
        for x in string:
            if self.countLetter(newString,x) == 0:
                newString = newString + x
        return newString

    def countLetter(string,char):
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
        i = 0
        while i < pwlength:
            self.constraints.append("")
            i += 1
        self.pattern = re.compile("^[aA0#$]+$")
        self.pwlength = pwlength
        self.characterSet = characterSet
        self.initConstraints()
        #print(self.constraints)

    def initConstraints(self):
        charSet = self.characterSet.getCharSet()
        i = 0
        while i < self.pwlength:
            self.constraints[i] = charSet
            #print(self.constraints)
            i += 1
        #print(self.constraints)

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
            #print(self.constraints)
        else:
            raise ValueError("wrong input. idiots!! how did this happen. =(")