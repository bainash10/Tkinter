from tkinter import *

def doSomething(event):
    print("Mouse Coordinates:" + str(event.x)+","+str(event.y))

window=Tk()

window.bind("<Button-1>",doSomething) #left click
window.bind("<Button-2>",doSomething) #scroll wheel
window.bind("<Button-3>",doSomething) #right click
# window.bind("<ButtonRelease>",doSomething) 
window.bind("<Enter>",doSomething) #enter the window i.e mouse entering position in window
window.bind("<Leave>",doSomething) #leave the window
window.bind("<Motion>",doSomething) #Where the mouse moved on window


window.mainloop()