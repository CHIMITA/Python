#도전문제 

#차
def diffsum(a,b,c):
    sum1 = a + b + c
    sum2 = (a**2 + b**2+ c**2)

    diff = abs(sum1 - sum2) #절댓값 함수

    rv = str(sum1) + "와" + str(sum2) + "의 차는" + str(diff) + "입니다!" 
    
    return rv


a,b,c = map(int,input("숫자를 입력하세요~ :").split())
print(diffsum(a,b,c))

#합
def diffsum2(a,b,c):
    sum1 = a + b + c
    sum2 = (a**2 + b**2+ c**2)

    diff = abs(sum1 + sum2) #절댓값 함수

    rv = str(sum1) + "와" + str(sum2) + "의 합은" + str(diff) + "입니다!" 
    
    return rv


a,b,c = map(int,input("숫자를 입력하세요~ :").split())
print(diffsum2(a,b,c))