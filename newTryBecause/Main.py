__author__ = 'twi'

import itertools
import newTryBecause.Permutations
import newTryBecause.CharacterSet
from tkinter import messagebox
import newTryBecause.interface04_ui
from PyQt4 import QtCore, QtGui
import sys

if __name__ == '__main__':

    #filepath = "test.txt"

    #try:
    #    file = open(filepath,'w')
    #except IOError as e:
    #    print("IOError")

    #charSet = newTryBecause.CharacterSet.CharacterSet(False,False,False,"","")
    #pwdLength = 1
    #constraints = newTryBecause.CharacterSet.Constraints(pwdLength,charSet)

    #constraints.changeConstraint(0,"#")
    #constraints.changeConstraint(1,"a")
    #constraints.changeConstraint(2,"#")
    #constraints.changeConstraint(3,"a")
    #constraints.changeConstraint(4,"{b}")
    #print(constraints.constraints)
    #perm = newTryBecause.Permutations.Permutations(file,5,constraints,charSet)
    #perm.permuteWithTree_Uli(0,"",0,"",5,charSet.mandatory)

    app = QtGui.QApplication(sys.argv)
    ex = newTryBecause.interface04_ui.Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())