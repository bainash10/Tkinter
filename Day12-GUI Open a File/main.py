from tkinter import *
from tkinter import filedialog

def openFile():
    filepath=filedialog.askopenfilename(initialdir="D:\Python Revision for 100 Days\Day82-GUI Open a File",
    title="Open file ?",
    filetypes=(("text files","*.txt"),("all files","*.*")) #limiting the extensions to open
    )
    # print(filepath)
    file= open(filepath,'r')
    print(file.read())
    file.close()

window=Tk()

button=Button(text="Open",command=openFile)
button.pack()
window.mainloop()