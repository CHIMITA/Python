from matplotlib import pyplot as plt
'''
plt.plot([1,2,3], [110,130,120])
plt.show()

'''

'''
#제목과 x,y축 레이블
plt.plot(["Seoul", "Paris", "Seattle"], [30,25,55])
plt.xlabel('City')
plt.ylabel('Response')
plt.title('Experiment Result')
plt.savefig('pythonXY.png')

'''

'''

#범례추가
plt.plot([1,2,3], [1,4,9])
plt.plot([2,3,4], [5,6,7])
plt.xlabel('Sequence')
plt.ylabel('Time(secs)')
plt.title('Experiment Result')
plt.legend(['Mouse', 'Cat'])
plt.savefig('PythonLegend.png')

'''

'''
#Bar형식 차트
y = [5, 3, 7, 10, 9, 5, 3.5, 8]
x = range(len(y))
plt.bar(x,y, width=0.7, color="Pink")
plt.title('Bar Chart')
plt.savefig('PythonBar.png')

'''

#Pie형식 차트
scores = [87,43,70]
team = ['A', 'B', 'C']
colors = ['yellowgreen', 'skyblue', 'lightcoral']

plt.pie(scores, labels=team, colors=colors, autopct='%1.2f%%', startangle=90)
plt.title('Pie Chart')
plt.savefig('PythonPie')


