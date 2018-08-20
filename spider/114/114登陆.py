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