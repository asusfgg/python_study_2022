'''
Author: your name
Date: 2022-03-29 10:06:56
LastEditTime: 2022-03-29 10:19:46
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\Scrapy基础\电影天堂\scrapy_movie_net\scrapy_movie_net\items.py
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyMovieNetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    src = scrapy.Field()

    pass
