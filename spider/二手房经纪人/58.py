#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

def get_soup (url):
    page = requests.get(url,headers = headers).content.decode()
    soup = BeautifulSoup(page,'html.parser')
    return  soup
for i in range(1,141):
    url = 'https://broker.58.com/bj/list/pn'+ str(i) +'/?PGTID=0d00000c-0000-00b6-0bb6-6e13b0e32781&ClickID=1'
    print(url)
    soup = get_soup(url)
    infos = soup.find('ul',{'class':'house-list-wrap'}).find_all('li')

    for info in infos:
        url_single = info.find('a').get('href')
        url = 'https:' + url_single
        soup = get_soup(url)

        name = soup.find('div',{'class':'user-name'}).text
        tel = soup.find('div',{'class':'phone-btn'}).text
        print(name)
        print(tel)
