from tkinter import *
import tkinter as tk

root = tk.Tk()

key = 0

x = 0
y = 0

width = 610
height= 400

class Game():
    def noseShape(event):
        global nose
        img = tk.PhotoImage(file='/Users/jiwon/Desktop/Python/sochang/nose.png')
        nose = canvas.create_image(x, y, anchor=NW, image=img)

    def noseMove(event):
        global x
        if event.char == 'Left':
            x -= 10
            canvas.move(nose, x, y)
        elif event.char == 'Right':   
            x += 10
            canvas.move(nose, x, y)

        canvas.coords(x, y)

        canvas = tk.Canvas(bg = '#AD7167', width = width, height = height)
        canvas.pack()   
        
my_label = Label(root, text="")
my_label.config(text='위치는 : x| ' + str(x))
my_label.pack(pady=20)

root.bind("<Left>", Game.noseMove)
root.bind("<Right>", Game.noseMove)

root.title("리듬게임")

root.mainloop() 
