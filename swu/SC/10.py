# 정보보호학과 2022111321 박지원
# 문제 1번

def plus(a, b): #덧셈
    sum = a + b 
    print(round(sum, 1)) #결과 출력, round() 함수를 사용해 소수점 첫째자리까지 출력

def minus(a, b): #뺄셈
    sum = a - b
    print(round(sum, 1)) 

def multi(a, b): #곱셈
    sum = a * b
    print(round(sum, 1))

def division(a, b): #나눗셈
    sum = a / b
    print(round(sum, 1))



while(True):
    i = int(input("1. 덧셈 , 2. 뺄셈 , 3. 곱셈 , 4. 나눗셈 , 5. 종료 "))

    if i == 5: #선택한 수가 5일 때
        print("프로그램을 종료합니다.")
        break #반복문 탈출 후 프로그램 종료 

    a = float(input("숫자를 입력하세요 : ")) #나눗셈과 뺄셈 계산을 위해 소수점을 포함할 수 있는 float 사용
    b = float(input("숫자를 입력하세요 : "))
    
    if i == 1: #선택한 수가 1일 때 
        plus(a, b); #위에서 정의한 plus() 함수 호출, 인자값을 넣어줌으로써 입력한 수를 계산
   
    elif i == 2: #선택한 수가 2일 때
        minus(a, b) #위에서 정의한 minus() 함수 호출, 인자값을 넣어줌으로써 입력한 수를 계산
    
    elif i == 3: #선택한 수가 3일 때
        multi(a, b) #위에서 정의한 multi() 함수 호출, 인자값을 넣어줌으로써 입력한 수를 계산

    elif i == 4: #선택한 수가 4일 때
        division(a, b) #위에서 정의한 division() 함수 호출, 인자값을 넣어줌으로써 입력한 수를 계산
        
        
      
   