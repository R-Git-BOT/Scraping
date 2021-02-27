# coding: UTF-8
import urllib.request
import urllib.error
import requests
import re
from pathlib import Path
from bs4 import BeautifulSoup


USER = "rgbot"
PASS = "satoshi3104"

session = requests.session()


# アクセスするURL
url = "https://www.pixiv.net/"
##url = "http://www.nikkei.com/"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(requests.get(url, headers = headers).content, "html.parser")

# タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
title_tag = soup.title

# 要素の文字列を取得する → 経済、株価、ビジネス、政治のニュース:日経電子版
title = title_tag.string

# タイトル要素を出力
# print(title_tag)

# タイトルを文字列を出力
print(title)

url = "https://accounts.pixiv.net/login"
soup = BeautifulSoup(requests.get(url, headers = headers).content, "html.parser")
title_tag = soup.title
title = title_tag.string
print(title)

payload = {
    'id': 'id',
    'password': 'password'
}
session.post(url, data = payload)

url = "https://www.pixiv.net/bookmark.php"
soup = BeautifulSoup(requests.get(url, headers = headers).content, "html.parser")
title_tag = soup.title
title = title_tag.string
print(title)

url = "https://www.fanbox.cc/@ponkotsu/posts/1187259"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")
title_tag = soup.title
title = title_tag.string

selector = "#root > div.sc-1spzamr-1.kHJYi > div.sc-1spzamr-2.fWSeZv > div > div.g8l3ju-0.jabdnZ > div > div > div.chf7b6-2.jLokm > div > article > div.sc-1vjtieq-17.bnlkzd > div.sc-1vjtieq-19.dlQSkX"
logout = '#root > div.sc-1spzamr-1.kHJYi > div.sc-1spzamr-2.fWSeZv > div > div.g8l3ju-0.jabdnZ > div > div > div.chf7b6-2.jLokm > div > article > div.sc-1vjtieq-17.bnlkzd > div > div > div.sc-1ofu41z-2.gWZFEn'

#print(soup.find('sc-1ofu41z-2 gWZFEn').get_text())

elems = soup.select(logout)
print(elems)

elems = soup.select('#root')
for elem in elems:
    print(elem)

'''
print(title)
print(soup.body)
topstories = soup.find('div', class_='sc-1ofu41z-2 gWZFEn')
print(topstories)
'''