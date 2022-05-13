#정보보호학과 2022111321 박지원
#문제 3번 

#모듈 호출
import square

#사용자에게 입력 받기
square_h = int(input("사각형의 가로 길이를 입력하시오. : "))
square_l = int(input("사각형의 세로 길이를 입력하시오. : "))

#모듈 사용
print("사각형의 넓이 : ",square.square_a(square_h, square_l))
print("사각형의 둘레 : ",square.square_r(square_h, square_l))



