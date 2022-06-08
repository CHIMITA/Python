import hashlib

string = input("암호화 할 문자열을 입력하세요 : ")

sha = hashlib.new('sha256')
sha.update(string.encode())
print("결과", sha.hexdigest())