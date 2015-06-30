__author__ = 'Hollow'
from BuildPermutations import *
from tkinter import messagebox

class Generator():
    def __init__(self,length,string,filePath):
        #self.characterSet = characterSet
        #self.patterns = patterns
        self.filePath = filePath
        try:
            file = open(filePath,'w')
            self.combinations_with_replacement(string,int(length),file)
        except IOError as e:
            messagebox.showinfo("Error", "I/O error({0}): {1}".format(e.errno, e.strerror))

    def combinations_with_replacement(self,iterable, r, file):
        'Alternate version that filters from product()'
        pool = tuple(iterable)
        print('pool: ', pool)
        n = len(pool)
        print('length: ', n)
        for indices in itertools.product(range(n), repeat=r):
            if sorted(indices) == list(indices):
                file.write(str(tuple(pool[i] for i in indices)) + '\n')
                #yield tuple(pool[i] for i in indices)
