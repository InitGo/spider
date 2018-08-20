#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

def get_soup (url):
    page = requests.get(url).content.decode()
    soup = BeautifulSoup(page,'html.parser')
    return  soup


url = 'http://gy.qizuang.com/company/'


print(url)

soup = get_soup(url)
city_name = soup.find('div', {'class': 'city'}).find('strong').text  # 获取城市名称
# print(city_name)
companies = soup.find('ul', {'class': 'gongslist'}).find_all('li')[2:]

for company in companies:
    u = company.find('a', {'class': 'company-link'}).get('href')
    compage = get_soup(u)

    name = compage.find('h1', {'class': 'com-tit'}).text  # 获取公司名称

    infos = compage.find('ul', {'class': 'c-tab-send'}).find_all('li')  # 获取公司信息：地址，电话1，电话2
    att = infos[2].text
    print(att)
    tel = infos[0].text
    print(tel)
    mob = infos[1].text
    print(mob)
    list = [name, att, mob, tel, ]
    print(list)

    file_name = '/Users/zhongyi/Desktop/d/' + city_name + '.csv'
    f = open(file_name, 'a+', encoding='utf-8')
    for info in list:
        f.write(info)
        f.write(',')
    f.write('\n')
    f.close()

#except AttributeError  :
#    pass