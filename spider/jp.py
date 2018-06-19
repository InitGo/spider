# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

page = requests.get('http://eaie.bjtu.edu.cn/cms/item/?cat=105').content.decode()
soup = BeautifulSoup(page,'html5lib')
links = soup.find('ul', {'class': 'list'}).find_all('a')
for link in links:
    url = link.get('href')
    url = 'http://eaie.bjtu.edu.cn/' + url
    page = requests.get(url).content.decode()
    soup = BeautifulSoup(page, 'html5lib')
    title = soup.find('div', {'class': 'title'}).text
    content = soup.find('div', {'class': 'main_nr'}).text
    postime = soup.find('div', {'class': 'pull-right main_more'}).text
    print(title)
    print(content)
    print(postime)

page =