import requests
import re
import time
import json

i = 0
while i <= 100:
    i = i + 1
    url = ('https://movie.douban.com/j/review/%d/full')%(i)
    #time.sleep(2)
    html = requests.get(url)

    try :
        for j in range(len(html.json()['data'])):

            data = html.json()['data'][j]['text']

            with open (r'/Users/zhongyi/Desktop/weibo_luhan.txt','a') as ff:
                hanzi = ''.join(re.findall('[\u4e00-\u9fa5]',data))
                print(hanzi)
                ff.write(hanzi + '\n'*2)

    except :
        None
