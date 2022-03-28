'''
Author: your name
Date: 2022-03-25 14:52:28
LastEditTime: 2022-03-28 16:57:59
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\Scrapy基础\当当网\scrapy_dangdang_3_25\scrapy_dangdang_3_25\pipelines.py
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import urllib.request
from itemadapter import ItemAdapter

# 如果使用管道，必须在settings中开启管道


class ScrapyDangdang325Pipeline:
    # item参数就是yield返回的数据book
    # 初始方法对文件操作过于频繁
    # 改进如下：
    # 方法一：

    # 爬虫开始前执行的方法
    def open_spider(self, spider,):
        print('+++++++++++++++爬虫开始前执行+++++++++++++++++')
        # 在爬虫开始前就开打一个对象，用来写入数据
        self.fp = open('book.json', 'w', encoding='utf-8')

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


class DangDang_downloda_Pipeline:
    def process_item(self, item, spider):
        # 判断是否下载成功
        # item['book_img'], './book_img/' + item['book_name'] + '.jpg'
        urllib.request.urlretrieve(
            url='http:'+item.get('src'), filename='./book_img/' + item.get('name') + '.jpg')
        if item['name']:
            print('下载成功')
        else:
            print('下载失败')
        return item
