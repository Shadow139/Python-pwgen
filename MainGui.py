from tkinter import filedialog
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
        #self.pack(fill=BOTH, expand=1) # macht einen Fehler zusammen mit .grid()

        #characterSet
        self.lblCharSet = Label(text='Character Set: ').grid(row=0,column=0,padx=3 ,pady=3,sticky='')
        #self.txtCharSet = Entry(width = 30)
        #self.txtCharSet.grid(row=0,column= 1,padx=3 ,pady=3,sticky='')

        self.lowerBool = IntVar()
        self.upperBool = IntVar()
        self.numberBool = IntVar()
        self.customBool = IntVar()

        self.ckbLower = Checkbutton(text='lower case',variable=self.lowerBool).grid(row=1,column=0,padx=3 ,pady=3,sticky='W')
        self.ckbUpper = Checkbutton(text='UPPER CASE',variable=self.upperBool).grid(row=2,column=0,padx=3 ,pady=3,sticky='W')
        self.ckbNumeber = Checkbutton(text='Numbers',variable=self.numberBool).grid(row=3,column=0,padx=3 ,pady=3,sticky='W')
        self.ckbCustom = Checkbutton(text='Custom',variable=self.customBool,command=checkCustomToggle).grid(row=4,column=0,padx=3 ,pady=3,sticky='W')

        self.txtCustom = Entry(width = 30,state='disabled')
        self.txtCustom.grid(row=4,column=1,padx=3 ,pady=3,sticky='W')
        self.txtCustom.bind('<Return>', setCustomCharacterSet)

        #Listbox with the patterns

        self.txtPattern = Entry(width=30)
        self.txtPattern.grid(row=1,column=4,columnspan=4,padx=3 ,pady=3,sticky='')

        self.lblPatterns = Label(text='Patterns: ').grid(row=0,column=4,columnspan=4,padx=3 ,pady=3,sticky='')

        self.lsbPatterns = Listbox(height=5,width=25)
        self.lsbPatterns.grid(row=2,column=4,rowspan=5,columnspan=4,padx=3 ,pady=3, sticky='WSNE')

        self.btnAddPattern = Button(text='Add',command=addPattern).grid(row=8,column=4,columnspan=2,padx=3 ,pady=3,sticky='WSNE')
        self.btnRemovePattern = Button(text='Remove',command=removePattern).grid(row=8,column=6,columnspan=2,padx=3 ,pady=3,sticky='WSNE')


        # Generate Button
        self.v = StringVar()
        self.txtFilePath = Entry(width=30,textvariable=self.v)
        self.txtFilePath.grid(row=9,column=0,columnspan=2,padx=3 ,pady=3,sticky='WSNE')
        self.btnOpen = Button(text='...',command=openFile)
        self.btnOpen.grid(row=9,column=3,padx=3 ,pady=3,sticky='WSNE')
        self.btnGenerate = Button(text='Generate', font=10, command=generate).grid(row=9,column=4,columnspan=4,padx=3 ,pady=3,sticky='WSNE')

##################################  End of Class ########################################

def setCustomCharacterSet(event):
    CharacterSets.setCustom(app.txtCustom.get())

def generate():
    print('Button Generate click.')
    return

def addPattern():
    app.lsbPatterns.insert(END,app.txtPattern.get())

def removePattern():
    selection = app.lsbPatterns.curselection()
    if selection != None:
        app.lsbPatterns.delete(selection)

def checkCustomToggle():
    if app.customBool.get() == 0:
        app.txtCustom.configure(state='disabled')
    else:
        app.txtCustom.configure(state='normal')

def openFile():
    file = filedialog.asksaveasfilename()
    app.v.set(file)
    print(file)

##################################   Main #################################

root = Tk()
root.geometry("800x600")
global app
app = MainFrame(root)
root.mainloop()



