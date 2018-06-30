#执法维权 政策通知
import time
import requests
from bs4 import BeautifulSoup


def get_info(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }  # 请求头
    page = requests.get(url,headers=headers)
    if page.status_code == 200:
        page=page.content.decode()
        soup = BeautifulSoup(page,'html.parser')

        infos = soup.find('div',{'class':'index_articl_list'}).find_all('li')
        #print(infos)
        for info in infos:

            url = info.find('a').get('href')
            url = 'http://www.sipo.gov.cn/zfwq/wqyzgzyq/' + url

            page = requests.get(url, headers=headers)
            if page.status_code == 200:
                page = page.content.decode()
                soup = BeautifulSoup(page, 'html.parser')

                title = soup.find('div',{'class':'index_title'}).text
                conts = soup.find('tbody').find('td').find_all('p')
                f.write(title)
                for cont in conts:
                    cont = cont.text
                    print(cont)

                    f.write(cont)

if __name__ == '__main__':
    for i in range(1,2):
        url = 'http://www.sipo.gov.cn/zfwq/wqyzgzyq/index%d.htm'%(i)
        f = open('执法维权政策通知.txt', 'a+', encoding='utf-8')
        get_info(url)
        time.sleep(1)
f.close()  # 循环结束后关闭文件





