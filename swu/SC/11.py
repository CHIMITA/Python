#정보보호학과 2022111321 박지원
#문제 2번 

print("안녕하세요~ 커피가 맛있는 소창 카페입니다~!")
print("어떤 걸 주문하시겠어요?")
print("메뉴는 1. Americano,  2. Cafe mocha, 3. Cafe Latte, 4. Green Tea Latte 가 있습니다~")

inputMenu = int(input("이 메뉴로 할게요 : ")) # 주문할 메뉴 입력

print("네~ 사이즈는 어떻게 해드릴까요? 1. grande 2. regular 3. short 가 있습니다~")

inputSize = int(input("이 사이즈로 할게요 : ")) # 주문할 사이즈 입력

# 메뉴에 따른 금액을 계산하는 함수 
def price(i): # 매개변수를 입력 받아 저장
    americano = 3500
    cafeMocha = 4000
    cafeLatte = 4500
    greenteaLatte = 5000

    if i == 1: #i가 1 일때 아래 문장 실행
        return americano # americano 값 반환
    elif i == 2:
        return cafeMocha
    elif i == 3:
        return cafeLatte
    elif i == 4:
        return greenteaLatte
    
# 컵 사이즈 선택에 따른 금액을 계산하는 함수
def size(s): 
    grande = 1000
    regular = 500
    short = 0

    if s == 1: #s가 1 일때 아래 문장 실행
        return grande
    elif s == 2:
        return regular
    elif s == 3:
        return short
 
# 총 금액을 계산하는 함수(메뉴 + 사이즈)
def sum(i, s): # 매개변수 2개 입력 받아 저장
    sum = price(i) + size(s) # 위에서 정의한 함수 호출 후, 인수를 넘겨주어 실행
    print("총", sum, "원 입니다~")
    return sum

sum(inputMenu, inputSize) # 입력받은 인수를 매개변수 i, s에 넘겨주어 실행

