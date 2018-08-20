#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json

f = open('百度地图API.json', 'a+',encoding='utf-8')

left_bottom = [116.282387,39.835862];  # 设置区域左下角坐标（百度坐标系）
right_top = [116.497405,39.996569]; # 设置区域右上角坐标（百度坐标系）
part_n = 2;  # 设置区域网格（2*2）

url0 = 'http://api.map.baidu.com/place/v2/search?';
x_item = (right_top[0]-left_bottom[0])/part_n;
y_item = (right_top[1]-left_bottom[1])/part_n;
query = '饭店'; #搜索关键词设置
ak = 'P2ZSs6rflck428VuGQa5WmqZmGEokYaz'; #百度地图api信令
n = 0; # 切片计数器
for i in range(part_n):
    for j in range(part_n):
        left_bottom_part = [left_bottom[0]+i*x_item,left_bottom[1]+j*y_item]; # 切片的左下角坐标
        right_top_part = [right_top[0]+i*x_item,right_top[1]+j*y_item]; # 切片的右上角坐标
        for k in range(20):
            url = url0 + 'query=' + query + '&page_size=20&page_num=' + str(k) + '&scope=1&bounds=' + str(left_bottom_part[1]) + ',' + str(left_bottom_part[0]) + ','+str(right_top_part[1]) + ',' + str(right_top_part[0]) + '&output=json&ak=' + ak;
            data = requests.get(url).content.decode();
            hjson = json.loads(data);
            if hjson['message'] == 'ok':
                results = hjson['results'];
                for m in range(len(results)): # 提取返回的结果
                    print(results[m])

                    f.write(results[m])

        n += 1;
        print ('第',str(n),'个切片入库成功')
f.close()