import tkinter

# 키 이름을 입력할 변수 선언
key = 0
# 키를 눌렀을 때 실행할 함수 정의
def key_down(e):
    global key # key을 전역 변수로 취급
    key = e.keysym # 눌려진 키 이름을 key에 대입

# 키를 눌렀다 뗐을 때 실행할 함수 정의
def key_up(e):
    global key # key을 전역 변수로 취급
    key = "" # key에 빈 문자열 대입

x = 400 # 캐릭터의 X 좌표를 관리할 변수
y = 300 # 캐릭터의 Y 좌표를 관리할 변수

# 실시간 처리를 수행할 함수 정의
def main_proc():
    global x, y # x, y를 전역 변수로 선언
   
    if key == "Left": # 왼쪽 방향키 눌렀다면 X 좌표 20 감소
        x -= 20
    if key == "Right": # 오른쪽 방향키 눌렀다면 X 좌표 20 증가
        x += 20
    canvas.coords("MYCHR", x, y) # 캐릭터 이미지 이동
    root.after(100, main_proc) # 0.1초 후 main_proc 함수 지정

        
root = tkinter.Tk()
root.title("캐릭터 이동")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=800, height=600, bg="lightgreen")
canvas.pack()
img = tkinter.PhotoImage(file="/Users/jiwon/Desktop/Python/swu/nose.png")
canvas.create_image(x, y, image=img, tag="MYCHR")
main_proc()
root.mainloop()
