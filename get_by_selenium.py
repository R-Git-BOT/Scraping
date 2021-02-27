# coding:utf-8
import chromedriver_binary
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import datetime
import os
import re
import requests
import urllib
import urllib.request
import urllib.parse
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        }


def scraping(id, pw, url):
    options = webdriver.ChromeOptions()
    profile_path = 'F:\\DEV\\ntrIO\\py3\\scra\\chronium'
    options.add_argument('user-data-dir=' + profile_path)
    driver = webdriver.Chrome(executable_path='../../chromeD/chromedriver', options=options)
    

    driver.get(url)
    time.sleep(0.5)

    driver.find_element_by_tag_name('body').click()
    for i in range(20):
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)    
    # いったん落ち着かせます
    # elem_last = driver.find_element_by_xpath('//*[@id="root"]/div[5]/div[1]/div/div[3]/div/div/div[1]/div/div[5]/div[2]/a/div[1]')
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    
    html = driver.page_source

    elem_title = driver.find_elements_by_css_selector(".sc-1vjtieq-10.bhchCq")
    print(elem_title[0].text)
    elem_date = driver.find_element_by_xpath('//*[@id="root"]/div[5]/div[1]/div/div[3]/div/div/div[1]/div/article/div[2]/div/div[1]')
    print(elem_date.text)
    tdatetime = datetime.datetime.strptime(elem_date.text, '%Y年%m月%d日 %H:%M')
    tdate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)
    date_str = tdate.strftime('%Y-%m-%d')
    print(date_str)
    
    elem_author = driver.find_elements_by_xpath('//*[@id="root"]/div[5]/div[1]/div/div[1]/div/div/div[2]/div/div[1]/h1/a')

    hozon_place = "F:\\Video\\Fanbox-Fantia\\"
    authorname = hozon_place + elem_author[0].text
    filename = authorname + '\\' + date_str + "_" +  elem_title[0].text
    os.makedirs(filename, exist_ok=True)
    
    soup = bs(html, 'html.parser')
    images = soup.find_all("img")
    print(images)

    for i, img in enumerate(images):
        src = img['src']
        print(src)
        #img_name = re.search(".*\/(.*png|.*jpg|.*jpeg)$",src)
        iz = str(i).zfill(3)
        img_name = iz +'.' + src.rsplit('.',1)[1]
        image = requests.get(src).content
        with open(filename + "\\" + img_name, "wb") as f:
            print('downloading...')
            f.write(image)
            #f.write(image.content)
        time.sleep(1.0)
    
    driver.close()


# = input("input URL : ")
url = 'https://ponkotsu.fanbox.cc/posts/1346409'
USER = "rougebotthew"
PASS = "A1ka2!rgbot"
scraping(USER, PASS, url)