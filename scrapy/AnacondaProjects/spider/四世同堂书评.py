import re
import requests
from bs4 import BeautifulSoup

url = ('https://book.douban.com/subject/3183775/reviews?start=0')#%(i)
html = requests.get(url).content.decode()
page = BeautifulSoup(html,'html.parser')
#print(page)
comments = page.find('div',{'class','article'}).find('div',{'class':'review-list'})
for comment in comments:
    comment = comments.find('div',{'class','short-content'}).text

    print(comment)