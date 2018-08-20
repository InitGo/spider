# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

for i in range(10):
    url = 'https://movie.douban.com/top250?start=%d' % (i * 25)
    #print(url)
    response = requests.get(url)#请求返回对象
    pagecontent=response.content.decode()#返回响应内容
    soup = BeautifulSoup(pagecontent, 'html.parser')
    movie_list = soup.find('ol', {'class': 'grid_view'}).find_all('li')
    for movie in movie_list:
        title = movie.find_all('span', {'class': 'title'})[0].text
        mark = movie.find('span',{'class':'rating_num'}).text
        print(title,mark)

