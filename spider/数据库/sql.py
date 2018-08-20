#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql
import requests
from bs4 import BeautifulSoup

url = 'http://www.ytz8.com/trade-record.html'

def get_soup(url):
    page = requests.get(url).content.decode('utf-8',errors='ignore')
    soup = BeautifulSoup(page,'html.parser')
    return soup

soup = get_soup(url)
infos = soup.find('table',{'class':'table table-striped table-bordered table-hover'}).find('tbody').find_all('tr')

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='grandline7',
    db='testdb',
    charset='utf8'
    )

for info in infos:
    info = info.find_all('td')
    a = info[0].text
    b = info[1].text
    c = info[2].text
    d = info[3].text
    e = info[4].text
    f = info[5].text

    cursor = conn.cursor()
    print(conn,cursor)

    print(a)


    sql = 'INSERT INTO touzi VALUES  '
    cursor.execute(sql)

cursor.close()
conn.close()











