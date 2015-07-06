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

    def permuteWithTree_Uli(self,lenOfPerm,lastChar,repetitionCount,permutationRightNow,maxRep):
        #print("enter")
        if (lenOfPerm == self.pwlength):
            print(permutationRightNow)
            #self.file.write(permutationRightNow+"\n")
            return
        for i in self.alphabet:
            count = repetitionCount

            if lastChar == i:
                count += 1
            if count > maxRep:
                return
            #print("should go in check..")
            if not self.checkShit(permutationRightNow):
                return

            perm = permutationRightNow
            perm += i
            self.permuteWithTree_Uli(lenOfPerm+1,i,count,perm,maxRep)

    def checkShit(self,string):
        #print("lenString: {l}".format(l=len(string)))
        #print("string: {s}".format(s=string))
        if len(string) == 0:
            return True
        x = len(string)-1
        #print("constraints: {c}".format(c=self.constraints[x]))
        if string[x] in self.constraints[x]:
            #print("True")
            return True
        #print("False")
        return False


def permute_uli(string):
    for i in string:
        return


def permute_uli_theObviouslyBetterOne():
    return

def permute_wiktor(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111

    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


def permute_wiktor_file(file,*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111

    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        file.write(str(tuple(prod) + '\n'))
        #yield tuple(prod)

def product2(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def product(file,*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        file.write(str(tuple(prod)))
        yield tuple(prod)