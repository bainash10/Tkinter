from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get()) +" degrees C")

window = Tk()

scale=Scale(window,from_=100,to=0,
            length=600,
            orient=VERTICAL,  #orientation of scale
            font=('Consolas',20),
            tickinterval=10, #adds numeric indicators for value
            # showvalue=0, #hide current value
            resolution=5, #increment of slider
            troughcolor='#00FF00',
            fg='#FF1C00',
            bg='#111111'
            )

scale.set(((scale['from']-scale['to'])/2)+scale['to'])  #slider always on middle whatever will be the from and to value

scale.pack()

button=Button(window,text='submit',command=submit)
button.pack()

window.mainloop()