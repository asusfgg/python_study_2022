'''
Author: your name
Date: 2022-03-25 14:54:16
LastEditTime: 2022-03-25 14:54:40
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\Scrapy基础\当当网\scrapy_dangdang_3_25\scrapy_dangdang_3_25\spiders\dang.py
'''
import scrapy


class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['http://category.dangdang.com/cp01.62.00.00.00.00.html']
    start_urls = ['http://category.dangdang.com/cp01.62.00.00.00.00.html']

    def parse(self, response):
        print('=========================================================')
        
        pass
