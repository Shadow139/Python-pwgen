# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_try02.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox, QFileDialog
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
        self.dictSpecialConstraints = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(794, 632)
        self.THEWINDOW = QtGui.QWidget(MainWindow)
        self.THEWINDOW.setObjectName(_fromUtf8("THEWINDOW"))
        self.verticalLayoutWidget = QtGui.QWidget(self.THEWINDOW)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 371, 211))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.charSetInput = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.charSetInput.setObjectName(_fromUtf8("charSetInput"))
        self.checkbox_lowerCase = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkbox_lowerCase.setObjectName(_fromUtf8("checkbox_lowerCase"))
        self.charSetInput.addWidget(self.checkbox_lowerCase)
        self.checkbox_upperCase = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkbox_upperCase.setObjectName(_fromUtf8("checkbox_upperCase"))
        self.charSetInput.addWidget(self.checkbox_upperCase)
        self.ceckbox_numbers = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.ceckbox_numbers.setObjectName(_fromUtf8("ceckbox_numbers"))
        self.charSetInput.addWidget(self.ceckbox_numbers)
        self.checkbox_custom = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkbox_custom.setObjectName(_fromUtf8("checkbox_custom"))
        self.charSetInput.addWidget(self.checkbox_custom)
        self.linetext_custom = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.linetext_custom.setObjectName(_fromUtf8("linetext_custom"))
        self.charSetInput.addWidget(self.linetext_custom)
        self.checkbox_mandatory = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkbox_mandatory.setObjectName(_fromUtf8("checkbox_mandatory"))
        self.charSetInput.addWidget(self.checkbox_mandatory)
        self.linetext_mandatory = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.linetext_mandatory.setObjectName(_fromUtf8("linetext_mandatory"))
        self.charSetInput.addWidget(self.linetext_mandatory)
        self.line0 = QtGui.QFrame(self.THEWINDOW)
        self.line0.setGeometry(QtCore.QRect(353, 10, 81, 441))
        self.line0.setFrameShape(QtGui.QFrame.VLine)
        self.line0.setFrameShadow(QtGui.QFrame.Sunken)
        self.line0.setObjectName(_fromUtf8("line0"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.THEWINDOW)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(409, 239, 371, 211))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.listOfConstraints = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.listOfConstraints.setObjectName(_fromUtf8("listOfConstraints"))
        self.label_constraints = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_constraints.setObjectName(_fromUtf8("label_constraints"))
        self.listOfConstraints.addWidget(self.label_constraints)
        self.listview_constraints = QtGui.QListWidget(self.verticalLayoutWidget_2)
        self.listview_constraints.setObjectName(_fromUtf8("listview_constraints"))
        self.listOfConstraints.addWidget(self.listview_constraints)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.THEWINDOW)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(9, 229, 371, 61))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.lenOfPwdInput = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.lenOfPwdInput.setObjectName(_fromUtf8("lenOfPwdInput"))
        self.label_lenPwd = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_lenPwd.setObjectName(_fromUtf8("label_lenPwd"))
        self.lenOfPwdInput.addWidget(self.label_lenPwd)
        self.spinbox_lenPwd = QtGui.QSpinBox(self.verticalLayoutWidget_3)
        self.spinbox_lenPwd.setMinimum(1)
        self.spinbox_lenPwd.setMaximum(50)
        self.spinbox_lenPwd.setObjectName(_fromUtf8("spinbox_lenPwd"))
        self.lenOfPwdInput.addWidget(self.spinbox_lenPwd)
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.THEWINDOW)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(9, 299, 371, 101))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.fileNameInput = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.fileNameInput.setObjectName(_fromUtf8("fileNameInput"))
        self.checkbox_saveInFile = QtGui.QCheckBox(self.verticalLayoutWidget_4)
        self.checkbox_saveInFile.setObjectName(_fromUtf8("checkbox_saveInFile"))
        self.fileNameInput.addWidget(self.checkbox_saveInFile)
        self.label_filePath = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_filePath.setObjectName(_fromUtf8("label_filePath"))
        self.fileNameInput.addWidget(self.label_filePath)
        self.fileInput = QtGui.QHBoxLayout()
        self.fileInput.setObjectName(_fromUtf8("fileInput"))
        self.linetext_fileChooser = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.linetext_fileChooser.setObjectName(_fromUtf8("linetext_fileChooser"))
        self.fileInput.addWidget(self.linetext_fileChooser)
        self.button_fileChooser = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.button_fileChooser.setObjectName(_fromUtf8("button_fileChooser"))
        self.fileInput.addWidget(self.button_fileChooser)
        self.fileNameInput.addLayout(self.fileInput)
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.THEWINDOW)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(409, 9, 371, 217))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.constraintsInput = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.constraintsInput.setObjectName(_fromUtf8("constraintsInput"))
        self.label_beginningConstraint = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_beginningConstraint.setObjectName(_fromUtf8("label_beginningConstraint"))
        self.constraintsInput.addWidget(self.label_beginningConstraint)
        self.spinBox_beginningConstraint = QtGui.QSpinBox(self.verticalLayoutWidget_5)
        self.spinBox_beginningConstraint.setObjectName(_fromUtf8("spinBox_beginningConstraint"))
        self.constraintsInput.addWidget(self.spinBox_beginningConstraint)
        self.label_lenConstraint = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_lenConstraint.setObjectName(_fromUtf8("label_lenConstraint"))
        self.constraintsInput.addWidget(self.label_lenConstraint)
        self.slider_lenConstraint =  QtGui.QSpinBox(self.verticalLayoutWidget_5)
        #self.slider_lenConstraint.setOrientation(QtCore.Qt.Horizontal)
        self.slider_lenConstraint.setObjectName(_fromUtf8("slider_lenConstraint"))
        #self.slider_lenConstraint = QtGui.QSlider(self.verticalLayoutWidget_5)
        #self.slider_lenConstraint.setOrientation(QtCore.Qt.Horizontal)
        #self.slider_lenConstraint.setObjectName(_fromUtf8("slider_lenConstraint"))
        self.constraintsInput.addWidget(self.slider_lenConstraint)
        self.label_allowedChars = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_allowedChars.setObjectName(_fromUtf8("label_allowedChars"))
        self.constraintsInput.addWidget(self.label_allowedChars)
        self.linetxt_allowedChars = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.linetxt_allowedChars.setObjectName(_fromUtf8("linetxt_allowedChars"))
        self.constraintsInput.addWidget(self.linetxt_allowedChars)
        self.button_addConstraint = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.button_addConstraint.setObjectName(_fromUtf8("button_addConstraint"))
        self.constraintsInput.addWidget(self.button_addConstraint)
        self.button_deleteConstraint = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.button_deleteConstraint.setObjectName(_fromUtf8("button_deleteConstraint"))
        self.constraintsInput.addWidget(self.button_deleteConstraint)
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.THEWINDOW)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 410, 371, 41))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.outputstrem = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.outputstrem.setObjectName(_fromUtf8("outputstrem"))
        self.checkbox_outputStream = QtGui.QCheckBox(self.verticalLayoutWidget_6)
        self.checkbox_outputStream.setObjectName(_fromUtf8("checkbox_outputStream"))
        self.outputstrem.addWidget(self.checkbox_outputStream)
        self.line1 = QtGui.QFrame(self.THEWINDOW)
        self.line1.setGeometry(QtCore.QRect(10, 460, 771, 21))
        self.line1.setFrameShape(QtGui.QFrame.HLine)
        self.line1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line1.setObjectName(_fromUtf8("line1"))
        self.button_startButton = QtGui.QPushButton(self.THEWINDOW)
        self.button_startButton.setGeometry(QtCore.QRect(10, 550, 771, 31))
        self.button_startButton.setObjectName(_fromUtf8("button_startButton"))
        self.label_amntPwd = QtGui.QLabel(self.THEWINDOW)
        self.label_amntPwd.setGeometry(QtCore.QRect(10, 480, 241, 21))
        self.label_amntPwd.setObjectName(_fromUtf8("label_amntPwd"))
        self.label_amntMemory = QtGui.QLabel(self.THEWINDOW)
        self.label_amntMemory.setGeometry(QtCore.QRect(10, 520, 181, 20))
        self.label_amntMemory.setObjectName(_fromUtf8("label_amntMemory"))
        self.linetext_amntPwd = QtGui.QLineEdit(self.THEWINDOW)
        self.linetext_amntPwd.setGeometry(QtCore.QRect(260, 480, 113, 27))
        self.linetext_amntPwd.setObjectName(_fromUtf8("linetext_amntPwd"))
        self.linetext_amntMemory = QtGui.QLineEdit(self.THEWINDOW)
        self.linetext_amntMemory.setGeometry(QtCore.QRect(260, 520, 113, 27))
        self.linetext_amntMemory.setObjectName(_fromUtf8("linetext_amntMemory"))
        #MainWindow.setCentralWidget(self.THEWINDOW)
        #self.MenuBar = QtGui.QMenuBar(MainWindow)
        #self.MenuBar.setGeometry(QtCore.QRect(0, 0, 794, 25))
        #self.MenuBar.setDefaultUp(False)
        #self.MenuBar.setObjectName(_fromUtf8("MenuBar"))
        #MainWindow.setMenuBar(self.MenuBar)
        #self.statusbar = QtGui.QStatusBar(MainWindow)
        #self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #MainWindow.setStatusBar(self.statusbar)

        self.setUpEvents()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.checkbox_lowerCase.setText(_translate("MainWindow", "lowercase", None))
        self.checkbox_upperCase.setText(_translate("MainWindow", "uppercase", None))
        self.ceckbox_numbers.setText(_translate("MainWindow", "numbers", None))
        self.checkbox_custom.setText(_translate("MainWindow", "custom", None))
        self.checkbox_mandatory.setText(_translate("MainWindow", "mandatory", None))
        self.label_constraints.setText(_translate("MainWindow", "constraints:", None))
        self.label_lenPwd.setText(_translate("MainWindow", "length of password:", None))
        self.checkbox_saveInFile.setText(_translate("MainWindow", "save in a file", None))
        self.label_filePath.setText(_translate("MainWindow", "file:", None))
        self.button_fileChooser.setText(_translate("MainWindow", "....", None))
        self.label_beginningConstraint.setText(_translate("MainWindow", "beginning of constraint", None))
        self.label_lenConstraint.setText(_translate("MainWindow", "length of constraint", None))
        self.label_allowedChars.setText(_translate("MainWindow", "allowed characters", None))
        self.button_addConstraint.setText(_translate("MainWindow", "add new constraint", None))
        self.button_deleteConstraint.setText(_translate("MainWindow", "delete constraint", None))
        self.checkbox_outputStream.setText(_translate("MainWindow", "output-stream", None))
        self.button_startButton.setText(_translate("MainWindow", "do it!!", None))
        self.label_amntPwd.setText(_translate("MainWindow", "amount of passwords being generated:", None))
        self.label_amntMemory.setText(_translate("MainWindow", "amount of memory required:", None))
        self.linetext_custom.setEnabled(False)
        self.linetext_mandatory.setEnabled(False)

        self.linetext_amntMemory.setReadOnly(True)
        self.linetext_amntPwd.setReadOnly(True)
        
        self.spinBox_beginningConstraint.setValue(1)
        self.spinBox_beginningConstraint.setMinimum(1)
        self.spinBox_beginningConstraint.setMaximum(50)
        self.slider_lenConstraint.setValue(1)
        self.slider_lenConstraint.setMinimum(1)
        self.slider_lenConstraint.setMaximum(50)

    def setUpEvents(self):
        # CHECKBOXES
        self.checkbox_lowerCase.stateChanged.connect(self.setAlpha)
        self.checkbox_upperCase.stateChanged.connect(self.setAlphaBig)
        self.ceckbox_numbers.stateChanged.connect(self.setNum)
        self.checkbox_custom.stateChanged.connect(self.enableCustom)
        self.checkbox_mandatory.stateChanged.connect(self.enableMandatory)
        self.checkbox_saveInFile.stateChanged.connect(self.setSaveFile)
        self.checkbox_outputStream.stateChanged.connect(self.setOutputStream)

        # TEXTINPUT
        self.linetext_custom.editingFinished.connect(self.setCustom)
        self.linetext_mandatory.editingFinished.connect(self.setMandatory)

        # SPINBOXES
        self.spinbox_lenPwd.editingFinished.connect(self.setPwdLen)

        #Buttons
        self.button_fileChooser.clicked.connect(self.setFile)
        self.button_addConstraint.clicked.connect(self.addConstraint)
        self.button_deleteConstraint.clicked.connect(self.deleteConstraint)

    # YES - now it actually it does work
    def setPwdLen(self):
        self.pwdLength = self.spinbox_lenPwd.value()
        #print(self.pwdLength)
        self.constraints.updateConstraints(self.pwdLength,self.dictSpecialConstraints)
        #print(self.constraints.constraints)

    # YES - it's fine
    def setAlpha(self):
        self.charSet.setAlpha(False if self.checkbox_lowerCase.checkState() == 0 else True)
        #print(self.charSet.alpha)
        self.constraints.updateConstraints(self.pwdLength,self.dictSpecialConstraints)
        #print(self.constraints.constraints)

    # YES - works
    def setAlphaBig(self):
        self.charSet.setAlphaBig(False if self.checkbox_upperCase.checkState() == 0 else True)
        #print(self.charSet.alphaBig)
        self.constraints.updateConstraints(self.pwdLength,self.dictSpecialConstraints)
        #print(self.constraints.constraints)

    # YES - it's okay
    def setNum(self):
        self.charSet.setNum(False if self.ceckbox_numbers.checkState() == 0 else True)
        #print(self.charSet.num)
        self.constraints.updateConstraints(self.pwdLength,self.dictSpecialConstraints)
        #print(self.constraints.constraints)

    # YES - it disables and enables just right.. =D
    def enableCustom(self):
        self.linetext_custom.setEnabled(False if self.checkbox_custom.checkState() == 0 else True)
        if not self.linetext_custom.isEnabled():
            self.linetext_custom.setText("")
            self.charSet.setCustom("")
            self.constraints.updateConstraints(self.pwdLength,self.dictSpecialConstraints)
            #print(self.constraints.constraints)

    # YES - works too
    def setCustom(self):
        self.charSet.setCustom(self.linetext_custom.text())
        #print(self.linetxt_custom.text())
        self.linetext_custom.setText(self.charSet.getCustom())
        #print(self.charSet.getCharSet())
        self.constraints.updateConstraints(self.pwdLength,self.dictSpecialConstraints)
        #print(self.constraints.constraints)

    # YES - this thing works too
    def enableMandatory(self):
        self.linetext_mandatory.setEnabled(False if self.checkbox_mandatory.checkState() == 0 else True)
        if not self.linetext_mandatory.isEnabled():
            self.linetext_mandatory.setText("")
            self.charSet.setMandatory("")
            self.constraints.updateConstraints(self.pwdLength,self.dictSpecialConstraints)
            #print(self.constraints.constraints)

    # YES - at least I think...
    def setMandatory(self):
        if len(self.linetext_mandatory.text()) <= self.pwdLength:
            try:
                self.charSet.setMandatory(self.linetext_mandatory.text())
            except ValueError as e:
                QMessageBox.warning(self,"ValueError!", str(e))
            #print("right")
        else:
            #print("wrong")
            QMessageBox.warning(self,"You Idiot", "it is not possible to have more mandatory characters than your password is long...")
        #print(self.charSet.mandatory)
        self.constraints.updateConstraints(self.pwdLength,self.dictSpecialConstraints)
        #print(self.constraints.constraints)

    # YES - it does right things.
    def setSaveFile(self):
        self.saveInFile = (False if self.checkbox_saveInFile.checkState() == 0 else True)

    # YES - wooorking
    def setOutputStream(self):
        self.outputStream = (False if self.checkbox_outputStream.checkState() == 0 else True)
        #print(self.outputStream)

    # YES - and if not...wiktor did it
    def setFile(self):
        #print("traLaLa")
        self.linetext_fileChooser.setText(QFileDialog.getOpenFileName())

    def addConstraint(self):
        #print("addButtonClicked")
        if self.slider_lenConstraint.value()-1 + self.spinBox_beginningConstraint.value() <= self.pwdLength and self.checkCharsetStuff(self.linetxt_allowedChars.text()):
            #print("i got here")
            constraint = self.buildConstraint(self.linetxt_allowedChars.text())
            #print(constraint)
            x = self.spinBox_beginningConstraint.value()
            self.listview_constraints.clear()
            #print(x)
            #print(self.slider_lenConstraint.value())
            while x <= self.slider_lenConstraint.value()-1+self.spinBox_beginningConstraint.value():
                self.constraints.setConstraint(x,constraint)
                self.dictSpecialConstraints[x-1] = self.linetxt_allowedChars.text()
                #print(x)
                #print(constraint)
                #print(self.dictSpecialConstraints)
                #self.listview_constraints.addItem("lala")
                x += 1
            for i in self.dictSpecialConstraints.keys():
                self.listview_constraints.addItem("{0}: ".format(i+1) + self.dictSpecialConstraints[i])
                self.slider_lenConstraint.setValue(1)
                self.spinBox_beginningConstraint.setValue(1)
                self.linetxt_allowedChars.setText("")
        else:
            if self.slider_lenConstraint.value()-1 + self.spinBox_beginningConstraint.value() > self.pwdLength:
                QMessageBox.warning(self,"seriously?", "the password is too short for that..")
                self.slider_lenConstraint.setValue(1)
                self.spinBox_beginningConstraint.setValue(1)
            QMessageBox.warning(self,"You Idiot", "do it right")

    # das koennte schoener sein. machs schoener...
    def checkCharsetStuff(self,string):
        charSet = self.charSet.getCharSet()
        i = 0
        while i < len(string):
            #print("enter")
            if string[i] == "{":
                i += 1
                while not string[i] == "}":
                    if string[i] not in charSet:
                        QMessageBox.warning(self,"...", "please stop being so stupid. you cannot use letters that you do not have in your charset.")
                        return False
                    i += 1
                    if i > len(string):
                        QMessageBox.warning(self,"WHY", "you need a '}'.. but i guess you're too stupid for that")
                i += 1 # sollte das da sein...?
            elif string[i] == "A" and not self.charSet.alphaBig:
                QMessageBox.warning(self,"You Idiot", "uppercase can't be included if it's not in the charset")
                self.linetxt_allowedChars.setText("")
                return False
            elif string[i] == "a" and not self.charSet.alpha:
                QMessageBox.warning(self,"You Idiot", "lowercase can't be included if it's not in the charset")
                self.linetxt_allowedChars.setText("")
                return False
            elif string[i] == "0" and not self.charSet.num:
                QMessageBox.warning(self,"You Idiot", "numbers can't be included if they are not in the charset")
                self.linetxt_allowedChars.setText("")
                return False
            elif string[i] == "#" and (self.charSet.custom == "" or self.checkbox_custom.checkState() == 0):
                QMessageBox.warning(self,"?", "you know that you are not using any custom characters?")
                self.linetxt_allowedChars.setText("")
                return False
            elif string[i] != "A" and string[i] != "a" and string[i] != "0" and string[i] != "#":
                QMessageBox.warning(self,"You are a puking frog", "i dont even know what you are trying to achieve with this input")
                self.linetxt_allowedChars.setText("")
                return False
            i += 1
        return True

    # das koennte auch viel netter sein
    def buildConstraint(self,string):
        charSet = ""
        alpha = False
        alphaBig = False
        num = False
        custom = False
        i = 0
        while i < len(string):
            if string[i] == "{":
                while not string[i] == "}":
                    i += 1
                    charSet = self.charSet + string[i]
                i += 1 # richtig??
            if string[i] == "A" and not alphaBig:
                charSet += self.charSet.alphaBigF
            elif string[i] == "a" and not alpha:
                charSet += self.charSet.alphaF
            elif string[i] == "0" and not num:
                charSet = charSet + self.charSet.numF
            elif string[i] == "#" and not custom:
                charSet = charSet + self.charSet.custom
            i += 1
        return charSet

    def deleteConstraint(self):
        #print("delete-button clicked")
        indexes = self.listview_constraints.selectedItems()
        if indexes == []:
            QMessageBox.warning(self,"The other left!", "you have to select something to delete it!")
        else:
            for i in indexes:
                print("should do things")