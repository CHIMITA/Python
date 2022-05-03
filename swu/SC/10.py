def plus(a, b):
    sum = a + b
    print(sum)

def minus(a, b):
    sum = a - b
    print(sum)

def multi(a, b):
    sum = a * b
    print(sum)

i = int(input("1. 덧셈 , 2. 뺄셈 , 3. 곱셈 , 4. 나눗셈 , 5. 종료 "))

if i == 1:
    a = int(input("숫자를 입력하세요 : "))
    b = int(input("숫자를 입력하세요 : "))
    plus(a, b)
elif i == 2:
    a = int(input("숫자를 입력하세요 : "))
    b = int(input("숫자를 입력하세요 : "))
    minus(a,b)
elif i == 3:
    a = int(input("숫자를 입력하세요 : "))
    b = int(input("숫자를 입력하세요 : "))
    multi
elif i == 4:
    a = int(input("숫자를 입력하세요 : "))
    b = int(input("숫자를 입력하세요 : "))
    minus(a,b)
