#国际合作 国际往来
import time
import requests
from bs4 import BeautifulSoup
import re



url = 'http://www.sipo.gov.cn/gjhz/gjwl/index1.htm'
page = requests.get(url).content.decode()
soup = BeautifulSoup(page,'html.parser')
print(soup.prettify())
infos = soup.find('div',{'class':'index_articl_list'}).find_all('li')
print(infos)
for info in infos:

     url = info.find('a').get('href')

     url = 'http://www.sipo.gov.cn/gjhz/gjwl/' + url
     #print(url)
     page = requests.get(url).content.decode()
     soup = BeautifulSoup(page, 'html.parser')
     i = soup.prettify()
     #print(i)

     # title = soup.find('div',{'class':'index_title'}).text
     # if title :
     #     print(title)
     # else:
     #     pass
     conts = soup.find('tbody').find('td').find_all('p')
     print(conts)


     for cont in conts :
         if cont.text:
             print(cont.text)
         else:
             pass








