import requests
from bs4 import BeautifulSoup


url = 'https://www.douban.com/doulist/45298673/'
page =requests.get(url).content.decode()
soup = BeautifulSoup(page,'html.parser')
book_list = soup.find('div',{'class':'article'}).find('div',{'class':'title'})
#print(book_list)
for book in book_list:
    title1 = book.find('a').text
    print(title1)