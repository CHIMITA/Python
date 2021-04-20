import time
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select


options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path='/Users/jiwon/Desktop/Python/KaKao/chromedriver')

driver.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%83%81%EC%9D%BC%EB%AF%B8%EB%94%94%EC%96%B4%EA%B3%A0%EB%93%B1%ED%95%99%EA%B5%90&oquery=%EC%83%81%EC%9D%BC%EB%AF%B8%EB%94%94%EC%96%B4%EA%B3%A0&tqi=hc0mxdprvh8ssD5eBVGssssss48-422181')

driver.implicitly_wait(10)

#driver.find_element_by_xpath('//*[@id="main_pack"]/section[1]/div/div[2]/div[1]/div[3]/ul/li[2]/a').click()
html=driver.page_source
soup=BeautifulSoup(html, "html.parser")


title = driver.find_element_by_class_name('menu_info')
print(title.text)

#table = driver.find_element_by_xpath('//*[@id="main_pack"]/section[1]/div/div[2]/div[1]/div[5]/div[7]/ul')
#print(table.text)

time.sleep(5)

driver.quit()
