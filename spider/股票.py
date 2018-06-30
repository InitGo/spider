import requests
import json
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}#请求头
with open("/Users/zhongyi/Desktop/1.json", "w",encoding='utf-8') as f:
    for num in range(1,10):  #可更改爬取数量
        url = 'http://data.bank.hexun.com/lccp/AllLccp.aspx?col=fld_issenddate&tag=desc&orderMarks=&page=%s'%str(num)
        page = requests.get(url,headers=headers).content.decode('gb2312')
        soup = BeautifulSoup(page,'html.parser')
        infos = soup.find_all('tr',{'align':'center'})
        for info in infos:
            name = info.find('td',{'class':'dr'}).find('a').get('alt')
            bank = info.find('td',{'class':'hl'}).text
            i = info.find_all('td')
            tsr = i[3].text #停售日
            dqr = i[4].text #到期日
            bz = i[5].text #币种
            glq = i[6].text #管理期（月）
            cplx = i[7].text #产品类型
            yqsy = i[8].text #预期收益（%）
            info = {"产品名称":name,"银行":bank,'停售日':tsr,'到期日':dqr,'币种':bz,'管理期（月）':glq,'产品类型':cplx,'预期收益':yqsy}
            jstr = json.dumps(info, ensure_ascii=False)
            f.write(jstr+'\n')
            print("加载入文件完成...")
    f.close()



