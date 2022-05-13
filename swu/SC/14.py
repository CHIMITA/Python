#실습

from tkinter import *
from tkinter import messagebox

win = Tk()

def myfunc():
    if chk.get() == 0:
        messagebox.showinfo("", "체크버튼이 꺼졌어요")
    else:
        messagebox.showinfo("", "체크버튼이 켜졌어요")

chk = IntVar()

cb1 = Checkbutton(win, text="눌러보세요", variable=chk, command=myfunc)
cb1.pack()

win.mainloop()