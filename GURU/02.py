#과제 2번

a = int(input("점수를 입력하세요 : "))

if a >= 90:
    print("A", end='')
elif a >= 80:
    print("B", end='')
elif a >= 70:
    print("C", end='')
elif a >= 60:
    print("D", end='')
else:
    print("F", end='')

print("학점입니다. ^^")