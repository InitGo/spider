# coding=utf-8

import re
import requests
from bs4 import BeautifulSoup
import time
from multiprocessing import Pool


headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

#url = 'http://www.doupoxs.com/doupocangqiong/2.html'


def get_info(url):

    html = requests.get(url,headers = headers)
    if html.status_code == 200 :
        page = html.content.decode('utf-8')
        page = BeautifulSoup(page,'html.parser')
        content = page.find('div',{'class':'read_chapterDetail'}).text
        #print(content)
        f.write(content)

    else:
        pass
if __name__  == '__main__':

        for i in range(1,5):

            url = ('http://www.doupoxs.com/doupocangqiong/%d.html')%(i)
            f = open('/Users/zhongyi/Desktop/doupo.txt', 'a+',encoding='utf-8')
            get_info(url)
            time.sleep(1)
f.close()



