#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:zhongyi

import requests
import time
from bs4 import BeautifulSoup
url = 'https://weibo.com/u/3591355593?refer_flag=1001030101_&is_all=1'

def get_soup(url):
    page = requests.get(url).content.decode('utf-8',errors='ignore')
    soup = BeautifulSoup(page,'html.parser')
    return soup

#def get_time():


soup = get_soup(url)
#print(soup.prettify())
up = soup.find('div',{'class': 'WB_detail'})
print(up)