import re

__author__ = 'twi'

class Permutations:

    def __init__(self,file,pwlength,constraints,charSet):
        self.file = file
        self.pwlength = pwlength
        self.charSet = charSet
        self.alphabet = charSet.getCharSet()
        self.constraints = constraints.constraints
        self.writeToFile = False
        self.outputStream = False

    def setWriteToFile(self,bool):
        self.writeToFile = bool

    def setOutputStream(self,bool):
        self.outputStream = bool

    def permuteWithTree_Uli(self,lenOfPerm,lastChar,repetitionCount,permutationRightNow,maxRep,mandatory):
        if not self.checkShit(permutationRightNow):
            return
        if lenOfPerm == self.pwlength and len(mandatory) == 0:
            if self.writeToFile:
                self.file.write(permutationRightNow+"\n")
            if self.outputStream:
                pass
            return
        for i in self.alphabet:
            count = repetitionCount

            if lastChar == i:
                count += 1
            if count > maxRep:
                return
            if len(mandatory) > self.pwlength-lenOfPerm:
                return

            newMan = mandatory

            if i in mandatory:
                regex = re.compile(i)
                newMan = regex.sub("", newMan, 1)

            perm = permutationRightNow
            perm += i
            self.permuteWithTree_Uli(lenOfPerm+1,i,count,perm,maxRep,newMan)

    def checkShit(self,string):
        if len(string) == 0:
            return True
        x = len(string)-1
        if string[x] in self.constraints[x]:
            return True
        return False

