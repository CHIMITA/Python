import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/index.nhn'
html = requests.get(url).text
bs4 = BeautifulSoup(html, 'html.parser')

table = bs4.select_one('#realTimeRankFavorite')

for tr in table.select('a'):
    print(tr.text)