'''
a, b, c = map(int, input('생년월일을 8자리 입력하세용 : ').split())

print('%d년\n%d월\n%d일' % ( a, b, c ))

if a >= 2000:
    print('21세기 사람이군용')

else:
    print('20세기 사람이군용')

'''

a = input('생년월일 8자리를 입력하세용 : ')


b = a[0:4] + '년\n'
c = a[4:6] + '월\n'
d = a[6:8] + '일'


print(b,c,d)

if a[0:4] >= '2000':
    print('21세기 사람이군용')

else:
    print('20세기 사람이군용')