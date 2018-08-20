import requests
import os
from bs4 import BeautifulSoup

targetDir = '/Users/zhongyi/Desktop/lol-img'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}#请求头

url = 'http://lol.owan.com/hero/'
count =1
page = requests.get(url,headers=headers).content.decode()
soup = BeautifulSoup(page,'html.parser')
urls = soup.find('ul',{'id':'champion_list'}).find_all('a')
for url in urls:
    url = url.get('href')
    #print(url)o
    page = requests.get(url).content.decode()
    soup = BeautifulSoup(page,'html.parser')
    title = soup.find('h2',{'class':'hero-title'}).text
    name = soup.find('h1',{'class':'hero-name'}).text
    print(title,name)
    imglinks = soup.find('ul',{'class':'ui-slide__content'}).find_all('img') #此处imglinks为单个英雄有的几种皮肤的链接
    for imglink in imglinks:
        imglink=imglink.get('src')#此处为单个英雄的多种皮肤链接url列写
        img = requests.get(imglink)
        print(img)
        t = os.path.join(targetDir,  title + '-' + name + ' ' + str(count) + '.jpg')  # 指定目录
        print(t)
        count += 1
        fw = open(t, 'wb')  # 指定绝对路径
        fw.write(img.content)  # 保存图片到本地指定目录
        print('正在下载第%d张图:%s' % (count,title))
        fw.close()


