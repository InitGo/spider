#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

def get_soup (url):
    page = requests.get(url).content.decode()
    soup = BeautifulSoup(page,'html.parser')
    return  soup


for i in range(1,100):

    url = 'http://sh.qizuang.com/company/?p=%d'%i
    print(url)

    soup = get_soup(url)
    city_name = soup.find('div', {'class': 'city'}).find('strong').text  # 获取城市名称
    # print(city_name)
    companies = soup.find('ul', {'class': 'gongslist'}).find_all('li')

    for company in companies:
        try:
            u = company.find('a', {'class': 'company-link'}).get('href')
            compage = get_soup(u)

            name = compage.find('h1', {'class': 'com-tit'}).text  # 获取公司名称

            infos = compage.find('ul', {'class': 'c-tab-send'})  # 获取公司信息：地址，电话1，电话2
            att = infos.find('li', {'class': 'att'}).text
            tel = infos.find('li', {'class': 'tel'}).text
            mob = infos.find('li', {'class': 'mob'}).text
            list = [name, att, mob, tel, ]
            print(list)

            file_name = '/Users/zhongyi/Desktop/f/' + city_name + '.csv'
            f = open(file_name, 'a+', encoding='utf-8')
            for info in list:
                f.write(info)
                f.write(',')
            f.write('\n')
            f.close()

        except AttributeError  :
            pass