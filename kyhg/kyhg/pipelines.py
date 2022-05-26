'''
Author: fgg
Date: 2022-05-26 14:22:40
LastEditors: fgg
LastEditTime: 2022-05-26 15:56:09
FilePath: \python_study_2022\kyhg\kyhg\pipelines.py
Description: 学习用文件，主要就是笔记和随笔
Copyright (c) 2022 by fgg/Mechanical Design Studio, All Rights Reserved. 
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class KyhgPipeline:

    # 爬虫开始前执行的方法
    def open_spider(self, spider,):
        print('+++++++++++++++爬虫开始前执行+++++++++++++++++')
        # 在爬虫开始前就开打一个对象，用来写入数据
        self.fp = open('shuzhi-sku.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # with open('book.json', 'a', encoding='utf-8')as fp:
        #     # write()写入的是字符串
        #     # 强转str（），但是json中只有最后一条信息
        #     # 因为‘w’模式 对每个对象都打开一次文件，覆盖之前的内容，后关闭
        #     fp.write(str(item))
        #     改进：改为‘a’模式，表示追加
        self.fp.write(str(item))
        return item

    # 爬虫结束执行后执行的方法

    def close_spider(self, spider):
        print('----------------爬虫结束执行-----------------')
        self.fp.close()
