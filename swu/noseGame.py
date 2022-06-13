from cProfile import label
import tkinter
from tkinter import messagebox
import random
import time

# 키 이름을 입력할 변수 선언
key = 0

x = 400 # 캐릭터의 X 좌표를 관리 할 변수
y = 400 # 캐릭터의 Y 좌표를 관리 할 변수

rhythm_x1 = 0 # 리듬 노드의 X 좌표를 관리 할 변수
rhythm_x2 = 0 # 리듬 노드의 X 좌표를 관리 할 변수
rhythm_x3 = 0 # 리듬 노드의 X 좌표를 관리 할 변수
rhythm_x4 = 0 # 리듬 노드의 X 좌표를 관리 할 변수
rhythm_y = 0 # 리듬 노드의 Y 좌표를 관리 할 변수

score = 0 # 게임 점수 관리 할 변수

# 키를 눌렀을 때
def key_down(e):
    global key # key을 전역 변수로 취급
    key = e.keysym # 눌려진 키 이름을 key에 대입

# 키를 눌렀다 뗐을 때
def key_up(e):
    global key # key을 전역 변수로 취급
    key = "" # key에 빈 문자열 대입

# 실시간 처리를 수행할 함수
def nose_move():
    global x, y, key # x, y를 전역 변수로 선언

    # 다시 시작 부분
    
    if key == "Left": # 왼쪽 방향키 눌렀다면 X 좌표 20 감소
        x -= 15
        print("Lx : ",x)
    if key == "Right": # 오른쪽 방향키 눌렀다면 X 좌표 20 증가
        x += 15
        print("Rx: ",x)
    info()
    canvas.coords("MYCHR", x, y) # 캐릭터 이미지 이동
    root.after(100, nose_move) # 0.1초 후 main_proc 함수 지정

    
def rhythm_node():
    global rhythm_x, rhythm_y

    rhythm_x1 = random.randrange(100, 800, 100)
    rhythm_x2 = random.randrange(100, 800, 20)
    rhythm_x3 = random.randrange(100, 800, 10)
    rhythm_x4 = random.randrange(100, 800, 5)
    
    while(True):
        rhythm_y += 20 # 리듬이 내려오는 y 좌표 

        canvas.coords("node1", rhythm_x1, rhythm_y) # 리듬 이동
        canvas.coords("node2", rhythm_x2, rhythm_y) # 리듬 이동
        canvas.coords("node3", rhythm_x3, rhythm_y) # 리듬 이동
        canvas.coords("node4", rhythm_x4, rhythm_y) # 리듬 이동

        print("리듬 1", rhythm_x1, rhythm_y)
        print("리듬 2", rhythm_x2, rhythm_y)
        print("리듬 3", rhythm_x3, rhythm_y)
        print("리듬 4", rhythm_x4, rhythm_y)

        root.after(800, rhythm_node) # 0.1초 후 nose_move 함수 지정
        break
        

def info():
    if key == "Shift_L":
        x = 400
        y = 300
        score = 0
        
        messagebox.showinfo("알림", "다시 시작합니다.")    

def start_timer():
    if(running):
        global timer
        timer += 1
        timeText.configure(text=str(timer))

        if timer == 31:
            stop()
            game_over()

    root.after(1000, start_timer)

def start():
    global running
    running = True

def stop():
    global running
    running = False

def game_over():
    messagebox.showinfo("알림","게임 시간이 종료되었습니다.")   
    print("game over")
    quit()

def score_plus():
    global x, y, rhythm_x1, rhythm_x2, rhythm_x3, rhythm_x4, rhythm_y, score
    print("실행됨")
    while(True):
        if x == rhythm_x1 or x == rhythm_x2 or x == rhythm_x3 or x == rhythm_x4 or rhythm_y == y:
            if y == rhythm_x1 or y == rhythm_x2 or y == rhythm_x3 or y == rhythm_x4 or rhythm_x1 == y:
                print("닿았음")
                score += 10
        break    
    

root = tkinter.Tk()

running = False
timer = 0
timeText = tkinter.Label(root, text="경과 한 시간 : 0", font=("Helvetica", 80))
timeText.pack()


canvas = tkinter.Canvas(width=800, height=600, bg="lightgreen")
canvas.pack()

root.title("코끼리 코 리듬게임")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)


img = tkinter.PhotoImage(file="/Users/jiwon/Desktop/Python/swu/nose.png")
canvas.create_image(x, y, image=img, tag="MYCHR")


music_img1 = tkinter.PhotoImage(file="/Users/jiwon/Desktop/Python/swu/music1.png")
canvas.create_image(rhythm_x1, rhythm_y, image=music_img1, tag="node1")

music_img2 = tkinter.PhotoImage(file="/Users/jiwon/Desktop/Python/swu/music2.png")
canvas.create_image(rhythm_x2, rhythm_y, image=music_img2, tag="node2")

music_img3 = tkinter.PhotoImage(file="/Users/jiwon/Desktop/Python/swu/music3.png")
canvas.create_image(rhythm_x3, rhythm_y, image=music_img3, tag="node3")

music_img4 = tkinter.PhotoImage(file="/Users/jiwon/Desktop/Python/swu/music4.png")
canvas.create_image(rhythm_x4, rhythm_y, image=music_img4, tag="node4")

canvas.pack()


start()
start_timer()


nose_move()
score_plus()
rhythm_node()



label = tkinter.Label(root, text="점수 :" + str(score))
label.pack()
root.mainloop()
