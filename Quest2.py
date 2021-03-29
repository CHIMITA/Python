#도전문제 1
a,b,c = map(int,input("3개의 숫자를 입력하세요 :").split(','))

def sum(a,b,c):
    sum = a + b + c
    return a+b+c
    
def squared(a,b,c):
    squar = a ** 2 + b ** 2 + c ** 2
    return a ** 2 + b ** 2 + c ** 2

def diffsum(a,b,c):
    sum = a + b + c
    squar = a ** 2 + b ** 2 + c ** 2

    if(sum > squar >= 0):
        return sum - squar
    else:
        return squar - sum

print(sum(a,b,c))
print(squared(a,b,c))
print(diffsum(a,b,c))


