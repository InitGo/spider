# coding=utf-8

import re
import requests
from bs4 import BeautifulSoup
import time
from multiprocessing import Pool



#url = 'http://www.doupoxs.com/doupocangqiong/2.html'


def get_info(url):#构造函数

    html = requests.get(url,headers = headers)
    if html.status_code == 200 :#确认连接正确
        page = html.content.decode('utf-8')
        page = BeautifulSoup(page,'html.parser')#解析页面
        content = page.find('div',{'class':'read_chapterDetail'}).text#拿到内容
        #print(content)
        f.write(content)#写入文件

    else:
        pass
if __name__  == '__main__':

        for i in range(1,5):

            url = ('http://www.doupoxs.com/doupocangqiong/%d.html')%(i)
            f = open('/Users/zhongyi/Desktop/doupo.txt', 'a+',encoding='utf-8')
            get_info(url)
            time.sleep(1)
f.close()#循环结束后关闭文件



