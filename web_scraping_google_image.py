# from selenium import webdriver

# chrome_driver_path = 'chromedriver.exe'
# driver=webdriver.Chrome()

# url = 'https://www.google.com/search?q=alize+lim&source=lnms&tbm=isch'
# driver.get(url)

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time

driver = webdriver.Chrome()

url = ("https://www.google.com/search?q={s}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568")
driver.get(url.format(s='Rafael Nadal'))

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(5)

imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'Q4LuWd')]")

src = []
for img in imgResults:
    src.append(img.get_attribute('src'))

# print(src)
# Download the first 10 images of search result
for i in range(10):
	urllib.request.urlretrieve(str(src[i]),"datasets/rafael_nadal/img{}.jpg".format(i))