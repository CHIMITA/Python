#정보보호학과 2022111321 박지원
#문제 3번 - 모듈.py

#넓이 구하는 함수
def square_a(square_h, square_l):
    sum = square_h * square_l
    print("사각형의 넓이는 ", sum, "입니다.")

    return sum

#둘레 구하는 함수
def square_r(square_h, square_l):
    sum = square_h + square_l * 2
    print("사각형의 둘레는 ", sum, "입니다.")