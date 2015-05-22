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

        self.lowerBool = IntVar()
        self.upperBool = IntVar()
        self.numberBool = IntVar()
        self.customBool = IntVar()
        self.manCharBool = IntVar()

        self.ckbLower = Checkbutton(text='lower case',variable=self.lowerBool).grid(row=1,column=0,padx=3 ,pady=3,sticky='W')
        self.ckbUpper = Checkbutton(text='UPPER CASE',variable=self.upperBool).grid(row=2,column=0,padx=3 ,pady=3,sticky='W')
        self.ckbNumeber = Checkbutton(text='Numbers',variable=self.numberBool).grid(row=3,column=0,padx=3 ,pady=3,sticky='W')
        self.ckbCustom = Checkbutton(text='Custom',variable=self.customBool,command=checkCustomToggle).grid(row=4,column=0,columnspan=2,padx=3 ,pady=3,sticky='W')

        self.txtCustom = Entry(width = 30,state='disabled')
        self.txtCustom.grid(row=5,column=0,columnspan=2,padx=25 ,pady=3,sticky='WSNE')
        self.txtCustom.bind('<Return>', setCustomCharacterSet)#

        self.ckbManChar = Checkbutton(text='Manditory Characters',variable=self.manCharBool,command=ckbManCharToggle).grid(row=6,column=0,columnspan=2,padx=3 ,pady=3,sticky='W')
        self.txtmandChar = Entry(width = 30,state='disabled')
        self.txtmandChar.grid(row=7,column=0,columnspan=2,padx=25 ,pady=3,sticky='WSNE')
        self.txtmandChar.bind('<Return>', setManditoryCharaters)

        self.lblLength = Label(text='Password Length:').grid(row=10,column=0,padx=25,pady=3,sticky='W')
        self.spbLength = Spinbox(from_=0, to=20)
        self.spbLength.grid(row=11,column=0,padx=25 ,pady=3,sticky='WSNE')

        #Listbox with the patterns

        self.lblPatterns = Label(text='Patterns: ').grid(row=0,column=4,columnspan=4,padx=3 ,pady=3,sticky='')

        self.lsbPatterns = Listbox(height=5,width=25)
        self.lsbPatterns.grid(row=1,column=4,rowspan=5,columnspan=4,padx=3 ,pady=3, sticky='WSNE')

        self.lblNewPattern = Label(text='New Pattern:').grid(row=6,column=4,padx=3,columnspan=4,pady=3)
        self.txtPattern = Entry(width=30)
        self.txtPattern.grid(row=7,column=4,columnspan=4,padx=3 ,pady=3,sticky='WSNE')

        self.lblBegin = Label(text='Begin').grid(row=10,column=4,padx=3 ,pady=3,sticky='WSNE')
        self.txtBegin = Entry(width=10)
        self.txtBegin.grid(row=10,column=5,padx=3 ,pady=3,sticky='WSNE')
        self.lblEnd = Label(text='End').grid(row=10,column=6,padx=3 ,pady=3,sticky='WSNE')
        self.txtEnd = Entry(width=10)
        self.txtEnd.grid(row=10,column=7,padx=3 ,pady=3,sticky='WSNE')

        self.btnAddPattern = Button(text='Add',command=addPattern).grid(row=11,column=4,columnspan=2,padx=3 ,pady=3,sticky='WSNE')
        self.btnRemovePattern = Button(text='Remove',command=removePattern).grid(row=11,column=6,columnspan=2,padx=3 ,pady=3,sticky='WSNE')

        # Generate Button
        self.v = StringVar()
        self.txtFilePath = Entry(width=30,textvariable=self.v)
        self.txtFilePath.grid(row=12,column=0,columnspan=7,padx=3 ,pady=3,sticky='WSNE')
        self.btnOpen = Button(text='...',command=openFile)
        self.btnOpen.grid(row=12,column=7,padx=3 ,pady=3,sticky='WSNE')
        self.btnGenerate = Button(text='Generate', font=10, command=generate).grid(row=13,column=0,rowspan=2,padx=3 ,pady=3,sticky='WSNE')

##################################   End of Class   ########################################

def setCustomCharacterSet(event):
    CharacterSets.setCustom(app.txtCustom.get())

def setManditoryCharaters(event):
    CharacterSets.setManditory(app.txtmandChar.get())

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

def ckbManCharToggle():
    if app.manCharBool.get() == 0:
        app.txtmandChar.configure(state='disabled')
    else:
        app.txtmandChar.configure(state='normal')

def openFile():
    file = filedialog.asksaveasfilename()
    app.v.set(file)
    print(file)

##################################   Main #################################

root = Tk()
root.geometry("600x400")
global app
app = MainFrame(root)
root.mainloop()



