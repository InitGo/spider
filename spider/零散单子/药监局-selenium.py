#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import  webdriver
from  selenium.webdriver.common.keys import Keys
import time

url = 'http://wenshu.court.gov.cn/list/list/?sorttype=1&number=KW78DFYP&guid=5316d928-44ae-a17e7cd7-b270d4dd7b60&conditions=searchWord+%E7%94%B5%E5%AD%90%E7%97%85%E5%8E%86+QWJS++%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2:%E7%94%B5%E5%AD%90%E7%97%85%E5%8E%86&conditions=searchWord+%E5%8C%BB%E7%96%97+AJMC++%E6%A1%88%E4%BB%B6%E5%90%8D%E7%A7%B0:%E5%8C%BB%E7%96%97#'
url1 = 'http://wenshu.court.gov.cn/content/content?DocID=5589c8bb-a6b9-4d2a-b76c-5b217f1bdaaf&KeyWord=%E7%94%B5%E5%AD%90%E7%97%85%E5%8E%86'

# driver = webdriver.Chrome()
# driver.get(url)
#
# time.sleep(5)
#
#
# button = driver.find_element_by_xpath('//*[@id="dataItem1"]/table/tbody/tr[1]/td/div/a')
# button.click()
# time.sleep(5)
#
# print(driver.page_source)
#
# download = driver.find_element_by_css_selector('#img_download')
# download.click()
# time.sleep(5)


driver = webdriver.Chrome()
driver.get(url)

time.sleep(5)

print(driver.page_source)

download = driver.find_element_by_xpath('//*[@id="dataItem1"]/div[2]/div[2]/img')
download.click()
time.sleep(5)