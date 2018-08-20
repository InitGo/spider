from selenium import webdriver
import time
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}


browser = webdriver.Chrome()
browser.get('http://www.114best.com/')
username = '18519037573'
password = 'grandline7'


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
    #browser.get('http://www.114best.com/114.aspx?w=%E5%8D%97%E4%BA%AC&pg=1')
    time.sleep(1)

    for i in range(1, 22):
        #每次点击公司现刷新页面
        #browser.refresh()
        time.sleep(3)
        response = requests.get('http://www.114best.com/gs11/434180324.html', headers=headers)    #用一个公司的url测试是否请求成功
        if response.status_code == 403:
            print('访问失败，等待3分钟')
            time.sleep(180)     #这里可以改一下试一下，可能可以减少一点时间
            browser.refresh()
            company = browser.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div[1]/ul/li[' + str(i) + ']')
            company.click()
            all_tr = browser.find_elements_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/table/tbody/tr')
            time.sleep(3)
            for tr in range(1, len(all_tr) + 1):
                time.sleep(3)
                try:
                    button = browser.find_element_by_xpath(
                        '//*[@id="content"]/div[1]/div[4]/div[1]/table/tbody/tr[' + str(tr) + ']/td[2]/span/a')
                    button.click()
                    time.sleep(1)
                    num = browser.find_element_by_xpath(
                        '//*[@id="content"]/div[1]/div[4]/div[1]/table/tbody/tr[' + str(tr) + ']/td[2]/b').text
                    print(num)
                    time.sleep(1)
                    break
                except:
                    #time.sleep(3)
                    None
            #time.sleep(3)
            browser.back()
            time.sleep(3)
        else:
            company = browser.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div[1]/ul/li[' + str(i) + ']')
            company.click()
            all_tr = browser.find_elements_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/table/tbody/tr')
            time.sleep(3)
            for tr in range(1, len(all_tr) + 1):
                time.sleep(3)
                try:
                    button = browser.find_element_by_xpath(
                        '//*[@id="content"]/div[1]/div[4]/div[1]/table/tbody/tr[' + str(tr) + ']/td[2]/span/a')
                    button.click()
                    time.sleep(1)
                    num = browser.find_element_by_xpath(
                        '//*[@id="content"]/div[1]/div[4]/div[1]/table/tbody/tr[' + str(tr) + ']/td[2]/b').text
                    print(num)
                    time.sleep(1)
                    break
                except:
                    #time.sleep(3)
                    None
            #time.sleep(3)
            browser.back()
            time.sleep(3)
            #抓取完之后在回到前一页


login()
browser.close()