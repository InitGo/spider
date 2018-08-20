# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

page= requests.get('https://movie.douban.com/top250').content.decode()
soup = BeautifulSoup(page,'html.parser')
links = soup.find('ol',{'class':'grid_view'}).find_all('a')

for link in links:
    url=link.get('href')
    page = requests.get(url).content.decode()
    soup = BeautifulSoup(page, 'html.parser')

    title = soup.find('span',{'property':'v:itemreviewed'}).text
    print(title)



#title = soup.find_all().find('span',{'class':'title'}).text