# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_try01.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from PyQt4.QtCore import SIGNAL, SLOT, pyqtSlot
import newTryBecause.Permutations
import newTryBecause.CharacterSet

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QWidget):
    def __init__(self):
        self.charSet = newTryBecause.CharacterSet.CharacterSet(False,False,False,"","")
        self.pwdLength = 1
        self.constraints = newTryBecause.CharacterSet.Constraints(self.pwdLength,self.charSet)
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(794, 535)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 371, 211))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.CharSetInput = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.CharSetInput.setObjectName(_fromUtf8("CharSetInput"))
        self.checkBox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.CharSetInput.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.CharSetInput.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.CharSetInput.addWidget(self.checkBox_3)
        self.checkBox_4 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.CharSetInput.addWidget(self.checkBox_4)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.CharSetInput.addWidget(self.lineEdit)
        self.checkBox_5 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.CharSetInput.addWidget(self.checkBox_5)
        self.lineEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.CharSetInput.addWidget(self.lineEdit_2)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(353, 10, 81, 421))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(409, 199, 371, 231))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.listOfConstraints = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.listOfConstraints.setObjectName(_fromUtf8("listOfConstraints"))
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.listOfConstraints.addWidget(self.label_5)
        self.listView = QtGui.QListView(self.verticalLayoutWidget_2)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.listOfConstraints.addWidget(self.listView)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(9, 229, 371, 61))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.lengthOfPwd = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.lengthOfPwd.setObjectName(_fromUtf8("lengthOfPwd"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.lengthOfPwd.addWidget(self.label)
        self.spinBox = QtGui.QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(50)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.lengthOfPwd.addWidget(self.spinBox)
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(9, 299, 371, 81))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.inputFileName = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.inputFileName.setObjectName(_fromUtf8("inputFileName"))
        self.checkBox_6 = QtGui.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.inputFileName.addWidget(self.checkBox_6)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.inputFileName.addWidget(self.label_2)
        self.lineEdit_3 = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.inputFileName.addWidget(self.lineEdit_3)
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(409, 9, 371, 185))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.inputConstraints = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.inputConstraints.setObjectName(_fromUtf8("inputConstraints"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.inputConstraints.addWidget(self.label_3)
        self.spinBox_2 = QtGui.QSpinBox(self.verticalLayoutWidget_5)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.inputConstraints.addWidget(self.spinBox_2)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.inputConstraints.addWidget(self.label_4)
        self.horizontalSlider = QtGui.QSlider(self.verticalLayoutWidget_5)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.inputConstraints.addWidget(self.horizontalSlider)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.inputConstraints.addWidget(self.label_6)
        self.lineEdit_4 = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.inputConstraints.addWidget(self.lineEdit_4)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.inputConstraints.addWidget(self.pushButton)
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(9, 389, 371, 41))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.outputstrem = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.outputstrem.setObjectName(_fromUtf8("outputstrem"))
        self.checkBox_7 = QtGui.QCheckBox(self.verticalLayoutWidget_6)
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.outputstrem.addWidget(self.checkBox_7)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 430, 771, 21))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 450, 771, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        #MainWindow.setCentralWidget(self.centralwidget)
        #self.MenuBar = QtGui.QMenuBar(MainWindow)
        #self.MenuBar.setGeometry(QtCore.QRect(0, 0, 794, 25))
        #self.MenuBar.setDefaultUp(False)
        #self.MenuBar.setObjectName(_fromUtf8("MenuBar"))
        #MainWindow.setMenuBar(self.MenuBar)
        #self.statusbar = QtGui.QStatusBar(MainWindow)
        #self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.setUpEvents()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.checkBox.setText(_translate("MainWindow", "lowercase", None))
        self.checkBox_2.setText(_translate("MainWindow", "uppercase", None))
        self.checkBox_3.setText(_translate("MainWindow", "numbers", None))
        self.checkBox_4.setText(_translate("MainWindow", "custom", None))
        self.checkBox_5.setText(_translate("MainWindow", "mandatory", None))
        self.label_5.setText(_translate("MainWindow", "constraints:", None))
        self.label.setText(_translate("MainWindow", "length:", None))
        self.checkBox_6.setText(_translate("MainWindow", "save in a file", None))
        self.label_2.setText(_translate("MainWindow", "file:", None))
        self.label_3.setText(_translate("MainWindow", "beginning of constraint", None))
        self.label_4.setText(_translate("MainWindow", "length of constraint", None))
        self.label_6.setText(_translate("MainWindow", "allowed characters", None))
        self.pushButton.setText(_translate("MainWindow", "add new constraint", None))
        self.checkBox_7.setText(_translate("MainWindow", "output-stream", None))
        self.pushButton_2.setText(_translate("MainWindow", "do it!!", None))

        #self.pushButton_2.clicked.connect(self.startPermutation)

    def setUpEvents(self):
        self.checkBox.stateChanged.connect(self.hallo)

    def setPwdLength(self,pwdlen):
        self.pwdLength = pwdlen

    def hallo(self):
        print("hallo")

    #def startPermutation(self):
    #    perm.permuteWithTree_Uli(0,"",0,"",5,charSet.mandatory)

