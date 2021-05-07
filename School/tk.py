import tkinter
import tkinter as tk
from tkinter import messagebox

win = tkinter.Tk()


win.geometry("500x300")
win.resizable(True, True)
win.title("HELLO")

label = tkinter.Label(win, text="Python", width=10, height=5, fg="green", relief="solid")
label.pack()



def msg():
    msg_ = messagebox.showinfo("INFO", "HELLO EVERYONE!!!") 
    #showinfo: 평범한 정보 
    #showwarning: 경고 정보
    #showerror: 오류 정보 
    #askquestion: 사용자에게 질문 
    #askokcancel: ok,cancel 
    #askyesno: yes,no 
    #askretrycancel: ‘재시도’, ‘취소’


bt = tk.Button(win, width=10, height=10, text="PUSH!!", command=msg)
bt.place(x=50, y=50)

photo = tkinter.Photoimage(file="C:\\Users\\User\\Desktop\\puppy.png") 

win.mainloop()