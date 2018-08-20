#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import time
import random
from bs4 import BeautifulSoup


a = random.uniform(5,10)
t = "%.0f" % a
t = int(t)

print(t)

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}#请求头

def get_soup (url):
    #time.sleep(1)
    page = requests.get(url,headers=headers).content.decode()
    soup = BeautifulSoup(page,'html.parser')
    #time.sleep(t)
    return soup

lis = range(7,36)

for i in lis:

    url ='https://www.anjuke.com/shanghai/cm/p%d'%i + '/'
    print(url)

    soup = get_soup(url)
    flags = soup.find('div',{'id':'content'}).find('ul',{'class':'P3'}).find_all('li')

    for flag in flags:
        flag = flag.find_all('em')

        for house in flag:
            house_url = house.find('a').get('href')
            print(house_url)

            try :
                soup = get_soup(house_url)

                infos = soup.find('div',{'class':'infos-box'})
                name = infos.find('h3',{'class':'hd'}).text
                price1 = infos.find('p',{'class':'av-price'}).text
                #price2 = infos.find('span',{'class':'price'}).text
                info = infos.find('ul',{'class':'basic-parms'}).find_all('li')
                bankuai = info[0].text
                hushu = info[1].text
                lvhualv = info[2].text
                tingche = info[3].text
                wuye = info[4].text
                jungong = info[5].text
                add = soup.find('p',{'class':'address'}).text
                list = [name,price1,bankuai,hushu,lvhualv,tingche,wuye,jungong,add]
                print(list)

                f = open('/Users/zhongyi/Desktop/小区/小区3.csv', 'a+', encoding='utf-8')
                for info in list:
                    f.write(info)
                    f.write(',')
                f.write('\n')
                f.close()
            except AttributeError:
                pass







