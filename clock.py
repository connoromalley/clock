# clock app from a tiktok i watched

from tkinter import *
from time import strftime

myWindow = Tk()
myWindow.title('My Clock')

def time():
    myTime = strftime('%H:%M:%S %p')
    clock.config(text = myTime)
    clock.after(1000, time)

clock = Label(myWindow, font = ('arial', 30, 'bold'),
                                background = 'green',
                                foreground = 'white')

clock.pack(anchor = 'center')
time()

mainloop()
