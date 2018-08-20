import requests

import re




url='https://movie.douban.com/j/review/9308096/full'
page = requests.get(url)
data= page.json()
with open (r'/Users/zhongyi/Desktop/pinlun.txt','a') as f:
    hanzi =''.join(re.findall('[\u4e00-\u9fa5]',data))

    f.write("{}\n".format(hanzi))


