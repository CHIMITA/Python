#도전문제 21

def even_odd(a):

    if  a % 2 == 0:
        print("짝수입니다!")
    else:
        print("홀수입니다!")
        
a = int(input("숫자를 입력하세요! :"))
even_odd(a)