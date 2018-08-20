#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:zhongyi
import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='grandline7',
    db='testdb',
    charset='utf8'
)

cursor = conn.cursor()

sql = 'INSERT INTO touzi (交易时间,买卖,类别,商品,手数,单价) VALUES ('2003','市价开空','市价开仓','甲醇1809','1','2891.00')'

cursor.execute(sql)

rs = cursor.fetchall()
print(rs)


cursor.close()
conn.close()