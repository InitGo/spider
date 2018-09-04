import requests
from bs4 import BeautifulSoup

with open('','w',encoding='utf-8') as f:
    for i in range(10):

        url = 'https://www.douban.com/doulist/45298673/?start=%d' % (i * 25)
        page =requests.get(url).content.decode()
        soup = BeautifulSoup(page,'html.parser')
        book_list = soup.find('div',{'class':'article'}).find_all('div',{'class':'title'})
        #print(book_list)
        for book in book_list:
            title1 = book.find('a').text
            print(title1)
            f.write("{}\n".format(title1))