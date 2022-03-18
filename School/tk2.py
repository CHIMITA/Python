from tkinter import *

win = Tk()

win.geometry("500x300")
win.title("Check")

C_Var1 = IntVar()
C_Var2 = IntVar

Check1 = Checkbutton(win, text="Check1", variable=C_Var1, onvalue=1, offvalue=0)
Check2 = Checkbutton(win, text="Check2", variable=C_Var2, onvalue=1, offvalue=0)

Check1.pack()
Check2.pack()

win.mainloop()