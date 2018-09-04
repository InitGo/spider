# -*- coding: utf-8 -*-
import scrapy
from dyzj.items import DyzjItem
from scrapy.http import Request

class DzSpiderSpider(scrapy.Spider):
    name = 'dz_spider'
    allowed_domains = ['https://tieba.baidu.com']
    start_urls = ['http://https://tieba.baidu.com/']

    def parse(self, response):
        item = DyzjItem()

        item['name'] = response.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/href').extract()
        print(item['name'])
        item['price'] = response.xpath('//div[@class="product_price"]/p[@class="price_color"]/text()').extract()
        print(item['price'])
        # 提取完数据后返回item
        yield item


        for i in range(0,50):
            i = i *50
            url = 'https://tieba.baidu.com/f?kw=%E6%AE%B5%E5%8F%8B%E4%B9%8B%E5%AE%B6&ie=utf-8&pn='+str(i)
            yield Request(url,callback=self.parse)
