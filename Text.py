from tkinter import *
from tkinter import messagebox
from random import randint
clik = 0
def xy():
    x1= randint(1, 550)
    y1 = randint(1, 600)
    button.place_configure(x=x1,y=y1)
    global clik
    clik = clik + 1
    button.configure(text=clik)
    if clik == 20:
        messagebox.showinfo('you win')
    elif clik > 20:
        root.destroy()
    

root = Tk()
root.geometry('600x630')

button = Button(text = 'Click', bg = 'orange', width = 10,height = 2,command=xy)
button.place(x=100, y = 200)
 
root.mainloop()