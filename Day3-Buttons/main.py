from tkinter import *

# button = you click it, then it does stuff

count=0
def click():
    global count
    count+=1
    print(f"You clicked the button {count} times!")

window=Tk()

photo=PhotoImage(file='Day73-Buttons/images.png')

button=Button(window,
              text="click me!",
              command=click,
              font=("Comic Sans", 30),
              fg="#00FF00",
              bg="black",
              activeforeground="#00FF00",
              activebackground="black",
              state=ACTIVE, #can also be DISABLED
              image=photo,
              compound='bottom'
              )
button.pack()


window.mainloop()