import csv
import matplotlib.pyplot as plt

f = open('C:\\Users\\User\\Python\\security.csv')
data = csv.reader(f)
result, x = [], []

yylist = [str(i) 
         for i in range(2011,2021)]
yy = input("원하는 연도를 입력하세요! : ")
colidx = yylist.index(yy)
col = 1 + (6 * colidx)

for row in data:
    a = row[0].strip(' ')
    if a in ('행정구역', '서울특별시'):
        continue
    x.append(row[0].replace('서울특별시', ''))
    result.append(int(row[col].replace(',', '')))

plt.style.use('ggplot') #격자모양
plt.figure(figsize= (18,7))
plt.rc('font', family='malgun gothic')
plt.ylabel('인구수')
plt.title(yy + '서울시 지역별 인구현황', fontsize= 15, color= 'red')
plt.bar(x,result)
plt.show()