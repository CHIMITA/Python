from tkinter import *

def event(btn): #이벤트 액션
    if btn == 'C':
        clear()
    elif btn == '=':
        rst = eval(entdata.get()) #eval() : 매개변수로 받은 expression을 문자열로 받아 실행
        clear()
        insert(0,rst)
    else:
        insert(END, btn)

def insert(key, val): #입력
    entdata.get()
    entdata.insert(key, val)

def clear(): #초기화
    entdata.get()
    entdata.delete(0, END)


win = Tk()
win.title("My Calculator")
win.geometry("270x125")
win.resizable(False,False) #resizeable(상하, 좌우) : 윈도우 창 크기 조절 가능 여부 

bt = ['7', '8', '9', '+', 'C',
      '4', '5', '6', '-', '%',
      '1', '2', '3', '*', '/',
      '0', '00', '.', '=', '']

i = 0
x = 5 

for b in bt:
    btn = Button(win, text=b, width=x, command=(lambda y = b: event(y)))
    btn.grid(row=i//x+1, column=i%x)
    i +=1

entdata = Entry(win, width=33, bg="skyblue")
entdata.grid(row=0, column=0, columnspan=x)

win.mainloop()

