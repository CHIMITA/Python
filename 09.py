# 실습 1

from traceback import print_tb


def plus(num1, num2):
    result = num1 + num2
    return result

hap = 0

hap = plus(200, 300)

print(hap)

# 실습 2

def print_n_times(n, value):
    for i in range(n):
        print(value)

print_n_times(5, "안녕하세요")

# 실습 3

def print_greeting(n, value):
    for i in range(n):
        print(value)

n = int(input("횟수를 입력하세요 : "))
print_greeting(n, "Hello, Python")

def square(num1, num2, num3, num4):
    result = num1 + num2 + num3 + num4
    return result

sum = square(2,3,2,3)

def sound(now, plus):
    now += plus
    return now

now_vol = 1
print("현재 볼륨 :", now_vol)
puls = int(input("증가 시킬 볼륨 : "))
print("볼륨이 " , sound(now_vol, puls), "로 변경되었습니다." )
