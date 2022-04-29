from tkinter import *

width = 1

def paint(event):
    x1 = event.x-1
    y1 = event.y-1
    x2 = event.x+1
    y2 = event.y+1

    canvas.create_oval(x1,y1,x2,y2, fill = "black", width=width)
    
win = Tk()

canvas = Canvas(win)

canvas.pack(expand=True, fill="both")

win.bind("<B1-Motion>", paint)


win.mainloop()