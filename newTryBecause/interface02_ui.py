# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_try01.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox
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
        self.saveInFile = False
        self.outputStream = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(794, 535)
        self.THEWINDOW = QtGui.QWidget(MainWindow)
        self.THEWINDOW.setObjectName(_fromUtf8("THEWINDOW"))
        self.verticalLayoutWidget = QtGui.QWidget(self.THEWINDOW)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 371, 211))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.CharSetInput = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.CharSetInput.setObjectName(_fromUtf8("CharSetInput"))
        self.cbx_lowerCase = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.cbx_lowerCase.setObjectName(_fromUtf8("cbx_lowerCase"))
        self.CharSetInput.addWidget(self.cbx_lowerCase)
        self.cbx_UpperCase = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.cbx_UpperCase.setObjectName(_fromUtf8("cbx_UpperCase"))
        self.CharSetInput.addWidget(self.cbx_UpperCase)
        self.cbx_numbers = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.cbx_numbers.setObjectName(_fromUtf8("cbx_numbers"))
        self.CharSetInput.addWidget(self.cbx_numbers)
        self.cbx_custom = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.cbx_custom.setObjectName(_fromUtf8("cbx_custom"))
        self.CharSetInput.addWidget(self.cbx_custom)
        self.linetxt_custom = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.linetxt_custom.setObjectName(_fromUtf8("linetxt_custom"))
        self.CharSetInput.addWidget(self.linetxt_custom)
        self.cbx_mandatory = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.cbx_mandatory.setObjectName(_fromUtf8("cbx_mandatory"))
        self.CharSetInput.addWidget(self.cbx_mandatory)
        self.linetxt_mandatory = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.linetxt_mandatory.setObjectName(_fromUtf8("linetxt_mandatory"))
        self.CharSetInput.addWidget(self.linetxt_mandatory)
        self.line = QtGui.QFrame(self.THEWINDOW)
        self.line.setGeometry(QtCore.QRect(353, 10, 81, 421))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.THEWINDOW)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(409, 239, 371, 191))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.listOfConstraints = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.listOfConstraints.setObjectName(_fromUtf8("listOfConstraints"))
        self.label_constraints = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_constraints.setObjectName(_fromUtf8("label_constraints"))
        self.listOfConstraints.addWidget(self.label_constraints)
        self.listView_constraints = QtGui.QListView(self.verticalLayoutWidget_2)
        self.listView_constraints.setObjectName(_fromUtf8("listView_constraints"))
        self.listOfConstraints.addWidget(self.listView_constraints)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.THEWINDOW)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(9, 229, 371, 61))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.lengthOfPwd = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.lengthOfPwd.setObjectName(_fromUtf8("lengthOfPwd"))
        self.label_length = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_length.setObjectName(_fromUtf8("label_length"))
        self.lengthOfPwd.addWidget(self.label_length)
        self.spinBx_lengthPwd = QtGui.QSpinBox(self.verticalLayoutWidget_3)
        self.spinBx_lengthPwd.setMinimum(1)
        self.spinBx_lengthPwd.setMaximum(50)
        self.spinBx_lengthPwd.setObjectName(_fromUtf8("spinBx_lengthPwd"))
        self.lengthOfPwd.addWidget(self.spinBx_lengthPwd)
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.THEWINDOW)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(9, 299, 371, 81))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.inputFileName = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.inputFileName.setObjectName(_fromUtf8("inputFileName"))
        self.cbx_saveInFile = QtGui.QCheckBox(self.verticalLayoutWidget_4)
        self.cbx_saveInFile.setObjectName(_fromUtf8("cbx_saveInFile"))
        self.inputFileName.addWidget(self.cbx_saveInFile)
        self.label_filePath = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_filePath.setObjectName(_fromUtf8("label_filePath"))
        self.inputFileName.addWidget(self.label_filePath)
        self.line_file = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.line_file.setObjectName(_fromUtf8("line_file"))
        self.inputFileName.addWidget(self.line_file)
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.THEWINDOW)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(409, 9, 371, 217))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.inputConstraints = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.inputConstraints.setObjectName(_fromUtf8("inputConstraints"))
        self.label_beginningConstraint = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_beginningConstraint.setObjectName(_fromUtf8("label_beginningConstraint"))
        self.inputConstraints.addWidget(self.label_beginningConstraint)
        self.spinBox_beginningConstraint = QtGui.QSpinBox(self.verticalLayoutWidget_5)
        self.spinBox_beginningConstraint.setObjectName(_fromUtf8("spinBox_beginningConstraint"))
        self.inputConstraints.addWidget(self.spinBox_beginningConstraint)
        self.label_lenConstraint = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_lenConstraint.setObjectName(_fromUtf8("label_lenConstraint"))
        self.inputConstraints.addWidget(self.label_lenConstraint)
        self.slider_lenConstraint = QtGui.QSlider(self.verticalLayoutWidget_5)
        self.slider_lenConstraint.setOrientation(QtCore.Qt.Horizontal)
        self.slider_lenConstraint.setObjectName(_fromUtf8("slider_lenConstraint"))
        self.inputConstraints.addWidget(self.slider_lenConstraint)
        self.label_allowedChars = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_allowedChars.setObjectName(_fromUtf8("label_allowedChars"))
        self.inputConstraints.addWidget(self.label_allowedChars)
        self.lineEdit_allowedChars = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.lineEdit_allowedChars.setObjectName(_fromUtf8("lineEdit_allowedChars"))
        self.inputConstraints.addWidget(self.lineEdit_allowedChars)
        self.button_addConstraint = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.button_addConstraint.setObjectName(_fromUtf8("button_addConstraint"))
        self.inputConstraints.addWidget(self.button_addConstraint)
        self.button_deleteConstraint = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.button_deleteConstraint.setObjectName(_fromUtf8("button_deleteConstraint"))
        self.inputConstraints.addWidget(self.button_deleteConstraint)
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.THEWINDOW)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(9, 389, 371, 41))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.outputstrem = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.outputstrem.setObjectName(_fromUtf8("outputstrem"))
        self.cbx_outputStream = QtGui.QCheckBox(self.verticalLayoutWidget_6)
        self.cbx_outputStream.setObjectName(_fromUtf8("cbx_outputStream"))
        self.outputstrem.addWidget(self.cbx_outputStream)
        self.line_2 = QtGui.QFrame(self.THEWINDOW)
        self.line_2.setGeometry(QtCore.QRect(10, 430, 771, 21))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.button_startButton = QtGui.QPushButton(self.THEWINDOW)
        self.button_startButton.setGeometry(QtCore.QRect(10, 450, 771, 31))
        self.button_startButton.setObjectName(_fromUtf8("button_startButton"))
        #MainWindow.setCentralWidget(self.THEWINDOW)
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
        self.cbx_lowerCase.setText(_translate("MainWindow", "lowercase", None))
        self.cbx_UpperCase.setText(_translate("MainWindow", "uppercase", None))
        self.cbx_numbers.setText(_translate("MainWindow", "numbers", None))
        self.cbx_custom.setText(_translate("MainWindow", "custom", None))
        self.cbx_mandatory.setText(_translate("MainWindow", "mandatory", None))
        self.label_constraints.setText(_translate("MainWindow", "constraints:", None))
        self.label_length.setText(_translate("MainWindow", "length of password:", None))
        self.cbx_saveInFile.setText(_translate("MainWindow", "save in a file", None))
        self.label_filePath.setText(_translate("MainWindow", "file:", None))
        self.label_beginningConstraint.setText(_translate("MainWindow", "beginning of constraint", None))
        self.label_lenConstraint.setText(_translate("MainWindow", "length of constraint", None))
        self.label_allowedChars.setText(_translate("MainWindow", "allowed characters", None))
        self.button_addConstraint.setText(_translate("MainWindow", "add new constraint", None))
        self.button_deleteConstraint.setText(_translate("MainWindow", "delete constraint", None))
        self.cbx_outputStream.setText(_translate("MainWindow", "output-stream", None))
        self.button_startButton.setText(_translate("MainWindow", "do it!!", None))
        self.linetxt_custom.setEnabled(False)
        self.linetxt_mandatory.setEnabled(False)

    def setUpEvents(self):
        # CHECKBOXES
        self.cbx_lowerCase.stateChanged.connect(self.setAlpha)
        self.cbx_UpperCase.stateChanged.connect(self.setAlphaBig)
        self.cbx_numbers.stateChanged.connect(self.setNum)
        self.cbx_custom.stateChanged.connect(self.enableCustom)
        self.cbx_mandatory.stateChanged.connect(self.enableMandatory)
        self.cbx_saveInFile.stateChanged.connect(self.setSaveFile)
        self.cbx_outputStream.stateChanged.connect(self.setOutputStream)

        # TEXTINPUT
        self.linetxt_custom.editingFinished.connect(self.setCustom)
        self.linetxt_mandatory.editingFinished.connect(self.setMandatory)
        self.line_file.fo

        # SPINBOXES
        self.spinBx_lengthPwd.editingFinished.connect(self.setPwdLen)

        # TODO

    def setPwdLength(self,pwdlen):
        self.pwdLength = pwdlen

    def setAlpha(self):
        self.charSet.setAlpha(False if self.cbx_lowerCase.checkState() == 0 else True)
        #print(self.charSet.alpha)

    def setAlphaBig(self):
        self.charSet.setAlphaBig(False if self.cbx_UpperCase.checkState() == 0 else True)
        #print(self.charSet.alphaBig)

    def setNum(self):
        self.charSet.setNum(False if self.cbx_numbers.checkState() == 0 else True)
        #print(self.charSet.num)

    def enableCustom(self):
        self.linetxt_custom.setEnabled(False if self.cbx_custom.checkState() == 0 else True)
        if not self.linetxt_custom.isEnabled():
            self.linetxt_custom.setText("")
            self.charSet.setCustom("")

    def setCustom(self):
        self.charSet.setCustom(self.linetxt_custom.text())
        #print(self.linetxt_custom.text())
        self.linetxt_custom.setText(self.charSet.getCustom())
        print(self.charSet.getCharSet())

    def enableMandatory(self):
        self.linetxt_mandatory.setEnabled(False if self.cbx_mandatory.checkState() == 0 else True)
        if not self.linetxt_mandatory.isEnabled():
            self.linetxt_mandatory.setText("")
            self.charSet.setMandatory("")

    def setMandatory(self):
        if len(self.linetxt_mandatory.text()) <= self.pwdLength:
            try:
                self.charSet.setMandatory(self.linetxt_mandatory.text())
            except ValueError as e:
                QMessageBox.warning(self,"ValueError!", str(e))
            #print("right")
        else:
            #print("wrong")
            QMessageBox.warning(self,"You Idiot", "it is not possible to have more mandatory characters than your password is long...")

    def setPwdLen(self):
        self.pwdLength = self.spinBx_lengthPwd.text()
        #print(self.pwdLength)

    def setSaveFile(self):
        self.pwdLength = (False if self.cbx_saveInFile.checkState() == 0 else True)
        #print(self.pwdLength)

    def setOutputStream(self):
        self.outputStream = (False if self.cbx_outputStream.checkState() == 0 else True)
        #print(self.outputStream)

    def setFile(self):
        print("traLaLa")