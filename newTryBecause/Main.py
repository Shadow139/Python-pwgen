__author__ = 'twi'

import itertools
import Permutations
from tkinter import messagebox

filepath = "test.txt"

try:
    file = open(filepath,'w')
except IOError as e:
    print("IOError")

perm = Permutations.Permutations(file,12,"abcdefg")

perm.permuteWithTree_Uli(0,"",0,"",12)