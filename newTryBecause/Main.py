__author__ = 'twi'

import itertools
import newTryBecause.Permutations
import newTryBecause.CharacterSet
from tkinter import messagebox

filepath = "test.txt"

try:
    file = open(filepath,'w')
except IOError as e:
    print("IOError")

charSet = newTryBecause.CharacterSet.CharacterSet(True,True,True,"#-$?","")
constraints = newTryBecause.CharacterSet.Constraints(4,charSet)
perm = newTryBecause.Permutations.Permutations(file,4,constraints,charSet)
perm.permuteWithTree_Uli(0,"",0,"",4)