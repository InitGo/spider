import requests
from bs4 import BeautifulSoup
import re

f = open('执法维权时评访谈.txt', 'a+', encoding='utf-8')
session = requests.Session()
session.headers.update(
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/67.0.3396.99 Safari/537.36'
    }
)


url1 = 'http://www.sipo.gov.cn/zfwq/wqyz12330rx/index.htm' #主页面 每条新闻开头
page = requests.get(url1).content.decode()
soup = BeautifulSoup(page, 'html.parser')
infos = soup.find('div',{'class':'index_articl_list'}).find_all('li')
print(infos)

for info in infos:
    url = info.find('a').get('href')
    if re.match(r'\d',url):
        url = 'http://www.sipo.gov.cn/zfwq/wqyz12330rx/' + url
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







