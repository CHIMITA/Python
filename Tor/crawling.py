import requests #Http 호출 라이브러리 
import re #정규표현식 모듈

from bs4 import BeautifulSoup

list = []
    
session = requests.session() # session 활성화
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

url = 'http://wiki47qqn6tey4id7xeqb6l7uj6jueacxlqtk3adshox3zdohvo35vad.onion/'
     
page = session.get(url)
soup = BeautifulSoup(page.content, "lxml")
    
p = soup.find("div", class_="box-info")

print("[.Onion site list]\n")

for div in p.find_all("div", class_="box-info-detail"):
    for a in p.find_all("a",{"class":"site-heading"}):
        
        list = soup.find_all("strong")
    
        t = re.compile('(?<=\<strong>)(.*?)(?=<\/strong>)') # 메타문자 
       
        t_list = t.findall(str(list)) 
      
    print("[.Onion site list]\n", t_list)