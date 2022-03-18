import csv
import matplotlib.pyplot as plt

f = open('C:\\Users\\User\\Python\\people.csv')
data = csv.reader(f)
result, x = [], []

yylist = [str(i) 
         for i in range(2019)]
yy = input("원하는 분야를 입력하세요! : ")
colidx = yylist.index(yy)
col = 1 + (6 * colidx)

for row in data:
    a = row[0].strip(' ')
    if a in ('특성별'):
        continue
    x.append(row[0].replace('특성별', ''))
    result.append(int(row[col].replace(',', '')))

plt.style.use('ggplot') #격자모양
plt.figure(figsize= (18,7))
plt.rc('font', family='malgun gothic')
plt.ylabel('2019')
plt.title(yy + '정보보호 IT투자', fontsize= 15, color= 'red')
plt.bar(x,result)
plt.show()