__author__ = 'Shadow'

from tkinter import *


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.parent = parent

        self.initUI()

    def initUI(self):

        self.parent.title("pwgen")
        self.pack(fill=BOTH, expand=1)
        txtField = Entry(self,width = 20)
        txtField.pack(side = TOP)

def main():

    root = Tk()
    root.geometry("800x600")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()