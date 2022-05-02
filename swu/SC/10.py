def plus(a, b):
    sum = a + b
    return sum

i = int(input("1. 덧셈 , 2. 뺄셈 , 3. 곱셈 , 4. 나눗셈 , 5. 종료 "))

for i in range(i):
    if i == 1:
        a = int(input("숫자를 입력하세요 : "))
        b = int(input("숫자를 입력하세요 : "))
        plus(a, b)
