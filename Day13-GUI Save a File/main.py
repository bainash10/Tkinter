from tkinter import *
from tkinter import filedialog

def saveFile():
    file=filedialog.asksaveasfile(
                                initialdir="D:\Python Revision for 100 Days\Day83-GUI Save a File",
                                defaultextension='.txt',
                                  filetypes=[
                                      ("Text File",".txt"),
                                      ("Html File",".html"),
                                      ("All Files",".*"),
                                  ])
    if file is None:
        return  #wont show any error when nothing is saved and crossed the window without any actions 

    filetext=str(text.get(1.0,END))
    # filetext=input("Enter some Text:")   #inplace of get function can use input function too
    file.write(filetext)
    file.close()


window=Tk()
button=Button(text='save',command=saveFile)
button.pack()
text=Text(window)
text.pack()
window.mainloop()