#파이썬 기초 강의 01.pdf 

#실습 1. 아래 코드를 형변화 하여 정수로 계산하시오.

from audioop import avg


x = input("첫 번째 숫자를 입력하세요 : ")
y = input("두 번째 숫자를 입력하세요 : ")

sum = x + y
print(sum)

#----------------------------정답------------------------------

x = int(input("첫 번째 숫자를 입력하세요 : "))
y = int(input("두 번째 숫자를 입력하세요 : "))

sum = x + y
print(sum)


#실습 2. 일년은 365일이다. 아래와 같이 실행 결과가 출력될 수 있도록 일년이 몇 주 인지 계산하는 프로그램을 만들어 보자.

days = 365
weeks = days//7

print("일년은", days, "일이고", weeks, "52주입니다!")


#실습 3. 아래의 화면과 같이 사칙연산을 하는 계산기 프로그램을 만들어 보자.

a = int(input("첫 번째 숫자를 입력하세요 : "))
b = int(input("두 번째 숫자를 입력하세요 : "))

result = a + b 
print(a, "+", b, "=", result)

result = a - b 
print(a, "-", b, "=", result)

result = a / b 
print(a, "/", b, "=", result)

result = a * b 
print(a, "*", b, "=", result)

#실습 4. 사용자에게 반지름을 입력 받아 원의 면적을 계산하는 프로그램을 만들어 보자.

pi = 3.14159
r = int(input("반지름을 입력하세요 :"))

si = pi * r * r

print("반지름 면적이", r, "인 원의 면적은 : ", si, "입니다.")


#실습 5. 사용자에게 국어, 영어, 수학, 과학 점수를 입력 받아 평균을 구하는 프로그램을 만들어 보자.

d1 = int(input("국어 점수를 입력하시오 : "))
d2 = int(input("영어 점수를 입력하시오 : "))
d3 = int(input("수학 점수를 입력하시오 : "))
d4 = int(input("과학 점수를 입력하시오 : "))

avg = (d1+d2+d3+d4)/4

print("성적 평균은 ", avg, "입니다!")

#실습 6. 우리나라의 부가 가치세는 10%이다. 물품 구매 총액을 입력했을 때, 부가 가치세를 계산하는 프로그램을 만들어 보자.

total = int(input("구매한 총 액 : "))

vat = total * 0.10
print("구매 총 액", total, "원의 부가가치세는", vat, "원입니다.")