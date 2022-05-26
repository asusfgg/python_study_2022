'''
Author: fgg
Date: 2022-05-26 14:26:01
LastEditors: fgg
LastEditTime: 2022-05-26 16:01:59
FilePath: \python_study_2022\kyhg\kyhg\spiders\kyhgspider.py
Description: 学习用文件，主要就是笔记和随笔
Copyright (c) 2022 by fgg/Mechanical Design Studio, All Rights Reserved. 
'''
from tkinter.font import names
from certifi import contents
import scrapy
from kyhg.items import KyhgItem


class KyhgspiderSpider(scrapy.Spider):
    name = 'kyhgspider'
    allowed_domains = ['4006787252.com']
    start_urls = [
        'https://www.4006787252.com/index.php?ac=Search&at=List&pageid=1&mid=3&keyword=%E4%B8%99%E7%83%AF%E9%85%B8%E6%A0%91%E8%84%82']
    # https://www.4006787252.com/index.php?ac=Search&at=List&pageid=2&mid=3&keyword=%E4%B8%99%E7%83%AF%E9%85%B8%E6%A0%91%E8%84%82
    # https://www.4006787252.com/index.php?ac=Search&at=List&pageid=3&mid=3&keyword=%E4%B8%99%E7%83%AF%E9%85%B8%E6%A0%91%E8%84%82
    base_url = 'https://www.4006787252.com/index.php?ac=Search&at=List&pageid='
    page = 1

    def parse(self, response):
        print('====================== 初始化成功 =======================')
        print('*'*22+'爬取树脂相关信息'+'*'*23)
        # names ： //div[@class="sslb"]/ul/li/p/a/@title
        # contents ：//div[@class="sslb"]/ul/li/p/a
        li_list = response.xpath('//div[@class="sslb"]/ul/li')
        for li in li_list:
            print(li)
            names = li.xpath('./p/a/@title').extract_first()
            contents = li.xpath('./p/a').extract_first()
            hrefs = li.xpath('./p/a/@href').extract_first()
            print(names, contents, hrefs)
            sku = KyhgItem(names=names, contents=contents, hrefs=hrefs)
            yield sku
        if self.page < 100:
            self.page = self.page + 1
            url = self.base_url + \
                str(self.page) + \
                '&mid=3&keyword=%E4%B8%99%E7%83%AF%E9%85%B8%E6%A0%91%E8%84%82'
            yield scrapy.Request(url=url, callback=self.parse)
        pass
