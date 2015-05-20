__author__ = 'Shadow'

from tkinter import *
import CharacterSets
import math



class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.parent = parent

        self.txtField = Entry(self,width = 20)

        self.initUI()

    def initUI(self):

        self.parent.title("pwgen")
        self.pack(fill=BOTH, expand=1)
        self.txtField.pack(side = TOP)
        self.txtField.bind('<Return>', setCustomCharacterSet)

    def getTextField(self):
        return self.txtField


def setCustomCharacterSet(event):
    CharacterSets.setCustom(app.getTextField().get())

def main():

    root = Tk()
    root.geometry("800x600")
    global app
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()