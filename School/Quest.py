
'''
#도전문제 1

player = [[], [], []]

for i in range(5):
    print("이름, 전화번호, 나이를 입력해주세요! :")

    player = input().split(',')
    
print(player)

'''

'''
#도전문제 2

name = 'Tom'
age = 13 

print("%s is %d years old!" % (name, age))

a = 10 
b = 3
sum = a/b

print('%d / %d = %.3f' % (a,b,sum))

c = 3
d = 12 
sum = c*d

print('%10d' % c)
print('x','%8d' % d)
print('-----------')
print('%10d' % sum)

'''

'''
#도전문제 3

num = int(input("숫자를 입력하세요! :"))



def evenodd(num):
    if num % 2 == 0:
        print('짝수네요~')
    else:
        print('홀수네요~')
    return num


print(evenodd(num))

'''

#도전문제 4

mon = input('달을 입력하세요! :')

def days(a):

    p_mon = ['1','3','5','7','8','10','12']
    _mon = ['4','6','9','11']


    year = [31, 30, 28]

    if a in p_mon:
        return year[0]
    elif a in _mon:     
        return year[1]
    elif a == '2':
        return year[2]  
  
        
print(days(mon))
    
