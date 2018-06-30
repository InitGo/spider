import requests
from bs4 import BeautifulSoup

f = open('协会动态专题活动.txt', 'a+', encoding='utf-8')
url = 'http://www.china-cba.net/list.php?fid=120'#主页面
page = requests.get(url).content.decode('gb2312',errors='ignore')
soup = BeautifulSoup(page, 'html.parser')
#print(soup.prettify())
urls = soup.find_all('span',{'style':'float:left;color:#666;'})
for url in urls:
    url = url.find('a').get('href')
    url = 'http://www.china-cba.net/' + url
    print(url)
    page = requests.get(url).content.decode('gb2312', errors='ignore')
    soup = BeautifulSoup(page, 'html.parser')
    #print(soup.prettify())
    infos = soup.find('div', {'id': 'my_bencandy_in'})
    title = infos.find('div', {'id': 'my_bencandy_in_tit'}).text
    if infos.find('div', {'id': 'my_bencandy_in_main'}).find('font'):
        conts = infos.find('div', {'id': 'my_bencandy_in_main'}).find('font').text
    f.write(title)
    f.write('\n')
    print(title)

    f.write(conts)
    f.write('\n')

    print(conts)
f.close()