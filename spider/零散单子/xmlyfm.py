import requests
from bs4 import BeautifulSoup
import re

url = 'https://m.ximalaya.com/95514597/album/11332641'
html =requests.get(url)
page=html.content.decode()
soup = BeautifulSoup(page,'html.parser')

infos = soup.find('ol',{'class':'mod list-t1 j-list'}).find_all('li',{'class':'item-block trackItem'})
ids = re.findall('data-id="([\d]*?)"',html.text)

for info in infos :
    name =info.find('h4').text
    print(name)
for id in ids:
    id = id
    print(id)