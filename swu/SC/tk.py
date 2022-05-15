from tkinter import *
import tkinter as tk

window = Tk()

window.title("Tkinter")

entry = tk.Entry(fg="gray19", bg="snow", width=20)
b='hello'
entry.insert(0,b)
entry.place(x=10,y=80)

window.mainloop()

