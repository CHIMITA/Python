
import requests #Http 호출 라이브러리 
import re #정규표현식 모듈
from bs4 import BeautifulSoup
import os
    
#session = requests.session() # session 활성화
#session.proxies = {}
#session.proxies['http'] = 'socks5h://localhost:9050'
#session.proxies['https'] = 'socks5h://localhost:9050'

url = "http://wiki47qqn6tey4id7xeqb6l7uj6jueacxlqtk3adshox3zdohvo35vad.onion/"

proxies ={
    'http' : 'socks5h://127.0.0.1:9150',
    'https' : 'socks5h://127.0.0.1:9150'
}

res = requests.get(url, proxies=proxies) # url로 get 요청과 프록시 설정값을 보내고 응답 받음

soup = BeautifulSoup(res.content, "lxml") 
    
p = soup.find("div", class_="box-info")

print("[.Onion site name list]\n")

for div in p.find_all("div", class_="space-10"):
    for a in p.find_all("a",{"class":"site-heading"}):
        
        list = soup.find_all("strong")
    
        t = re.compile('(?<=\<strong>)(.*?)(?=<\/strong>)') # 메타문자 
       
        t_list = t.findall(str(list)) 
        
del t_list[0:3] #onion 사이트 명이 아닌 다른 것이 출력되어서 삭제 
print("\n".join(t_list))

print("[.Onion site Link list]\n")

for href in soup.find("div", class_="box-info").find_all("a",{"class":"site-url"}):
    print(href["href"])
