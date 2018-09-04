# -*- coding: utf-8 -*-
import scrapy
import os
import json
from scrapy.selector import Selector
from FmFiles.items import FmfilesItem
from FmFiles.settings import FILES_STORE



class FmfilesSpider(scrapy.Spider):
    name = 'fmfiles'
    allowed_domains = ['']
    # PC端起始url
    pc_url = 'http://www.ximalaya.com/'
    # 移动端起始url
    mobile_url = 'http://m.ximalaya.com/'


def parse(self, response):
    # 专辑名称
    album_name = response.xpath('//article/div/div/h2/text()').extract_first().strip()
    # self.album_name = album_name
    filepath = FILES_STORE + album_name
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    meta = response.meta
    yield self.json_formrequest(aname=album_name,
                                aid=meta['aid'])



def start_requests(self):
    for url in self.urls:
        if url.startswith(self.mobile_url):
            yield self.request_album_url(url)
        elif url.startswith(self.pc_url):
            yield scrapy.Request(url=url, callback=self.parse_pc)

def request_album_url(self, album_url=''):
    if len(album_url) == 0:
        return None
    album_url = album_url.strip().strip('/')
    album_id = album_url.split('/')[-1]
    return scrapy.Request(album_url,
                          meta={'aid': album_id},
                          callback=self.parse,
                          dont_filter=True)

def parse_pc(self, response):
    # 从PC端专辑html中解析出移动端专辑url
    mobile_url = response.xpath('//head/link[contains(@rel, "alternate")]/@href').extract_first()
    yield self.request_album_url(mobile_url)

def json_formrequest(self, aname='', aid=0, page=1):
    moreurl = '/album/more_tracks'
    # album_id = album_url.split('/')[-1]
    page = str(page)
    formrequest = scrapy.FormRequest(url='http://m.ximalaya.com' + moreurl,
                                     formdata={'url': moreurl,
                                               'aid': str(aid),
                                               'page': str(page)},
                                     meta={'aname': str(aname),
                                           'aid': str(aid),
                                           'page': str(page)},
                                     method='GET',
                                     callback=self.parse_json,
                                     dont_filter=True)
    return formrequest

def parse_json(self, response):
    jsondata = json.loads(response.text)
    if jsondata['res'] is False:
        return None
    next_page = jsondata['next_page']
    selector = Selector(text=jsondata['html'])
    file_nodes = selector.xpath('//li[@class="item-block"]')
    if file_nodes is None:
        return None
    meta = response.meta
    for file_node in file_nodes:
        file_name = file_node.xpath('a[1]/h4/text()').extract_first().strip()
        file_url = file_node.xpath('a[2]/@sound_url').extract_first().strip()
        item = FmfilesItem()
        item['file_album'] = meta['aname']
        item['file_name'] = file_name + '.' + file_url.split('.')[-1]
        item['file_url'] = file_url
        yield item
    if int(next_page) == 0:
        return None
    if int(next_page) == (int(meta['page']) + 1):
        yield self.json_formrequest(aname=meta['aname'],
                                    aid=meta['aid'],
                                    page=next_page)

