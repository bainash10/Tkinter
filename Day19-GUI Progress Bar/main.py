from tkinter import *
from tkinter.ttk import *
import time

def start():
    tasks=10
    x=0
    while(x<tasks):
        time.sleep(0.1)
        bar['value']+=10
        x+=1
        percent.set(str(((x/tasks)*100))+"%")
        task.set(str(x)+"/"+str(tasks)+" tasks completed")
        window.update_idletasks()

window=Tk()

percent=StringVar()
task=StringVar()

bar=Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel=Label(window,textvariable=percent).pack()
taskLabel=Label(window,textvariable=task).pack()

button=Button(window,text="download",command=start).pack()

window.mainloop()