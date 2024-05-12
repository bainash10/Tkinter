# label = an area widget that holds text and/or an image within a window

from tkinter import *

window=Tk()

photo=PhotoImage(file='Day72-Labels/code.gif')

label=Label(window,
            text="Hello World! This is Nischal.", 
            font=('Arial',40,'bold'),
            fg='green',
            bg='#000000', 
            relief=RAISED,  #relief specifies the border style
            bd=10,
            padx=20, #padding x
            pady=20, #padding y
            image=photo,
            compound='bottom')
# label.place(x=100,y=10)  #shows the text defined in label into the specified coordinate
label.pack()  #shows in the window that is previewd when hit run

window.mainloop()