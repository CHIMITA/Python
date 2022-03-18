import csv
import matplotlib.pyplot as plt

f = open('C:\\Users\\User\\Python\\콘텐츠산업.csv')

data = csv.reader(f)

result, x = [], []

for i, row in enumerate(data):
    if i ==0:
        for j in range(14):
            x.append(row[j+1])
    elif i == 1:
        continue
    elif i == 2:
        for j in range(14):
            result.append(int(row[j+1]))
    else:
        break

plt.style.use('ggplot')
plt.figure(figsize=(10,7))
plt.rc('font', family='malgun gothic')
plt.ylabel('인원') 
plt.title('콘텐츠 산업 종사자 현황', fontsize=15, color='green')  
plt.bar(x,result, color='skyblue')
plt.tight_layout(pad=1)
plt.show()