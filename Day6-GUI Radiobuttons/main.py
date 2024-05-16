 # radio button = similar to checkbox, but you can only select one from a group
from tkinter import *

food=["pizza","hamburger","hotdog"]

def order():
    if(x.get()==0):
        print("You ordered pizza!")
    if(x.get()==1):
        print("You ordered burger!")
    if(x.get()==2):
        print("You ordered hotdog!")
    else:
        print("What?")


window=Tk()

pizzaImage=PhotoImage(file='Day76-GUI Radiobuttons/pizza.png')
burgerImage=PhotoImage(file='Day76-GUI Radiobuttons/burger.png')
hotdogImage=PhotoImage(file='Day76-GUI Radiobuttons/hotdog.png')
foodImages=[pizzaImage,burgerImage,hotdogImage]

x=IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],  #adds text to radio buttons
                              variable=x,  #groups radiobuttons together if they share the same variable
                              value=index, #assigns each radiobutton a different value
                              padx=25, #adds padding on x-axis
                              font=("Impact",50),
                              image= foodImages[index], #adds image to radiobutton
                              compound='left', #adds image and text(left-side)
                              indicatoron=0, #eliminate circle indicators
                              width=375, #sets width of radiobuttons
                              command=order #set command of radiobutton to function
                              ) 

    radiobutton.pack(anchor=W)

window.mainloop()