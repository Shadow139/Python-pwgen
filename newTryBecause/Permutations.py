__author__ = 'twi'
import itertools
from tkinter import messagebox

class Permutations:
    def __init__(self, filepath, pwlength,alphabet):
        self.filepath = filepath
        self.pwlength = pwlength
        self.alphabet = alphabet



def permuteWithTree_Uli(charset,maxlen,lenOfPerm,lastChar,repetitionCount,permutationRightNow,maxRep):
    if (lenOfPerm == maxlen):
        print(permutationRightNow)
        return
    for i in charset:
        count = repetitionCount
        if lastChar == i:
            count += 1
        if count > maxRep:
            return
        perm = permutationRightNow
        perm += i
        permuteWithTree_Uli(charset,maxlen,lenOfPerm+1,i,count,perm,maxRep)


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