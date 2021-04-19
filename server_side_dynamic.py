from selenium import webdriver
import time

URL = ('https://stu.sen.go.kr/edusys.jsp?page=sts_m42320&returnDomain=B10'
        'schulCode=B100000586&schulCrseScCode=4&schulKndScCode=04'
        '&schMmealScCode=%d&schYmd=%s')
driver = webdriver.Chrome(executable_path=r"C:\Users\User\Python\KaKao\chromedriver.exe")
driver.get(url=URL)