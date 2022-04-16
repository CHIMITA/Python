#실습 01. 아래의 키와 값으로 student1이라는 이름으로 딕셔너리를 생성하세요.

from turtle import st


student = {'학번':'1000', '이름':'홍길동', '학과':'컴퓨터학과'}
print(student)

student['연락처'] = '010-1111-2222'
print(student)

del student['학과']
print(student)

print(student.get('이름'))

#실습 02. for 문을 활용해 아래의 딕셔너리의 모든 값을 출력하세요.

singer = {}

singer['이름'] = '트와이스'
singer['구성원 수'] = '9'
singer['데뷔'] = '서바이벌 식스틴'
singer['대표곡'] = 'SIGNAL'

print(singer)

for key in singer.keys():
    print(key, '->', singer[key])

#실습 03. 어느 커피숍에는 메뉴가 4가지 있다. Americano, Cafe latte, Green Tea latte, Mocha latte 
#        각 메뉴의 가격은 2000원, 2500원, 3000원, 3500이다. 이 목록을 dictionary로 작성해보고 
#        Americano와 Vanila latte가 있는지 없는지 확인해 보세요.

cafe = {'Americano':'2000원', 'Cafe latte':'2500원', 'Green Tea latte':'3000원', 'Mocha latte':'3500원'}
print(cafe)

if 'Americano' and 'Vanila latte' in cafe:
    print('Americano와 Vanila latte가 카페에 있습니다.')
else:
    print('Americano는 있지만, Vanila latte가 카페에 없습니다.')

cafe['Vanila latte'] = '3000원'
print('cafe에 Vanila latte가 추가되었습니다.')

if 'Americano' and 'Vanila latte' in cafe:
    print('Americano와 Vanila latte가 카페에 있습니다.')


print('Americano' in cafe.keys())
print('Vanila latte' in cafe.keys())


