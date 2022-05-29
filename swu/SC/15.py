#실습
from cProfile import label
from tkinter import *


win = Tk()

label1 = Label(win, text="선택한 언어 : ", fg="pink")

def myfunc():
    if var.get() == 1:
        label1.configure(text="Python")
    elif var.get() == 2:
        label1.configure(text="C++")
    elif var.get() == 3:
        label1.configure(text="JAVA")

var = IntVar()

rb1 = Radiobutton(win, text="Python", variable=var, value=1, command=myfunc)
rb2 = Radiobutton(win, text="C++", variable=var, value=1, command=myfunc)
rb3 = Radiobutton(win, text="JAVA", variable=var, value=1, command=myfunc)

rb1.pack()
rb2.pack()
rb3.pack()

win.mainloop()