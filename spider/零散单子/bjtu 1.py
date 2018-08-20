# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup


page = requests.get('http://eaie.bjtu.edu.cn/cms/item/?cat=105').content.decode()
soup = BeautifulSoup(page,'html.parser')

links = soup.find('ul', {'class': 'list'}).find_all('a')

for link in links:
    url = link.get('href')
    url = 'http://eaie.bjtu.edu.cn/' + url
    print(url)

    # page = requests.get(url).content.decode()
    # soup = BeautifulSoup(page, 'html.parser')

