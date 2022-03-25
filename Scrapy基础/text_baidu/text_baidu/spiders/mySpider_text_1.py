'''
Author: your name
Date: 2022-03-24 09:41:26
LastEditTime: 2022-03-24 09:53:24
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\text_baidu\text_baidu\spiders\mySpider_text_1.py
'''
import scrapy


class MyspiderText1Spider(scrapy.Spider):
    # 爬虫名字，用于运行爬虫时使用的值
    name = 'mySpider_text_1'
    # 允许访问的域名
    allowed_domains = ['www.baidu.com']
    # 起始的url地址（指的是第一次点进去要访问的域名）
    start_urls = ['http://www.baidu.com/']
    # 执行起始url后的方法，response为响应对象，
    # 相当于response = urllib.request.urlopen(start_urls)
    # 或者response = requests.get(start_urls)

    def parse(self, response):
        # print(response.text)
        print('苍茫的天涯是我的爱,绵绵的青山脚下花正开')
        # 不出意外，反爬了，接下来去干robots协议
        # pass
