# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
from pymongo import MongoClient
from scrapy import Item

class GetproxyPipeline(object):
    def __init__(self):
        self.file = codecs.open('/Users/zhongyi/Desktop/ipdata2.json', 'wb', encoding='utf-8')
        # 打开json文件

    def process_item(self, item, spider):
        for j in range(0, len(item['ip'])):
            ip = item['ip'][j]
            port = item['port'][j]
            noname = item['noname'][j]
            type = item['type'][j]
            location = item['location'][j]
            res_speed = item['res_speed'][j]

            data = {'ip':ip,'端口':port,'匿名度':noname,'类型':type,'响应速度':res_speed,'位置':location,}
            i = json.dumps(dict(data), ensure_ascii=True)
            line = i + '\n'  # 每条数据后加上换行
            self.file.write(line)  # 数据写入
        return item

    def close_spider(self, spider):
        self.file.close()
        # 关闭json文件

