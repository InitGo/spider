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

    page = driver.get(url)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    return soup

for i in range(384,430):
    url = 'https://bj.5i5j.com/jingjiren/n' + str(i) + '/'
    print(url)

    soup = get_soup(url)
    infos = soup.find('div',{'class':'list-con-box'}).find_all('div',{'class':'agent-con-box clear'})
    for info in infos:
        name = info.find('span',{'class':'name'}).text
        year = info.find('p',{'class':'iconsleft'}).text
        tel = info.find('div',{'class':'contacty'}).find('span').text
        print(name,year,tel)
        f = open('5i5j-2.csv', 'a+', encoding='utf-8')
        f.write(name)
        f.write(',')
        f.write('联系方式:' + tel)
        f.write(',')
        f.write(year)
        f.write('\n')
        f.close()


