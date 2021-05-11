import requests
from bs4 import BeautifulSoup

url = 'https://search.shopping.naver.com/best100v2/main.nhn'
html = requests.get(url).text
bs4 = BeautifulSoup(html, 'html.parser')

table = bs4.find_all('a', {'class': '_popular_srch_lst_li'})

for tr in table:
    print(tr.text)