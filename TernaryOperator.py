
a = 10 
b = 20

#and와 or을 이용한 3항 연산자
result = a == b and a-b or a+b 
print(result)

c = 10
d = 20

#if와 else를 이용한 3항 연산자
result = (a-b) if a == b else(a+b)
print(result)

#3항 연산자 활용
'''
list = [idx for idx in range(10)]
print(list)
'''
a = tuple(i for i in range(10) if i % 2 == 0)
b = [i for i in range(10) if i % 2 == 0]
c = list(i for i in range(10) if i % 2 == 0)

print(a)
print(b)
print(c)

lista = [i if i < 6 else i + 10 for i in range(10)]
print(lista)

a = 'test'
print('Right') if a == 'test' else print('Wrong')


mylist = [4, 8, 3, 9]
a = [i for i in mylist if i < 5]
print(a)

a = [x if x <5 else '0' for x in mylist]
print(a)

a = [x if x < 5 else '*' for x in mylist]
print(a)