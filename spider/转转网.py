import requests
from xtml import etree

start_url = 'http://cs.58.com/sale.shtml'
url_host = 'http://cs.58.com'

def get_channel_urls(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    infos = selector.xpath('/html/body/div[3]/div[1]')

    for info in infos:
        class_urls = info.xpath()