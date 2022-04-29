#실습 01. 리스트 

n = int(input('자연수 n: '))
sieve = [True] * (n + 1) #sieve 리스트를 True로 초기화 

for i in range(2, n + 1):
    if sieve[i] == True: #i가 소수인 경우
        print(i, end=' ') #소수 출력
        for j in range(i + i, n + 1, i):
            sieve[j] = False