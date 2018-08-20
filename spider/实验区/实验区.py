#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
headers = {
    'Set-Cookie':'domain=bj; expires=Sat, 18-Aug-2018 08:18:42 GMT; Max-Age=3600; path=/; domain=5i5j.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

driver = webdriver.Chrome()
def get_soup (url):
    time.sleep(1)
    page = driver.get(url)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    return soup

for i in range(166,200):
    url = 'https://bj.5i5j.com/jingjiren/n' + str(i) + '/'
    print(url)

    soup = get_soup(url)
    print(soup.prettify())
    infos = soup.find('div',{'class':'list-con-box'}).find_all('div',{'class':'agent-con-box clear'})
    print(infos)
    for info in infos:

        name = info.find('span',{'class':'name'}).text
        print(name)

    #     year = info.find('p',{'class':'iconsleft'}).text
    #     tel = info.find('div',{'class':'contacty'}).find('span').text
    #     print(name,year,tel)



