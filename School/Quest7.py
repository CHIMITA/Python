#도전문제 10
def year(a):
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                print(a,"는/은 윤년입니다!")
            else:
                print(a,"는/은 평년입니다!")
        else:
            print(a,"는/은 윤년입니다!")
    else:
       print(a,"는/은 평년입니다!")
    return

b = int(input("년도를 입력하세요! :"))

print(year(b))

def year2(a):
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        print(a,"는/은 윤년입니다!")
    else:
        print(a,"는/은 평년입니다!")
    return

c = int(input("년도를 입력하세요! :"))
year2(c)