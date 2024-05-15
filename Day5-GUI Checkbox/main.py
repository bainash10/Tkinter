from tkinter import *

def display():
    if(x.get()==1):  #only use x.get()  if used boolean
        print("You agree!")

    else:
        print("You don't agree!")

window=Tk()

x=IntVar()  #if used true and fasle need to use BooleanVar()

python_photo=PhotoImage(file='Day75-GUI Checkbox/py.gif')

check_button = Checkbutton(window,
                           text= "I agree to something",
                           variable=x,
                           onvalue=1,  #can be True
                           offvalue=0, #can be False
                           command=display,
                           font=("Arial",20),
                           fg='#00FF00',
                           bg="black",
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound='left'
                           )
check_button.pack()

window.mainloop()