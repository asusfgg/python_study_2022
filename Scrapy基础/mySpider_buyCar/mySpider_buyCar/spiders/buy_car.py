'''
Author: your name
Date: 2022-03-24 15:33:40
LastEditTime: 2022-03-25 11:23:13
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\mySpider_buyCar\mySpider_buyCar\spiders\buy_car.py
'''
import scrapy


class BuyCarSpider(scrapy.Spider):
    name = 'buy_car'
    allowed_domains = ['https://car.autohome.com.cn/price/brand-114.html']
    # url后缀是html时，不允许加斜杠
    start_urls = ['https://car.autohome.com.cn/price/brand-114.html']

    def parse(self, response):
        print('================================================================')
        print('项目建立成功')
        print('================================================================')
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        # print(name_list)
        # 因为是个列表，则可以遍历
        # for name in name_list:
        # .extract提取对象的data属性值
        #     print(name.extract())
        price_list = response.xpath(
            '//span[@class="lever-price red"]/span/text()')
        for i in range(len(name_list)):
            # 打印索引下标
            # print(i)
            # 对应打印
            print(name_list[i].extract(), price_list[i].extract())
        pass
