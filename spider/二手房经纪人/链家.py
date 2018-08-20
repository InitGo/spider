#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
def get_soup (url):
    page = requests.get(url,headers = headers).content.decode()
    soup = BeautifulSoup(page,'html.parser')
    return soup

for i in range(1,101):
    url = 'https://bj.lianjia.com/jingjiren/pg' + str(i) +'/'
    print(url)

    soup = get_soup(url)
    time.sleep(3)
    infos = soup.find('ul',{'class':'agent-lst'}).find_all('li')

    for info in infos:

        name = info.find('div',{'class':'agent-name'}).find('a',{'target':'_blank'}).find('h2').text
        year = info.find('div',{'class':'main-plate'}).text
        tel = info.find('div',{'class':'col-3'}).find('h2').text
        print(name,year,tel)
        f = open('lianjia.csv', 'a+', encoding='utf-8')
        f.write(name)
        f.write(',')
        f.write('联系方式:' + tel)
        f.write(',')
        f.write(year)
        f.write('\n')
        f.close()


