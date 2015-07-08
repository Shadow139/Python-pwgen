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

charSet = newTryBecause.CharacterSet.CharacterSet(True,False,False,"#-$?","tu")
constraints = newTryBecause.CharacterSet.Constraints(5,charSet)
constraints.changeConstraint(0,"#")
constraints.changeConstraint(1,"a")
constraints.changeConstraint(2,"#")
constraints.changeConstraint(3,"a")
constraints.changeConstraint(4,"{b}")
#print(constraints.constraints)
perm = newTryBecause.Permutations.Permutations(file,5,constraints,charSet)
perm.permuteWithTree_Uli(0,"",0,"",5,charSet.mandatorymeh)