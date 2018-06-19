import requests

from bs4 import BeautifulSoup
import re
with open('/Users/zhongyi/Desktop/data_list_from_pycharm.txt','w',encoding='utf-8') as f:
    for i in range(5):
        url=('http://job.bjtu.edu.cn/cms/employment/list/1?page=%d')%(i)

        page = requests.get(url).content.decode()
        soup = BeautifulSoup(page,'html.parser')
        # print (soup.prettify())
        # print(soup.td.contents)
        links = soup.find('tbody').find_all('a')
        for link in links:
            url=link.get('href')
            url='http://job.bjtu.edu.cn/'+url
            page=requests.get(url).content.decode()
            soup = BeautifulSoup(page,'html.parser')
            # company_name=soup.find('div',{'class':'info p_red'}).find('span',{'style':'font-weight: bolder;color: #ff5516'}).text
            information=soup.find('div',{'class':'info p_red'}).text
            # print(company_name)
            print(information)
            f.write("{}\n".format(information))
            input()
# for link in links:
#     url = link.get('href')
#     url='http://job.bjtu.edu.cn'+url
#     print(url)