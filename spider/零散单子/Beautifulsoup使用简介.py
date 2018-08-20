import requests
from bs4  import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

url ='http://www.njtu.edu.cn/'
html = requests.get(url,headers = headers)
page = html.content.decode('gb2312')
#print(html.text)

soup = BeautifulSoup(page,'html.parser')   #此处对网页内容进行解析（需要加上 .content.decode()） 而不是直接requests到网页立即解析
#print(soup)
# soup.prettify() 使得soup按照标准缩进格式的结构输出 可实验 与soup直接输出的对比
print(soup.prettify())

soup.find_all()

soup.find()

soup.selector(div.item > a >h1)#类似于 中国 > 湖南 > 长沙从小到大提取信息