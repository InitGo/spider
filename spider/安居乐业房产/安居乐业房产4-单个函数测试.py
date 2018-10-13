#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

list = []
flag_list = []
def get_soup (url):
    page = requests.get(url,headers = headers).content.decode('gbk',errors='ignore')
    soup = BeautifulSoup(page,'html.parser')
    return soup

#传入一个单页url，返回所有页面页中flagurl的list
def every_page_urls (url,k,j):  #把每单页的房子的URL得到并且进入获取信息 传入的为每单页的url 返回单页中的flag——url
    browser = webdriver.Chrome()
    url1 = url + '&page='
    for i in range(k,j+1):
        url = url1
        url = url + str(i)
        print(url, '正在扫描这一页的flag')
        browser.get(url)
        flags = browser.find_elements_by_xpath('/html/body/div[13]/div[1]/ul/li/div/div[2]/div[1]/div[1]/a')
        for flag in flags:
            flag_url = flag.get_attribute('href')#find('div', {'class': 'houselist_subject'}).find('a').get('href')
            print(flag_url)
            flag_list.append(flag_url)

    browser.close()
    print(flag_list)
    return flag_list #返回一个列表
        #这是得到每单页中每条房子的url的函数

every_page_urls('http://f.51-maifang.com/index.php?caid=2&addno=1&ccid1=5033&page=')