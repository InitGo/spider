#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}




def get_soup (url):
    page = requests.get(url,headers = headers).content.decode('gb2312',errors='ignore')
    soup = BeautifulSoup(page,'html.parser')
    return soup

#传入一个单页url，返回所有页面页中flagurl的list
def all_page_urls (url,k,j):  #把每单页的房子的URL得到并且进入获取信息 传入的为每单页的url 返回单页中的flag——url
    flag_list = []
    browser = webdriver.Chrome()
    url1 = url + '&page='
    for i in range(k,j+1):
        url = url1
        url = url + str(i)
        print(url, '正在扫描这一页的flag')
        browser.get(url)
        flags = browser.find_elements_by_xpath('/html/body/div[13]/div[1]/ul/li/div/div[2]/div[1]/div[1]/a')
        for flag in flags:
            flag_url = flag.get_attribute('href')
            print(flag_url)
            flag_list.append(flag_url)

    browser.close()
    print(flag_list)
    return flag_list #返回一个列表
        #这是得到每单页中每条房子的url的函数

#传入一个flag——url 返回一个次flag的所有信息的list，其中首字为名字
def get_info (flag_url):
    list = []
    #   现已得到单页中每条房产的url
    soup = get_soup(flag_url)
    #获取信息
    info1 = soup.find('div',{'class':'pull-left h'}).find_all('p')
    name = info1[0].text
    type = info1[1].text
    list.append(name)
    list.append(type)

    info2 = soup.find('dl',{'id':'lp-info'}).find_all('dd')
    price = info2[0].text
    list.append(price)
    add = '主力户型: ' + info2[5].text
    list.append(add)
    #获取详情页面
    in_url = flag_url + '&addno=12'
    print('这是获取详情页面：' + in_url)
    soup = get_soup(in_url)
    info3 = soup.find('div',{'class':'item'})

    info31 = info3.find_all('dl')[:-3]
    info32 = info3.find_all('dl')[-3:]

    for info311 in info31:
        try :
            info3111 = info311.find_all('dd')
            info3112 = info311.find_all('dt')
            one = info3112[0].text + info3111[0].text
            two = info3112[1].text + info3111[1].text
            list.append(one)
            list.append(two)
            ##在此将信息写入列表
        except IndexError :
            pass
    for info322 in info32:
        try :
            info3111 = info322.find('dd')
            info3112 = info322.find('dt')
            one = info3112.text + info3111.text
            list.append(one)
            ##在此将信息写入列表
        except IndexError :
            pass
    print('这是这一个flag的详情信息')
    print(list)
    return list

#传入名字和单个flagurl，自动把图片写入文件夹 拟定一个城市一个文件夹 传入城市名
def get_img (name,city_name,flag_url):
    img_url = flag_url +'&addno=3' #传入单个flag的url，改造成flag图片的url
    print(img_url)
    browser = webdriver.Chrome()
    browser.get(img_url)
    pics = browser.find_elements_by_xpath('//*[@id="lp-plist"]/li/a')

    i = 1
    for pic in pics:
        pic_type = name + '-' + str(i) + '-' + pic.text
        pic_link = pic.get_attribute('href')
        i = i + 1
        # print(pic_link)
        # print(pic_type)
        targetDir = '/Users/zhongyi/Desktop/' + city_name  #后期修改 改成城市的名字
        pic = requests.get(pic_link).content
        t = targetDir + '/' + pic_type + '.jpg'  # 生成保存的目录
        fw = open(t, 'wb')  # 指定绝对路径
        fw.write(pic)  # 保存图片到本地指定目录
        fw.close()
        print(t + '下载完成')

    browser.close()


# browser = webdriver.http://f.51-maifang.com/index.php?caid=2&ccid1=5019&addno=1Chrome()
# browser.get('http://f.51-maifang.com/index.php?caid=2&addno=1')
# citys = browser.find_elements_by_xpath('/html/body/div[11]/ul[1]/li/p/a')[:-8]
# for city in citys:
#     city_url = city.get_attribute('href')
#     city_name = city.text
#     print(city_url,city_name)

city_url = 'http://f.51-maifang.com/index.php?caid=2&ccid1=5047&addno=1'
city_name = '太原'
print(city_url,city_name)
flag_list = all_page_urls(city_url,3,16) #输入开始和终止页面 湖州全 涿州全 霸州全 廊坊全 北京共30 海口市10 三亚11 中山市23 杭州37 海南29 邯郸20 南京11 合肥7 上海3 成都13 湛江14 张家口16 太原6
for flag_url in flag_list:
    print('现在正在处理这一flag：')
    print(flag_url)
    info_list = get_info(flag_url)#已得到每条flag的信息
    #把infolist写入csv
    file_name = city_name + '.csv'
    dir = '/Users/zhongyi/Desktop/'+ city_name + '/'
    print('这是下载地址：' + dir)
    f = open( dir + file_name, 'a+', encoding='utf-8')
    for info in info_list:
        f.write(info)
        f.write(",")
    f.write("\n")
    f.close()
    name = info_list[0]
    get_img(name,city_name,flag_url)
    print('\n\n')



