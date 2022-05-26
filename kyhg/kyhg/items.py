'''
Author: fgg
Date: 2022-05-26 14:22:40
LastEditors: fgg
LastEditTime: 2022-05-26 15:43:59
FilePath: \python_study_2022\kyhg\kyhg\items.py
Description: 学习用文件，主要就是笔记和随笔
Copyright (c) 2022 by fgg/Mechanical Design Studio, All Rights Reserved. 
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from turtle import title
from unicodedata import name
import scrapy


class KyhgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    names = scrapy.Field()
    contents = scrapy.Field()
    hrefs = scrapy.Field()
    pass
