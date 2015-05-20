from tkinter.ttk import Style

__author__ = 'Shadow'

from tkinter import *
import CharacterSets


class MainFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent

        self.initUI()
    def initUI(self):

        self.parent.title("pwgen")
        #self.pack(fill=BOTH, expand=1)

        #characterSet
        self.lblCharSet = Label(text='Character Set: ').grid(row=0,column=0,padx=3 ,pady=3,sticky='')
        self.txtCharSet = Entry(width = 30)
        self.txtCharSet.grid(row=0,column= 1,padx=3 ,pady=3,sticky='')
        self.txtCharSet.bind('<Return>', setCustomCharacterSet)

        #Pattern input
        self.lblPattern = Label(text='Pattern Set: ').grid(row=1,column=0,padx=3 ,pady=3,sticky='')
        self.txtPattern = Entry(width = 30)
        self.txtPattern.grid(row=1,column= 1,padx=3 ,pady=3,sticky='')

        #Listbox with the patterns
        self.lsbPatterns = Listbox(height=5,width=25)
        self.lsbPatterns.insert(END, "Pattern1")
        self.lsbPatterns.insert(END, "Pattern2")
        self.lsbPatterns.insert(END, "Pattern3")
        self.lsbPatterns.insert(END, "Pattern4")
        self.lsbPatterns.insert(END, "Pattern5")
        self.lsbPatterns.grid(row=0,column=4,rowspan=5,columnspan=4,padx=3 ,pady=3, sticky='WSNE')

        self.btnAddPattern = Button(text='Add',command=addPattern).grid(row=6,column=4,columnspan=2,padx=3 ,pady=3,sticky='WSNE')
        self.btnRemovePattern = Button(text='Remove',command=removePattern).grid(row=6,column=6,columnspan=2,padx=3 ,pady=3,sticky='WSNE')


        self.btnGenerate = Button(text='Generate', font=10, command=generate).grid(row=7,column=4,columnspan=4,padx=3 ,pady=3,sticky='WSNE')

    def getTxtCharSet(self):
        return self.txtCharSet


##################################  End of Class ########################################

def setCustomCharacterSet(event):
    CharacterSets.setCustom(app.getTxtCharSet().get())

def generate():
    print('Button Generate click.')
    return

def addPattern():
    app.lsbPatterns.insert(END,app.txtPattern.get())

def removePattern():
    selection = app.lsbPatterns.curselection()
    if selection != None:
        app.lsbPatterns.delete(selection)

##################################   Main #################################

root = Tk()
root.geometry("800x600")
global app
app = MainFrame(root)
root.mainloop()



