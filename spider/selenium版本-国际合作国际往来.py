#国际合作 国际往来
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def get_soup(url):
    browser = webdriver.Chrome()
    browser.get(url)
    browser.implicitly_wait()
    page = browser.page_source
    soup = BeautifulSoup(page, 'html.parser')
    print(soup)
    return soup   #返回bs4处理过的网页源代码


def get_info(soup):
    infos = soup.find('div',{'class':'index_articl_list'}).find_all('li')

    for info in infos:

        url = info.find('a').get('href')
        url = 'http://www.sipo.gov.cn/gjhz/gjwl/' + url
        soup = get_soup(url)
        title = soup.find('div',{'class':'index_title'}).text
        conts = soup.find('tbody').find('td').find_all('p')
        for cont in conts:
            cont = cont.text
            print(cont)
            f.write(title)
            f.write(cont)

if __name__ == '__main__':
    for i in range(1,5):
        url = 'http://www.sipo.gov.cn/gjhz/gjwl/index%d.htm'%(i)
        f = open('国际合作国际往来.txt', 'a+', encoding='utf-8')
        get_info(url)
        time.sleep(1)
f.close()  # 循环结束后关闭文件





