

#导入用到的模块
import requests
from bs4 import BeautifulSoup

#请求链接
url='http://job.bjtu.edu.cn/cms/employment/list/1?page=1'

page = requests.get(url).content.decode() #用request发送请求并编解码得到page
soup = BeautifulSoup(page,'html.parser') #将编解码好的页面page转换成可搜索遍历操作的soup源代码
# print (soup.prettify())
# print(soup.td.contents)

#对soup进行对一系列操作 得到想要的数据
links = soup.find('tbody').find_all('a')
for link in links:
    url=link.get('href')
    url='http://job.bjtu.edu.cn/'+url
    page=requests.get(url).content.decode()
    soup = BeautifulSoup(page,'html.parser')
    # company_name=soup.find('div',{'class':'info p_red'}).find('span',{'style':'font-weight: bolder;color: #ff5516'}).text
    information=soup.find('div',{'class':'info p_red'}).text
    # print(company_name)

    #打印数据
    print(information)

