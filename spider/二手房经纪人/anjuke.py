#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import re
#page = 50
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
def get_soup (url):
    page = requests.get(url,headers = headers).content.decode()
    soup = BeautifulSoup(page,'html.parser')
    return soup

for i in range(1,51):
    url = 'https://beijing.anjuke.com/tycoon/p' + str(i) +'/'
    print(url)

    soup = get_soup(url)
    time.sleep(3)
    infos = soup.find('div',{'class':'list-content'}).find_all('div',{'class':'jjr-itemmod'})

    for info in infos:

        agent_url = info.find('div',{'class':'jjr-title'}).find('h3').find('a').get('href')
        soup = get_soup(agent_url)



        name = info.find('div',{'class':'jjr-title'}).find('h3').find('a').text

        try :
            years = info.find('p',{'class':'jjr-desc'}).find_all('a')
            year = '门店：' + years[0].text + '/' + years[1].text
        except IndexError:
            year = '独立经纪人'

        try :
            tel_filter = soup.find('head').find('title').text
            tel = re.findall('\d+', tel_filter)[0]

        except IndexError:
            tel = '无'
        #tel = info.find('div',{'class':'col-3'}).find('h2').text
        print(name,year,tel)
        f = open('anjuke.csv', 'a+', encoding='utf-8')
        f.write(name)
        f.write(',')
        f.write('联系方式:' + tel)
        f.write(',')
        f.write(year)
        f.write('\n')
        f.close()


