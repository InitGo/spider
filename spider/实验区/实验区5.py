#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
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
        print('加载下一页：'+ url)

        return url
    else:
        return None

url = 'http://www.qizuang.com/city/'
soup = get_soup(url)
A_url = soup.find('div',{'class':'p2 clearfix'}).find_all('div',{'class':'con1 acti'})[4].find_all('div',{'class':'span1'})[0].find_all('li')
for url in A_url :

    url = url.find('a').get('href')
    url = url + '/company/?p=1'
            #print(url)
            #每个城市的公司
    try:
        while url:
             print(url)
             soup = get_soup(url)  # 已经获取到每个城市某一页的soup
             city_name = soup.find('div',{'class':'city'}).find('strong').text #获取城市名称
             #print(city_name)
             companies = soup.find('ul', {'class': 'gongslist'}).find_all('li')

             for company in companies:
                 u = company.find('a', {'class': 'company-link'}).get('href')
                 compage = get_soup(u)

                 name = compage.find('h1',{'class':'com-tit'}).text#获取公司名称

                 infos = compage.find('ul',{'class':'c-tab-send'})#获取公司信息：地址，电话1，电话2
                 att = infos.find('li', {'class': 'att'}).text
                 tel = infos.find('li',{'class':'tel'}).text
                 mob = infos.find('li',{'class':'mob'}).text
                 list = [name,att,mob,tel,]
                 print(list)



                 file_name = '/Users/zhongyi/Desktop/d/'+ city_name + '.csv'
                 f = open(file_name, 'a+', encoding='utf-8')
                 for info in list:
                     f.write(info)
                     f.write(',')
                 f.write('\n')
                 f.close()

             url = get_nexturl(soup)  # 获取下一页的url

    except AttributeError  :
        pass



