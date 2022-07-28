#두개의 소수 선언
p = 991
q = 997

#두 소수의 계수
n = p * q

#오일러의 피 함수 구하기
totient = (p - 1) * (q - 1)

#유클리드 호제법 사용해 최대공약수 구하기
def gcd(a, b):
    while b!= 0:
        a, b = b, a % b
    return a

#1 < e < totient, gcd(e, totient)가 1인 e를 구하기
# e는 공개키
def getPublicKey(tot):
    e=2
    while e < tot and gcd(e, tot)!= 1:
        e += 1
    return e

# ed를 (p - 1) * (q - 1)로 나눈 나머지가 1이 아니거나 d가 e이면 d의 값을 1씩 증가시킨다. 
# 위의 조건을 만족시키지 않을때, d값을 반환
def getPrivateKey(e, tot):
    d = 1
    while (e * d) % tot != 1 or d == e:
        d += 1
    return d

#암호화
def encrypt(pk, plaintext):
    key, n = pk
    
    # c = m^e % n 
    cipher = [(ord(char) ** key) % n for char in plaintext] #ord() : 문자를 인자로 받아 해당하는 유니코드 정수 값을 반환

    return cipher

#복호화
def decrypt(pk, ciphertext):
    key, n = pk
  
    # m = (c*d)%n
    plain = [chr((char ** key) % n) for char in ciphertext] #chr() : 정수를 인자로 받아 해당하는 유니코드 문자 값을 반환

    return ''.join(plain)

m = str(input("암호화 할 문자를 입력하세요:"))

e = getPublicKey(totient)

d = getPrivateKey(e, totient)

encryptMsg = encrypt((e, n), m)

print("암호화 된 문자 : ", ''.join(map(lambda x: str(x), encryptMsg)))

print("복호화 한 문자 : ", decrypt((d,n), encryptMsg))
