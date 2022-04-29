# 파이썬 기초 02 강의 

#조건식

from cmath import pi


score = 99

if score >= 90:
    print("성적은 A등급입니다.")
elif score >= 80:
    print("성적은 B등급입니다.")
elif score >= 70:
    print("성적은 C등급입니다.")
elif score >= 60:
    print("성적은 D등급입니다.")
else:
    print("성적은 F등급입니다.")

#중첩 if문

heigh = int(input("키를 입력하세요 : "))
age = int(input("나이를 입력하세요 : "))

if age >= 10:
    if heigh >= 150:
        print("탈 수 있습니다.")
    else:
        print("탈 수 없습니다.")
else:
    print("탈 수 없습니다.")

#나이를 입력 받아 20살이 넘으면 "당신은 성인입니다"를 출력하고, 10살 이상 20살 미만은 "당신은 청소년입니다"를 출력하고, 
# 10살 미만은 "당신은 어린이입니다"를 출력하는 프로그램을 작성하시오.

age = int(input("나이를 입력하시오."))

if age >= 10:
    if age < 20:
        print("당신은 청소년입니다.")
else:
    print("당신은 어린이입니다.")

#While문
#1~10 합 구하기 

i, sum = 0,0

i = 1

while i < 11:
    sum += i
    i += 1

print("1에서 10까지의 합은? : ", sum)

#실습 01. 사용자가 암호를 입력하고 프로그램에서 암호가 맞는지 체크하시오

password = ""

while password != "python":
    password = input("암호를 입력하시오 : ")

print("암호가 맞았습니다. 프로그램을 종료합니다. 암호 :", password)

#실습 02. 구구단 3단

num = 1

while num < 10:
    print('3 *', end='')
    print(num, end='')
    print('=', end='')
    print(3 * num)
    num += 1

#실습 03. 1~30까지의 정수를 출력하며 홀수인 경우 홀수, 짝수인 경우 짝수라고 출력하세요

num = 0
while num < 31:
    num += 1
    if num % 2 == 0:
        print(num, ' 짝수')
    else:
        print(num, ' 홀수')
        
