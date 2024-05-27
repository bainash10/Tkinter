from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title='This is an info message box',message='You are a person')

    # messagebox.showwarning(title='Warning',message='You are a Virus')

    # messagebox.showerror(title='Error',message='Not responding :(')

    # if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):
    #     print('You did a thing!')
    # else:
    #     print('You cancelled a thing')


    # if messagebox.askretrycancel(title='ask ok askretrycancel',message='Do you want to retry the thing?'):
    #     print('You retried a thing!')
    # else:
    #     print('You cancelled a thing')

    # if messagebox.askyesno(title='ask yes or no',message="Do you like cake?"):
    #     print("I like cake too")

    # else:
    #     print("Why don't you like cake?")

    # print(messagebox.askquestion(title='ask question',message="Do you like pie?"))  #returns yes or no

    print(messagebox.askyesnocancel(title='Yes no cancel',message="DO you like to code?")) #returns true false or none

window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()