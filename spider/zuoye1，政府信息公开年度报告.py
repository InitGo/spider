import requests
from bs4 import BeautifulSoup

f = open('政府信息公开年度报告.txt', 'a+', encoding='utf-8')
url = 'http://211.157.104.86:8080/ogic/view/webpage.jhtml?channelId=6&order=sorted'#主页面
page = requests.get(url).content.decode()
soup = BeautifulSoup(page, 'html.parser')
urls = soup.find('ul',{'class':'list-act01'}).find_all('li')

for url in urls:
    url = url.find('a').get('href')
    url = 'http://211.157.104.86:8080/' + url
    #print(url)

    page = requests.get(url).content.decode()
    soup = BeautifulSoup(page, 'html.parser')

    infos = soup.find('div',{'class':'index_art_pane'})
    #print(infos)
    conts = infos.find('tbody').find_all('p')#
    if conts :
        pass
    else:
        conts = conts = infos.find('tbody').find_all('div')
    title = infos.find('div',{'class':'index_title'}).text
    print(title)
    f.write(title)
    f.write('\n')
    for cont in conts:
        if cont.text :
            cont = cont.text
            f.write(cont)
            print(cont)
    f.write('\n')
f.close()

