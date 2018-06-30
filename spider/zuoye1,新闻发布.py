import requests
from bs4 import BeautifulSoup
import re

f = open('新闻发布.txt', 'a+', encoding='utf-8')
session = requests.Session()
session.headers.update(
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/67.0.3396.99 Safari/537.36'
    }
)


url111 = 'http://www.sipo.gov.cn/xwfb/index.htm' #主页面 每条新闻开头
url222 = 'http://www.sipo.gov.cn/xwfb/index1.htm'
url = [url111,url222]
for url1 in url:
    page = requests.get(url1).content.decode()
    soup = BeautifulSoup(page, 'html.parser')
    infos = soup.find('div',{'class':'index_articl_list'}).find_all('li')
    print(infos)

    for info in infos:
        url = info.find('a').get('href')
        if re.match(r'\d',url):
            url = 'http://www.sipo.gov.cn/xwfb/' + url
        else :
            url = None
        print(url)
        if url :
            session.get(url1)
            page = session.get(url).content.decode()
            soup = BeautifulSoup(page, 'html.parser')
           # print(soup.prettify()）
            title = soup.find('div',{'class':'index_title'}).text
            conts = soup.find('tbody').find('td').find_all('p')
            f.write(title)
            for cont in conts:
                cont = cont.text
                print(title)
                print(cont)

                f.write('\n')
f.close()







