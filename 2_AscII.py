# FF, FE 값 초기화
FF = 1
FE = 0

#입력 받을 16진수를 띄어쓰기(공백)으로 구분하여 리스트 형태로 저장 
msg = list(input("변환할 16진수 입력 : ").split())

#잘 들어갔나 확인
#print(msg) 

#모든 16진수를 비교하기 위해 리스트 길이만큼 반복
for i in range(len(msg)):
    if msg[i] == "FF": #msg[i]값이 FF일 때
        print(FF)
    elif msg[i] == "FE": #msg[i]값이 FE일 때
        print(FE)