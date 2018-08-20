import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'

page = requests.get(url).content.decode()
soup =BeautifulSoup(page,'html.parser')

links = soup.find('ol',{'class':'grid_view'}).find_all('div',{'class':'hd'})
#print(links)

for link in links:

    url = link.find('a').get('href')
    page = requests.get(url).content.decode()
    soup = BeautifulSoup(page,'html.parser')
    title = soup.find('span',{'property':'v:itemreviewed'}).text
   # language = soup.find('span',{'class':'actor'}).find_all('span',{'class':'attrs'})
    print(title)

    #缺网页循环