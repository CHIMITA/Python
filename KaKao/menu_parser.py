import requests
import re
import datetime
from datetime import date
from bs4 import BeautifulSoup

req = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_sly.hst&fbm=1&acr=1&ie=utf8&query=%EC%83%81%EC%9D%BC%EB%AF%B8%EB%94%94%EC%96%B4%EA%B3%A0%EB%93%B1%ED%95%99%EA%B5%90") #급식 사이트 주소 가져옴 

html = req.text #Html source code를 text형식으로 변환
soup = BeautifulSoup(html, 'html.parser') #BeautifulSoup으로 Html source code를 python 객체로 변환
menu_data = soup.select('.menu_info') #python 객체로 변환된 코드에서 .menu_info 요소 찾아냄

dt = datetime.datetime.now() #현재 날짜 라이브러리
today_dt = str(dt.month)+"월 "+str(dt.day)+"일 " + "[중식]" #date.today().strftime("%m{0} %d{1} %%").format(*'월일[중식]') %%[중식] 안들어감 
print(today_dt + "의 급식은?!\n")


for menu in menu_data: #이 menu는 인스턴스변수로 for문 안에서 동작, menu가 menu_data에 존재 할 때
    today = menu.select('strong')[0].text #python 객체로 변환된 Html 코드에서 strong 요소를 text형식으로 가져옴

    if today_dt in today: #today_dt가 today에 존재할 때
        listMenu = (menu.text).strip(". ").split(" ") #listMenu에 급식 메뉴값들 공백으로 나누고, 앞뒤 공백 제거

        for i in range(len(listMenu)-3): #급식 메뉴 수 만큼 반복
            if i == 0: 
                listMenu[3] = listMenu[0] + listMenu[1] + listMenu[2] + listMenu[3] #listMenu 3번째 공간에 listMenu[0:3] 의 값을 넣어줌
                del listMenu[:3] #listMenu[:3] 까지 제거
            print(listMenu[i]) #리스트 메뉴 출력



