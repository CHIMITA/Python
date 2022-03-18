#도전문제 7
#txt파일 핸들링

#쓰기모드로 열기
file = open('hello.txt', 'w')
file.write('Hello, World!')
file.close()

#읽기모드로 열기
file = open('hello.txt', 'r') 
r = file.read()
print(r)

#자동으로 파일 객체 닫기
with open('hello.txt', 'r') as file:  
    r = file.read()
print(r)

#파일 수정하기
f = open('hello.txt', 'a') 
for i in range(2, 10+1):
    content = '\n' + str(i) + '번째 줄 입니다.'
    f.write(content)
f.close()


with open('hello.txt', 'r') as file:
    lines = file.readlines() #파일 내용을 한줄씩 리스트로 가져옴 
    print(lines)

#while문 이용
with open('hello.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line)
        print(line.strip('\n')) #파일에서 읽어온 문자열에서 \n 삭제하여 출력

#for문 이용
with open('hello.txt', 'r') as file:
    for line in file:
        print(line)
        #print(line.strip('\n'))
'''
with open('C:\\Users\\User\\Desktop\\words.txt', 'r') as file: #파이썬 경로 지정은 \\
    count = 0
    for word in file:
        if len(word.strip('\n')) <= 10:
            count += 1
    print(count)

'''

