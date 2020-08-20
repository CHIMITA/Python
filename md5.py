import hashlib

 

for i in range(0,1000000000):

    if b"'='" in hashlib.md5(str(i).encode()).digest():     # bytes형태로 바꿔줌

        print('Found : {}'.format(i))