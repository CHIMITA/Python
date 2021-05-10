import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import *

win = tkinter.Tk()


win.geometry("500x300")
win.resizable(True, True)
win.title("HELLO")

label = tkinter.Label(win, text="Python", width=10, height=5, fg="green", relief="solid")
label.pack() #pack() : 화면에 배치



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

#photo = tkinter.Photoimage(file="C:\\Users\\User\\Desktop\\puppy.png") 

c = Canvas(win, bg = "skyblue", height = 150, width = 200) #Canvas : 사진이나 다양한 형태의 그림 등을 표시하기 위해 사용


c.create_text(100, 70, text = "도형그리기 on canvas", fill = "black", font =("굴림", 15))

c.create_line(0,105,200,200, fill="gray90", width=2)
c.create_line(0,200,200,105, fill="gray90", width=2)


c.pack()

win.mainloop()