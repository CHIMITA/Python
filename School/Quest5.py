#도전문제 20

#덧셈
a = 12345
b = 7890

print("{:10,}".format(a))
print("+{:>9,}".format(b))

print("-" * 20)

print("+{:>10,}".format(a+b)) 

#뺄셈
a = 12345
b = 7890

print("{:10,}".format(a))
print("-{:>9,}".format(b))

print("-" * 20)

print("{:>10,}".format(a-b))

#나눗셈
c, d = map(int,input("숫자를 입력하세요! :").split(","))

print("{:10,}".format(c))
print("/{:>9,}".format(d))

print("-" * 20)

print("{:>10,}".format(c/d))

#나머지
c, d = map(int,input("숫자를 입력하세요! :").split(","))

print("{:10,}".format(c))
print("%{:>9,}".format(d))

print("-" * 20)

print("{:>10,}".format(c%d))