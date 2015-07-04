__author__ = 'twi'

import itertools
from newTryBecause.Permutations import permute_wiktor,permute_wiktor_file,product
from tkinter import messagebox

filePath = "test.txt"


try:
   file = open(filePath,'w')
except IOError as e:
    messagebox.showinfo("Error", "I/O error({0}): {1}".format(e.errno, e.strerror))

permList = list(product(file,"abcdefghij", repeat = 10))


for x in permList:
    print(x)
print(len(permList))
