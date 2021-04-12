
'''
도전문제 1

list_A = [1,3,5,7,10]

list_A.insert(5, 11)
list_A.insert(3, 6)

list_A[5:5] = [8,9]
print(list_A)
'''

'''
도전문제 2

list_B = [1,2,3,4,5,6,7,8]

num = int(input("숫자를 입력하세용 :"))

if num in list_B:
    print(list_B, "값이 리스트에 있네요!")
else:
    print("값이 리스트에 없습니당")

'''

'''
도전문제 3

girlFriend = ['소원', '예린', '유주', '신비', '엄지']

name = input("이름을 입력하세용 : ")

if name in girlFriend:
    name_idx = girlFriend.index(name)
    print(name_idx + 1, '번 째에 있습니당')

else:
    print("리스트에 없는 이름입니당")

'''

'''
도전문제4

a = []
a = input('숫자 5개를 입력 해주세용 :').split()

print('입력한 값의 최대값 :', max(a))
print('입력한 값의 최소값 :', min(a))

'''

'''
도전문제5
for num in range(100):
    if num % 4 == 0:
        print(num)

'''

'''
도전문제6
#문제 정확히 못들었ㅇ....

for num in range(100):
    if num % 6 == 0:
        print(num)
    elif num % 4 == 0:
        print(num)
    elif num % 12 == 0:
        print(num)

'''
