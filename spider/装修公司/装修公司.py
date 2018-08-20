#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup





def get_soup (url):
    page = requests.get(url).content.decode()
    soup = BeautifulSoup(page,'html.parser')
    return  soup

def get_nexturl (soup):
    pages = soup.find('div', {'class': 'page'}).find_all('a')
    url_exist = pages[-1].text
    if url_exist == '下一页':
        url = pages[-1].get('href')
        print(url)
        return url
    else:
        return None

url = 'http://www.qizuang.com/city/'

soup = get_soup(url)
cities = soup.find('div',{'class':'p2 clearfix'}).find_all('div',{'class':'con1 acti'})[2:3]
for city in cities :
    city = city.find_all('div',{'class':'span1'})[2:]
    for cit in city:
        cit = cit.find('ul').find_all('li')[23:]
        for url in cit :
            url = url.find('a').get('href')
            url = url + '/compan/?p=1'
            #print(url)
            #每个城市的公司

            while url:
                 print(url)
                 soup = get_soup(url)  # 已经获取到每个城市某一页的soup
                 city_name = soup.find('div',{'class':'city'}).find('strong').text #获取城市名称
                 #print(city_name)
                 companies = soup.find('ul', {'class': 'gongslist'}).find_all('li')

                 for company in companies:
                     try:
                         u = company.find('a', {'class': 'company-link'}).get('href')
                         compage = get_soup(u)

                         name = compage.find('h1',{'class':'com-tit'}).text#获取公司名称

                         infos = compage.find('ul',{'class':'c-tab-send'})#获取公司信息：地址，电话1，电话2
                         att = infos.find('li', {'class': 'att'}).text
                         tel = infos.find('li',{'class':'tel'}).text
                         mob = infos.find('li',{'class':'mob'}).text
                         list = [name,att,mob,tel,]
                         print(list)
                         file_name =  city_name + '.csv'
                         f = open('/Users/zhongyi/Desktop/f/' + file_name, 'a+', encoding='utf-8')
                         for info in list:
                             f.write(info)
                             f.write(',')
                         f.write('\n')
                         f.close()

                     except AttributeError  :
                            pass
                 url = get_nexturl(soup)  # 获取下一页的url



