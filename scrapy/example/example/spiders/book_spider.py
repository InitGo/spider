# -*- coding: utf-8 -*-
import scrapy
from example.items import ExampleItem
from scrapy.http import Request


class BookSpiderSpider(scrapy.Spider):
    name = 'book_spider'
    allowed_domains = ['books.toscrape.com']

    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        item = ExampleItem()

        item['name'] = response.xpath('//article[@class="product_pod"]/h3/a/text()').extract()
        print(item['name'])
        item['price'] = response.xpath('//div[@class="product_price"]/p[@class="price_color"]/text()').extract()
        print(item['price'])
        #提取完数据后返回item
        yield item

        for i in range(1,50):
            url = 'http://books.toscrape.com/catalogue/page-'+ str(i) +'.html'
            yield Request(url,callback=self.parse)
