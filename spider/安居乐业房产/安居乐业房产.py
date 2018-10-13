#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

def get_soup (url):
    page = requests.get(url,headers = headers).content.decode('gb2312',errors='ignore')
    soup = BeautifulSoup(page,'html.parser')
    return soup


url = 'http://f.51-maifang.com/index.php?caid=2&addno=1'
soup = get_soup(url)
print(soup.prettify())
cities = soup.find('ul',{'type':'ccid1'}).find('li').find('p').find_all('a')[:-8]
for city in cities:
    city_url = city.get('href')
    city_name = city.text
    print(url)

    # soup = get_soup(city_url)#定位到每个城市的页面，但还需确认要不要下一页
    #
    # next_urls = soup.find('div',{'class':'p_bar'}).find_all('a')
    # tag = next_urls[-1]
    # while tag.text == '|':  #如果有下一页，就获取下一页的url，调取获取信息的函数every_page_urls：所有处理在此函数中进行
    #     next_url = next_urls[-2].get('href')
    #     print(next_url)
    #     every_page_urls(next_url)





        #
        # for i in range(50):
        #     flag_url = flag_ur + '&ccid1=5019&page=' + str(i)
        #     if requests.get(flag_url) == 200:
        #         soup = get_soup(flag_url)
        #         input()











