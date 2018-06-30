import requests
from bs4 import BeautifulSoup
import time

def get_soup(url):
    page = requests.get(url).content.decode('gb2312',errors='ignore')
    soup = BeautifulSoup(page, 'html.parser')
    return soup

def get_info(soup):

    infos = soup.find('div',{'id':'list_r_list'}).find_all('span')
    #print(infos)
    for info in infos:

        url = info.find('a')
        if url:
            url = url.get('href')
            url = 'http://www.china-cba.net/' + url
            #print(url)
            soup = get_soup(url)
            #print(soup.prettify())
            infos = soup.find('div',{'id':'my_bencandy_in'})
            title = infos.find('div',{'id':'my_bencandy_in_tit'}).text
            conts = infos.find('div',{'id':'my_bencandy_in_main'}).find_all('div')
            f.write(title)
            f.write('\n')
            for cont in conts:
                cont = cont.text
                f.write(cont)
                f.write('\n')


                print(cont)

if __name__  == '__main__':

        for i in range(1,5):

            url = ('http://www.china-cba.net/list.php?fid=43&page=%d') % (i)
            f = open('协会动态领导讲话.txt', 'a+',encoding='utf-8')
            soup = get_soup(url)
            info = get_info(soup)
            time.sleep(1)
f.close()#循环结束后关闭文件


