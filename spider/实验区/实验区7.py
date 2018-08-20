#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_soup (url):
    page = requests.get(url).content.decode()
    soup = BeautifulSoup(page,'html.parser')
    return soup

login_url = 'http://www.114best.com/login.aspx?op=model'

driver = webdriver.Chrome()
driver.get(login_url)

soup = BeautifulSoup(driver.page_source,'html.parser')

user = driver.find_element_by_xpath('//*[@id="login-username"]')
print('请输入用户名：')
#id = input()
user.send_keys('18519037573')

pwd = driver.find_element_by_xpath('//*[@id="login-password"]')
print('请输入密码：')
#password = input()
pwd.send_keys('grandline7')

code = driver.find_element_by_xpath('//*[@id="login-verifycode"]')
print('请输入验证码：')
vc = input()
code.send_keys(vc)

sub = driver.find_element_by_xpath('//*[@id="login-submit"]')
sub.click()

time.sleep(3)

# print(driver.page_source)
url = 'http://www.114best.com/114.aspx?w=%E5%8D%97%E4%BA%AC&pg=3'

print(url)
driver.get(url)
i=10
while(i>0):
    soup = BeautifulSoup(driver.page_source,'html.parser')

    companies = soup.find('div',{'class':'search-list-bg'}).find_all('div',{'class':'search-ent-row clearfix'})[1:-1]
    for company in companies:
        try:
            url = company.find('div',{'class','search-ent-left-content'}).find('a').get('href')
            cpn_url = 'http://www.114best.com/' + url
            print(cpn_url)

            driver.get(cpn_url)
            button = driver.find
            if button:
                button.click()
                time.sleep(1)

                soup = BeautifulSoup(driver.page_source,'html.parser')

                name = soup.find('ul',{'class':'item'}).find('li').text
                infos = soup.find('div',{'class':'contact'}).find('tbody').find_all('tr')
                for info in infos:
                    info = info.text
                    print(info)
            else :
                pass




        except ArithmeticError :
            pass
    nextpg = driver.find_element_by_xpath('//*[@id="content"]/div[3]/a[10]')
    nextpg.click()
    time.sleep(1)
    i = i -1









