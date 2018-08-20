#!/usr/bin/env python
# -*- coding:utf-8 -*-


list = ['荣诺搜居网线下装饰体验馆 ', '立山区齐家装饰设计工作室', '18842074270', '421541122']

f = open('a.csv', 'a+',encoding='utf-8')
for info in list:

    f.write(info)
    f.write(',')

f.write('\n')
f.close()