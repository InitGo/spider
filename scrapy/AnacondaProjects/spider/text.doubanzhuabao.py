import requests
import re
import time
import json

ii = 9175056
i = ii
while i <= 9900000:
    i = ii +10000
    url = ('https://movie.douban.com/j/review/%d/full')%(i)
    #time.sleep(2)
    html = requests.get(url)

    try :
        #for j in range(len(html.json()['data'])):

        body = html.json()['body']

       # with open (r'/Users/zhongyi/Desktop/weibo_luhan.txt','a') as ff:
        anzi = ''.join(re.findall('[\u4e00-\u9fa5]',body))
        print(anzi)
            #ff.write(hanzi + '\n'*2)

    except :
        None
