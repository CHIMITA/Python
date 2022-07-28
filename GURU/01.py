#과제 1번

name = str(input("이름 입력 : "))
num = int(input("학번 입력 : "))
korean = int(input("국어점수 입력 : "))
math = int(input("수학점수 입력 :"))
english = int(input("영어점수 입력 : "))

avg = (korean + math + english) / 3

print("이름 : %s" % name)
print("학번 : %d" % num)
print("국어점수 : %d" % korean)
print("수학점수 : %d" % math)
print("영어점수 : %d" %  english)
print("평균점수 : %.2f" % avg)
