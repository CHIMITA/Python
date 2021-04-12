#재귀호출로 Factorial 

def factorial(n):
    if n == 1:
        return 1
    print(n, 'x ', end='')
    return n * factorial(n-1)

num = int(input("Factorial 숫자 입력 :"))
print("1=",format(factorial(num),','))
