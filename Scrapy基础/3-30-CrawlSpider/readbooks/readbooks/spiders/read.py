'''
Author: your name
Date: 2022-04-07 10:34:05
LastEditTime: 2022-04-07 15:05:50
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\Scrapy基础\3-30-CrawlSpider\readbooks\readbooks\spiders\read.py
'''
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from readbooks.items import ReadbooksItem


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    # 下面这个大概率还得是目标url而不是主机url
    start_urls = ['https://www.dushu.com/book/1107.html']

    rules = (
        # allow 正则表达式 \d 匹配数字 + 匹配一个或多个 \. 匹配 .
        Rule(LinkExtractor(allow=r'/book/1107_\d+\.html'),callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        img_list = response.xpath('//div[@class="bookslist"]//img')
        for img in img_list:
            name = img.xpath('./@alt').extract_first()
            print('name:', name)
            src = img.xpath('./@src').extract_first()
            print('src:', src)
            photo = img.xpath('./@data-original').extract_first()
            print('photo:', photo)
            book = ReadbooksItem(name=name, src=src, photo=photo)
            yield book
        # return item

