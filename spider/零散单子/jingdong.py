import requests
from bs4 import BeautifulSoup


url = 'https://item.jd.com/6946629.html'
r = requests.get(url).content.decode('gbk')
soup = BeautifulSoup(r,'html.parser')
print(soup)
