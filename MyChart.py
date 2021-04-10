from matplotlib import pyplot as plt

#McAfee Labs에서 공개한 2017년 네트워크 해킹 Top 8을 참고하여 작성했습니다.
'''
#조각내기
scores = [20, 20, 15, 13, 10, 4, 4, 14]
team = ['Browser', 'Brute Force', 'Denial of service', 'Worm', 'Malware', 'Web', 'Scan', 'Others']
colors = ['yellowgreen', 'lightBlue', 'lightcoral', 'palegoldenrod', 'Pink', 'lightsalmon', 'lightGray', 'lightGreen' ]
explode = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]

plt.pie(scores, labels=team, colors=colors, autopct='%.1f%%', startangle=90, counterclock=False, explode=explode)
plt.title('Network Hacking in 2017')
plt.savefig('PythonNetHAK.png')

'''

'''
#pie차트
scores = [20, 20, 15, 13, 10, 4, 4, 14]
team = ['Browser', 'Brute Force', 'Denial of service', 'Worm', 'Malware', 'Web', 'Scan', 'Others']
colors = ['yellowgreen', 'lightBlue', 'lightcoral', 'palegoldenrod', 'Pink', 'lightsalmon', 'lightGray', 'lightGreen' ]

plt.pie(scores, labels=team, colors=colors, autopct='%.1f%%', startangle=90)
plt.title('Network Hacking in 2017')
plt.savefig('PythonNetHAK.png')

'''
#도넛차트
scores = [20, 20, 15, 13, 10, 4, 4, 14]
team = ['Browser', 'Brute Force', 'Denial of service', 'Worm', 'Malware', 'Web', 'Scan', 'Others']
colors = ['yellowgreen', 'lightBlue', 'lightcoral', 'palegoldenrod', 'Pink', 'lightsalmon', 'lightGray', 'lightGreen' ]

plt.pie(scores, labels=team, colors=colors, autopct='%.1f%%', startangle=90, wedgeprops=dict(width = 0.6))
plt.title('Network Hacking in 2017')
plt.savefig('PythonNetHAK.png')
