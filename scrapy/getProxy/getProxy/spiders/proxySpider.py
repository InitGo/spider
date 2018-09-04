# -*- coding: utf-8 -*-
import scrapy
from getProxy.items import GetproxyItem
from scrapy.http import Request

class ProxyspiderSpider(scrapy.Spider):
    name = 'proxySpider'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/5']

    def parse(self, response):
        item = GetproxyItem()

        item['ip'] = response.xpath('//tbody/tr/td[1]/text()').extract()
        item['port'] = response.xpath('//tbody/tr/td[2]/text()').extract()
        item['noname'] = response.xpath('//tbody/tr/td[3]/text()').extract()
        item['type'] = response.xpath('//tbody/tr/td[4]/text()').extract()
        item['location'] = response.xpath('//tbody/tr/td[5]/text()').extract()
        item['res_speed'] = response.xpath('//tbody/tr/td[6]/text()').extract()
        print(item['ip'])
        yield item

        for i in range(6,2000):
            url = 'https://www.kuaidaili.com/free/inha/' + str(i)

            yield Request(url, callback=self.parse)
