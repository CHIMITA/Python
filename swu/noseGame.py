
import tkinter
from tkinter import messagebox
import random

root = tkinter.Tk()
root.title("코끼리 코 리듬게임")
root.geometry("900x800")

# 키 이름을 입력할 변수 선언
key = 0

x = 400 # 캐릭터의 X 좌표를 관리 할 변수
y = 400 # 캐릭터의 Y 좌표를 관리 할 변수

# 리듬 노드의 좌표를 관리 할 변수
rhythm_x1 = 0 
rhythm_x2 = 0 
rhythm_x3 = 0 
rhythm_x4 = 0 
rhythm_y = 0

score = 0 # 게임 점수 관리 할 변수

running = False # 게임 실행중임을 나타내는 변수
timer = 0 # 게임 경과 시간 변수

# 이미지
canvas = tkinter.Canvas(width=800, height=600, bg="#6DC667")
canvas.pack()

nose = tkinter.PhotoImage(file="swu/nose.png")
canvas.create_image(x, y, image=nose, tag="nose")

halfNose1 = tkinter.PhotoImage(file="swu/halfNose.png")
canvas.create_image(x - 320, y + 100, image=halfNose1, tag="halfNose1")

halfNose2 = tkinter.PhotoImage(file="swu/halfNose.png")
canvas.create_image(x - 300, y + 100, image=halfNose2, tag="halfNose2")

halfNose3 = tkinter.PhotoImage(file="swu/halfNose.png")
canvas.create_image(x - 280, y + 100, image=halfNose3, tag="halfNose3")


music_img1 = tkinter.PhotoImage(file="swu/music1.png")
canvas.create_image(rhythm_x1, rhythm_y, image=music_img1, tag="node1")

music_img2 = tkinter.PhotoImage(file="swu/music2.png")
canvas.create_image(rhythm_x2, rhythm_y, image=music_img2, tag="node2")

music_img3 = tkinter.PhotoImage(file="swu/music3.png")
canvas.create_image(rhythm_x3, rhythm_y, image=music_img3, tag="node3")

music_img4 = tkinter.PhotoImage(file="swu/music4.png")
canvas.create_image(rhythm_x4, rhythm_y, image=music_img4, tag="node4")


# 키를 눌렀을 때
def key_down(e):
    global key # key을 전역 변수로 취급
    key = e.keysym # 눌려진 키 이름을 key에 대입


# 키를 눌렀다 뗐을 때
def key_up(e):
    global key # key을 전역 변수로 취급
    key = "" # key에 빈 문자열 대입

4
# 실시간 이동 함수
def nose_move():
    global x, y, key 

    if key == "Left": # 왼쪽 방향키 눌렀다면 X 좌표 20 감소
        x -= 15
        print("Lx : ",x)
    if key == "Right": # 오른쪽 방향키 눌렀다면 X 좌표 20 증가
        x += 15
        print("Rx: ",x)
    info()
    canvas.coords("nose", x, y) # 캐릭터 이미지 이동
    root.after(100, nose_move) # 0.1초 후 nose_move 함수 지정


def rhythm_node():
    global rhythm_x1, rhythm_x2, rhythm_x3,rhythm_x4, rhythm_y

    rhythm_x1 = random.randrange(100, 800, 100)
    rhythm_x2 = random.randrange(100, 800, 20)
    rhythm_x3 = random.randrange(100, 800, 10)
    rhythm_x4 = random.randrange(100, 800, 5)
    
    while(True):
        rhythm_y += 20 # 리듬이 내려오는 y 좌표 

        # 리듬 이동
        canvas.coords("node1", rhythm_x1, rhythm_y) 
        canvas.coords("node2", rhythm_x2, rhythm_y) 
        canvas.coords("node3", rhythm_x3, rhythm_y) 
        canvas.coords("node4", rhythm_x4, rhythm_y) 

        root.after(1000, rhythm_node) # 0.1초 후 rhythm_node 함수 지정
        break


# 다시 시작 함수       
def info():
    global x, y, score
    if key == "Shift_L":
        x = 400
        y = 300
        score = 0
        
        messagebox.showinfo("알림", "다시 시작합니다.")    


# 타이머 함수
def start_timer():
    if(running):
        global timer
        timer += 1
        timeText.configure(text="게임 경과 시간 :" +str(timer))

        if timer == 31:
            stop()
            game_over()

    root.after(1000, start_timer)


# 프로그램 시작하는 함수
def start():
    global running
    running = True


# 프로그램 멈추는 함수
def stop():
    global running
    running = False


# 게임 종료 함수
def game_over():
    messagebox.showinfo("알림","게임 시간이 종료되었습니다." 
                        + "\n게임 점수는 " + str(score) + " 점 입니다.\n축하합니다!")
    quit()


# 점수 더하는 함수
def score_plus():
    global x, y, rhythm_x1, rhythm_x2, rhythm_x3, rhythm_x4, rhythm_y, score

    while(True):
        if x == rhythm_x1 or x == rhythm_x2 or x == rhythm_x3 or x == rhythm_x4 or rhythm_y == y:
            print("닿았음")
            score += 10
            if y == rhythm_x1 or y == rhythm_x2 or y == rhythm_x3 or y == rhythm_x4 or rhythm_x1 == y:
                print("닿았음")
                score += 10
        break

    scoreText.configure(text="점수 : " + str(score))
    root.after(500, score_plus)


# 코 늘어나는 함수
def nose_half():
    global x, y, score

    half_X = x
    half_Y = y - 60
    
    if key == "Left": # 왼쪽 방향키 눌렀다면 X 좌표 20 감소
        half_X -= 15
    if key == "Right": # 오른쪽 방향키 눌렀다면 X 좌표 20 증가
        half_X += 15

    while(True):
        if score >= 50:
            half_Y -= 60
            
            canvas.coords("halfNose1", half_X, half_Y)
                
        if score >= 100:
            half_Y -= 80
            
            canvas.coords("halfNose2", half_X, half_Y)
        
        if score >= 150:
            half_Y -= 80
            canvas.coords("halfNose3",half_X, half_Y)
        
        root.after(100, nose_half)
       
        break


# 키 입력 이벤트 처리
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

# 시간
timeText = tkinter.Label(root, text="0", font=("Helvetica", 30), )
timeText.pack()

# 점수 
scoreText = tkinter.Label(root, text="0", font=("Helvetica", 30))
scoreText.pack()

noseText = tkinter.Label(root, text="코끼리 코 대기석", font=("Helvetica", 20))
noseText.place(x=80, y=610)

#함수 호출
start()
start_timer()
nose_move()
nose_half()
score_plus()
rhythm_node()

root.mainloop()