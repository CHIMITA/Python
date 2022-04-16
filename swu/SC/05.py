# 파이썬 심화 강의 02.pdf

#tuple
#읽기 전용 리스트. 변경 불가능

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'purple')
print(colors)

print(type(colors)) 
print(colors[1:3])

colors = sorted(colors) #tuple 은 원래 정렬이 안되지만, sorted 함수를 사용하면 정렬 할 수 있음. 이를 사용하면 list로 형이 변환됨.
print(colors)
print(type(colors))

#dictionary
#key와 value로 쌍으로 이루어진 자료구조
#{key : value} 형태로 선언, 범위 지정 에러 X, key는 중복 불가 - 중복되면 마지막 값 사용

phone_book = {'이준신':'010-2133-1234', '강준이':'010-1234-5678', '김지운':'010-2567-9877', '지시훈':'010-1234-7893'}
value = phone_book['지시훈']
print(value)
print(type(phone_book))

#.get을 사용하면 특정 값을 가져올 수 있음
value = phone_book.get('강준이') 
print(value)

#.get을 사용해 없는 값을 불러와도 에러가 발생하지 않음
value = phone_book.get('박지원') 
print(value)

if '김지운' in phone_book: #딕셔너리 안에 '' 값이 포함되어 있는지 in을 사용해 확인 
    print('김지운이 딕셔너리에 포함되어 있습니다.') #김지운이 있을 경우 
else:
    print('김지운이 딕셔너리에 없습니다.') #김지운이 없을 경우 

#딕셔너리에 값 추가
phone_book['민지원'] = '010-2345-1345' 
print(phone_book)

#딕셔너리 값 변경
phone_book['민지원'] = '010-5432-1234' 
print(phone_book)

#딕셔너리 값 삭제 [key]를 지정하지 않으면 딕셔너리 자체를 삭제
del phone_book['강준이'] 
print(phone_book)

#딕셔너리에서 특정 값을 빼내어 반환
item = phone_book.pop('이준신') 
print('이준신의 번호는 : ', item)
print(phone_book) #pop을 한 값은 딕셔너리에서 사라짐

# phone_book.clear 딕셔너리 항목 전체 삭제, 빈 딕셔너리를 남길 때 사용

#전체 키 조회
print(phone_book.keys())
print(list(phone_book.keys())) #딕셔너리 명 없이 출력

#전체 값 조회
print(phone_book.values())
print(list(phone_book.values())) #딕셔너리 명 없이 출력

#전체 항목 출력
print(phone_book.items())
print(list(phone_book.items())) #딕셔너리 명 없이 출력

for key in phone_book.keys():
    print(key, phone_book[key])

print('\nkey, value')

for key, value in phone_book.items():
    print(key,value)