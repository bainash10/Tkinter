from tkinter import *

def openFile():
    print("File has been opened")

def saveFile():
    print("File has been saved")

def cut():
    print("File has been cut")

def copy():
    print("File has been copied")

def paste():
    print("File has been paste")


window=Tk()

menubar=Menu(window)
window.config(menu=menubar)

fileMenu=Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)

editMenu=Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_cascade(label="Cut",command=cut)
editMenu.add_cascade(label="Copy",command=copy)
editMenu.add_cascade(label="Paste",command=paste)

window.mainloop()