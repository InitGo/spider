import requests
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}#请求头

url = 'https://www.qiushibaike.com/hot/text/'
res = requests.get(url,headers = headers)
selector = etree.HTML(res.text)
id = selector.xpath('//*[@id="qiushi_tag_120325407"]/div[1]/a[2]/h2/text()')
print(id)
