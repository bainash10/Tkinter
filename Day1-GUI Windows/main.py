from tkinter import *

#* widgets = GUI elements: buttons, textboxes, labels, images
#* windows = serves as a container to hold or contain these widgets

#!Remember always first import tkinter, assign Tk() to a variable and call variable.mainloop()

window=Tk() #instantiate an instance of a window

window.geometry("420x420")  #width x height--> size of the window to assign

window.title("Nischals window")  #changes the title of the window from tk to what assigned inside title method

# icon=PhotoImage(file='random.png')  #!for converting the icon in the window
# window.iconphoto(True,icon)


window.config(background="RED")

window.config(background="#5cfcff")




window.mainloop() #place window on computer screen, and listen for events-->create a window where we will further place geometrics and other graphics