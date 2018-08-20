import requests
from bs4 import  BeautifulSoup


for i in range(100):
    url='https://movie.douban.com/review/best/?start=%d'
    page = requests.get(url).content.decode()
    soup = BeautifulSoup(page,'html.parser')
    movie_comments=soup.find('div',{'class':'review-list chart'}).find_all('div')
    for z in movie_comments:
        th=z.find_all('div',{'class':'short-content'}).text
        print(th)


