__author__ = 'Shadow'

from tkinter import *
import CharacterSets
import math



class Example(Frame): # WHY? example...really?

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.parent = parent

        self.listBox = Listbox(self)
        self.txtField = Entry(self,width = 20)

        self.initUI()

    def initUI(self):

        self.listBox.insert(1,"1")
        self.listBox.insert(2,"2")
        self.listBox.insert(3,"3")
        self.listBox.insert(4,"4")
        self.listBox.insert(5,"5")
        self.listBox.pack()

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