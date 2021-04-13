#도전문제 

def days1(mon):
    if mon in (1, 3, 5, 7, 8, 10, 12):
        print(mon ,"월은 31일 입니다~")
    elif mon in (4, 6, 9, 11):
        print(mon ,"월은 30일 입니다~")
    elif mon > 12:
         print("댓츠 노노우 정확한 월을 입력해주세용")
    else:
        print(mon ,"월은 28일 입니다~")
    return
    

mon = int(input("월을 입력하세요! :"))

print(days1(mon))


#도전문제

def days2(yy_mm):
    yy = int(yy_mm[0:4])
    mm = int(yy_mm[4:6])

    if mm in (1,3,5,7,8,10,12):
        print(yy,"년",mm ,"월은 31일 입니다~")
    elif mm in (4,6,9,11):
        print(yy,"년",mm ,"월은 30일 입니다~")
    elif mm > 12:
        print("댓츠 노노우 정확한 월을 입력해주세용")
    else:
        if yy % 4 == 0 and yy % 100 == 0 and yy % 400 == 0:
            print(yy,"년",mm ,"월은 윤년으로 29일 입니다~")
        else:
            print(yy,"년",mm ,"월은 28일 입니다~")
    return 

yy_mm = input("년도와 월을 입력해주세용 (예: 200311) :")
print(days2(yy_mm))