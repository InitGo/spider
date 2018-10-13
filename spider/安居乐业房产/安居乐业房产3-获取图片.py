#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

img_url = 'http://f.51-maifang.com/archive.php?aid=423841&addno=3'

def get_soup (url):
    page = requests.get(url,headers = headers).content.decode('gbk',errors='ignore')
    soup = BeautifulSoup(page,'html.parser')
    return soup

def getandwrite_img(name,img_url):
    browser = webdriver.Chrome()
    browser.get(img_url)
    pics = browser.find_elements_by_xpath('//*[@id="lp-plist"]/li/a')

    i = 1
    for pic in pics:
        pic_type = name + '-'+ str(i) + '-' + pic.text
        pic_link = pic.get_attribute('href')
        i = i + 1
        print(pic_link)
        print(pic_type)

        targetDir = '/Users/zhongyi/Desktop/实验区'
        pic = requests.get(pic_link).content
        t = targetDir + '/' + pic_type + '.jpg'  # 生成保存的目录
        fw = open(t, 'wb')  # 指定绝对路径
        fw.write(pic)  # 保存图片到本地指定目录
        fw.close()
        print(t + '下载完成')

    browser.close()

browser = webdriver.Chrome()
browser.get('http://f.51-maifang.com/index.php?caid=2&addno=1')
citys = browser.find_elements_by_xpath('/html/body/div[11]/ul[1]/li/p/a')[:-8]
for city in citys:
    city_url = city.get_attribute('href')
    city_name = city.text
    print(city_url,city_name)


