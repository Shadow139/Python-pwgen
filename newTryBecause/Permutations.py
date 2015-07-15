import re
from newTryBecause import CharacterSet

__author__ = 'twi'
import itertools
from tkinter import messagebox

class Permutations:

    def __init__(self,file,pwlength,constraints,charSet):
        self.file = file
        #print("file: {f}".format(f=file))
        self.pwlength = pwlength
        #print("pwlen: {l}".format(l=pwlength))
        self.charSet = charSet
        self.alphabet = charSet.getCharSet()
        #print("alphabet: {a}".format(a=self.alphabet))
        self.constraints = constraints.constraints
        #print("constraints: {c}".format(c=self.constraints))
        self.writeToFile = False
        self.outputStream = False

    def setWriteToFile(self,bool):
        self.writeToFile = bool

    def setOutputStream(self,bool):
        self.outputStream = bool

    def permuteWithTree_Uli(self,lenOfPerm,lastChar,repetitionCount,permutationRightNow,maxRep,mandatory):
        #if lenOfPerm == 2:
        #    print(mandatory)
        #print(mandatory)
        #print("enter")
        #print("alpha:")
        #print(self.alphabet)
        #print(self.pwlength)
        if not self.checkShit(permutationRightNow):
            #print("checkShit")
            return
        if lenOfPerm == self.pwlength and len(mandatory) == 0:
            #print("pwd:")
            #print(permutationRightNow)
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
            #print("should go in check..")
            if len(mandatory) > self.pwlength-lenOfPerm:
                return

            newMan = mandatory

            if i in mandatory:
                regex = re.compile(i)
                newMan = regex.sub("", newMan, 1)

            perm = permutationRightNow
            perm += i
            #print("perm")
            #print(perm)
            self.permuteWithTree_Uli(lenOfPerm+1,i,count,perm,maxRep,newMan)

    def checkShit(self,string):
        #print("lenString: {l}".format(l=len(string)))
        #print("string: {s}".format(s=string))
        if len(string) == 0:
            return True
        x = len(string)-1
        #print(string)
        #print("constraints: {c}".format(c=self.constraints[x]))
        if string[x] in self.constraints[x]:
            #print(x)
            #print(string[x])
            #print(self.constraints[x])
            #print("True")
            return True
        #print("False")
        return False

