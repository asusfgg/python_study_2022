'''
Author: your name
Date: 2022-03-25 14:52:28
LastEditTime: 2022-03-25 15:08:33
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\Scrapy基础\当当网\scrapy_dangdang_3_25\scrapy_dangdang_3_25\items.py
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDangdang325Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 通俗说，要下载的数据都有啥，就定义啥
    # 1 先爬一下图片
    src = scrapy.Field()
    # 2 再爬一下标题
    name = scrapy.Field()
    # 3 最后爬一下价格
    price = scrapy.Field()
    pass
