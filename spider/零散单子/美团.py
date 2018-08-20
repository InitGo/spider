#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = 'http://bj.meituan.com/meishi/pn1/'

page = requests.get(url).content.decode()
soup = BeautifulSoup(page,'html.parser')

#print(soup.prettify())

infos = soup.find('div',{'class':'content clear'}).find('div',{'class':'left'})
print(infos)