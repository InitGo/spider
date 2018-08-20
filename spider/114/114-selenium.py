from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


browser = webdriver.Chrome()
browser.get('http://www.114best.com/')
username = '18519037573'
password = 'grandline7'

def get_infomation(url_all):
    browser.get(url_all)
    time.sleep(1)
    all_tr = browser.find_elements_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/table/tbody/tr')
    time.sleep(1)
    for tr in range(1, len(all_tr) + 1):
        # time.sleep(3)
        try:
            button = browser.find_element_by_xpath(
                '//*[@id="content"]/div[1]/div[4]/div[1]/table/tbody/tr[' + str(tr) + ']/td[2]/span/a')
            button.click()
            time.sleep(2)
            num = browser.find_element_by_xpath(
                '//*[@id="content"]/div[1]/div[4]/div[1]/table/tbody/tr[' + str(tr) + ']/td[2]/b').text
            name = browser.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div[2]/ul/li[1]').text

            # address = browser.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/table/tbody/tr[' + str(tr) + ']/td[2]').text
            print(name)
            print('联系方式:' + num)

            f = open('/Users/zhongyi/Desktop/114查询/南京.csv', 'a+', encoding='utf-8')
            f.write(name)
            f.write(',')
            f.write('联系方式:' + num)
            f.write('\n')
            f.close()

            break
        except:
            # time.sleep(3)
            None
    # time.sleep(3)
    browser.back()
    time.sleep(3)


def login():
    button1 = browser.find_element_by_xpath('//*[@id="span_onuser_menu"]/a[2]')
    button1.click()
    time.sleep(1)
    text = input('请输入验证码:')
    browser.switch_to_frame(browser.find_element_by_id('showframe'))
    #上一行为跳转到登陆框
    username_button = browser.find_element_by_xpath('//*[@id="login-username"]')
    username_button.clear()
    username_button.send_keys(username)
    password_button = browser.find_element_by_xpath('//*[@id="login-password"]')
    password_button.clear()
    password_button.send_keys(password)
    yzm_button = browser.find_element_by_xpath('//*[@id="login-verifycode"]')
    yzm_button.clear()
    yzm_button.send_keys(text)
    login_button = browser.find_element_by_xpath('//*[@id="login-submit"]')
    login_button.click()
    time.sleep(3)
    #上面一大段为登陆
    #下面以首页的公司为例

    browser.refresh()
    for page in range(1,5):
        page_url = 'http://www.114best.com/114.aspx?w=南京&pg=' + str(page)
        browser.get(page_url)
        html = BeautifulSoup(browser.page_source,'html.parser')
        company_urls = html.find_all('div',{'class':'search-ent-row clearfix'})[1:-1]
        for company_url in company_urls :
            url = company_url.find('div',{'class':'search-ent-left-content'}).find('a').get('href')
            url_all = 'http://www.114best.com/' + url
            print(url_all)

        # for i in range(2, 10):
        #     每次点击公司现刷新页面
        #     browser.refresh()
        #     time.sleep(3)
            #browser.get(url_all)

            response = requests.get('http://www.114best.com/gs11/434180324.html', headers=headers)    #用一个公司的url测试是否请求成功
            if response.status_code == 403:
                print('访问失败，等待3分钟')
                time.sleep(180)     #这里可以改一下试一下，可能可以减少一点时间
                browser.refresh()
                get_infomation(url_all)

            else:
                get_infomation(url_all)


login()
browser.close()