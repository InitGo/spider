# -*- coding: utf-8 -*-
import scrapy


class Proxyspider2Spider(scrapy.Spider):
    name = 'proxySpider2'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://xicidaili.com/']

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

        for i in range(1, 2000):
            url = 'https://www.kuaidaili.com/free/inha/' + str(i)

            yield Request(url, callback=self.parse)

