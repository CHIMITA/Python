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

#실습 7. 비교연산자

a, b = 100, 200
print(a == b, a != b, a > b, a < b, a >= b, a <= b)

#실습 8. 논리연산자

a = 99
(a > 100) and (a < 200)
(a > 100) or (a < 200)
not(a == 100)

#실습 9. 논리연산자 - and (~이고, 그리고)

n1 = 10
n2 = 20
n3 = 30

(n1 < n3) and (n2 < n3)
(n1 > n3) and (n2 < n3)
(n1 > n3) and (n2 > n3)

#실습 9. 논리연산자 - or (~이거나, 또는)

n1 = 10
n2 = 20
n3 = 30

(n1 < n3) or (n2 < n3)
(n1 > n3) or (n2 < n3)
(n1 > n3) or (n2 > n3)


#실습 10. 논리연산자 - not (부정)

var = 10
var > 15
not(var > 15)
var < 15
not(var < 15)

#실습 11. if문 - 도어락의 비밀번호가 [1234]일 경우 "문이 열렸습니다" 문장 출력하기

password = input("비밀번호는 무엇인가요? : ")
if password == "1234":
    print("비밀번호가 일치하여, 문이 열립니다.")


#실습 12. if문 - 나이가 20살 이상인 경우 "당신은 성인입니다" 문장 출력하기

age = int(input("당신의 나이를 입력하시오 : "))
if age >= 20:
    print("당신은 성인이시군요")

#실습 13. if else문 - 사용자에게 숫자를 입력 받아 홀수인지 짝수인지 출력하기

a = int(input("숫자를 입력하세요 : "))
if a % 2:
    print("홀수입니다.")
else:
    print("짝수입니다.")

#실습 14. 보물상자에 비밀번호가 걸려 있다. 사용자에게 비밀번호를 입력 받아, 미리 정 해진 비밀번호(1234)와 일치하면 
#        “상자가 열렸습니다, 보물획득”을 출력하고, 틀린 경우 “비밀번호가 틀렸습니다“를 출력하는 프로그램을 작성해보자.

boxps = int(input("보물상자의 비밀번호를 입력하세요 : ")) 

if boxps == "1234":
    print("상자가 열렸습니다.")
else:
    print("비밀번호가 틀렸습니다.")

#실습 15. 놀이공원의 어린이용 놀이기구는 키는 155cm 이하, 몸무게는 50kg 이하의 제 한 조건이 있다고 한다. 
#        A의 키는 165cm, 몸무게는 60kg 이라면 이 어린이용 놀이기구를 탈 수 있는지 확인해보세요.

heigh = 155
weigh = 50

a_heigh = 165
a_weigh = 60

if heigh >= a_heigh and weigh >= 60:
    print("어린이용 놀이기구에 탈 수 있습니다.")
else:
    print("어린이용 놀이기구를 탈 수 없습니다.")

    