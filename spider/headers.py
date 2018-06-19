import requests
from bs4  import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

url ='http://www.njtu.edu.cn/'
html = requests.get(url,headers = headers)
print(html.text)