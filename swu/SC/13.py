#실습

from tkinter import *
from tkinter import messagebox

win = Tk()

win.title("Python")

label1 = Label(win, text="Python")
label2 = Label(win, text="열정", font=('궁서체', 30), fg="red")
label3 = Label(win, text="쉿, 공부중", bg="yellow", width=50, height=10, anchor=SE)

label1.pack()
label2.pack()
label3.pack()

button = Button(win, text="파이썬 종료", fg="pink")
button.pack()

def myfunc():
    messagebox.showinfo("버튼", "누르고 싶지!?")

image = PhotoImage(file="/Users/jiwon/Desktop/티스토리/Tistory-001 (1).png")
button2 = Button(win, image=image, command=myfunc, fg="purple")
button2.pack()

win.mainloop()


