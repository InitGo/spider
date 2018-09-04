# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
from pymongo import MongoClient
from scrapy import Item

class ExamplePipeline(object):
    def __init__(self):
        self.file = codecs.open('/Users/zhongyi/Desktop/mydata2.json','wb',encoding='utf-8')
        #打开json文件

    def process_item(self, item, spider):
        for j in range(0,len(item['name'])):
            name = item['name'][j]
            price = item['price'][j]
            book = {'name':name,'price':price}
            i = json.dumps(dict(book),ensure_ascii=False)
            line = i +'\n' #每条数据后加上换行
            self.file.write(line) #数据写入
        return item

    def close_spider (self,spider):

        self.file.close()
        #关闭json文件
