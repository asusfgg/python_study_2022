'''
Author: fgg
Date: 2022-05-26 16:16:45
LastEditors: fgg
LastEditTime: 2022-05-26 16:45:45
FilePath: \python_study_2022\kyhg\kyhg\spiders\trans.py
Description: 学习用文件，主要就是笔记和随笔
Copyright (c) 2022 by fgg/Mechanical Design Studio, All Rights Reserved. 
'''
import json
import tablib
import csv

# 获取json数据
with open('kyhg\kyhg\spiders\shuzhi-sku.json', 'r', encoding='utf-8', errors='ignore') as f:
    rows = json.load(f)
# 将json中的key作为header, 也可以自定义header（列名）

# print(type(rows))组数据，以列表形式存储,
# 列表中的每一个元素构成是大小为2的列表
# 一号位为字符串 title 'SH603919_2017-08-03_1203757451'
# 而号位为字典，包含了具体存储元素 {}
# 如果我需要生成excel，重点在于第二个元素

print(rows[0][1])

header = tuple([i for i in rows[0][1].keys()])
# for i in rows[0][1]:
#   print(type(i))


# 创建文件对象
f = open('data.csv', 'w', encoding='utf-8')
csv_write = csv.writer(f)
csv_write.writerow(rows[0][1].keys())
for i in range(len(rows)):
    csv_write.writerow(rows[i][1].values())
f.close()
