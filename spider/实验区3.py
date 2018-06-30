import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver

url = 'http://www.stats.gov.cn//tjsj/zxfb/index.html'
browser = webdriver.Chrome()
browser.get(url)
browser.implicitly_wait(10)
page = browser.page_source
soup = BeautifulSoup(page,'html.parser')

infos = soup.find('ul',{'class':'center_list_contlist'}).find_all('a')
#print(infos)

for info in infos:
    # topics = info.find_all('font')
    # topic = topics[0].text#主题
    # time = topics[1].text#日期
    url = info.get('href')
    print(url)
    if re.match(r'/tjsj',url):
        url = 'http://www.stats.gov.cn/' + url
    elif re.match(r'\./',url):
        url = url[1:]
        url = 'http://www.stats.gov.cn/tjsj/sjjd' + url

    print(url)

    # page = requests.get(url, headers=headers).content.decode()
    # soup = BeautifulSoup(page, 'html.parser')
    # infos = soup.find('div',{'class':'center_xilan'})
    # title = infos.find('h2',{'class':'xilan_tit'}).text
    # conts = infos.find('div',{'class':'TRS_Editor'}).find_all('p')
    # for cont in conts:
    #     cont = cont.text
    #     print(cont)



