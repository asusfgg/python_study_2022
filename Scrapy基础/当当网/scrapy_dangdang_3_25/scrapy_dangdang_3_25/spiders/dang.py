'''
Author: your name
Date: 2022-03-25 14:54:16
LastEditTime: 2022-03-28 15:55:55
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\Scrapy基础\当当网\scrapy_dangdang_3_25\scrapy_dangdang_3_25\spiders\dang.py
'''
from gc import callbacks
import scrapy
from scrapy_dangdang_3_25.items import ScrapyDangdang325Item


class DangSpider(scrapy.Spider):
    name = 'dang'
    # 如果是多页下载，要调整allowed_domains的范围，如下：
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.62.00.00.00.00.html']
    # http://category.dangdang.com/pg2-cp01.62.00.00.00.00.html
    # http://category.dangdang.com/pg3-cp01.62.00.00.00.00.html
    # http://category.dangdang.com/pg4-cp01.62.00.00.00.00.html
    base_url = 'http://category.dangdang.com/pg'
    page = 1

    def parse(self, response):
        print('====================== 项目初始化成功 =======================')
        # 去定义item数据结构，在item文件中
        # 找xpath路径
        # src = //ul[@id="component_59"]/li//img/@src
        # ****** 图片这里有个懒加载，这TM是反爬措施 ******
        # ****** 注意观察，往下滑动页面，发现路径有变化，变化成谁，一定要看仔细 ******
        # ****** 然后再留意第一条数据，可能路径不匹配了 ******
        # ale = //ul[@id="component_59"]/li//img/@alt
        # price = //ul[@id="component_59"]/li//p[@class="price"]/span[1]/text()
        # 一页60个，一百页6000个 ， 好家伙
        # 规律：
        # 以上仨 共享li标签，都是li的子标签
        # 所以： 所有的selector都可以调用xpath方法
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            # print(li)
            src = li.xpath('.//img/@data-original').extract_first()
            # 如果，src： 表示src为none
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath(
                './/p[@class="price"]/span[1]/text()').extract_first()
            print(src, name, price)
            # 将数据交给pipeline
            # 代码首行得去导入一下items
            book = ScrapyDangdang325Item(src=src, name=name, price=price)
            # 交给pipeline去下载
            yield book
            # yield 表示 获得一个 交给管道一个 迭代

        if self.page < 100:
            self.page = self.page + 1
            url = self.base_url + str(self.page) + '-cp01.62.00.00.00.00.html'
        # 调用parse方法，继续解析下一页
        # 定义函数内调用 ,套娃操作??????
            # scrapy的get请求
            # callback是要执行的那个函数，parse是调用的函数，不允许加()
            yield scrapy.Request(url=url, callback=self.parse)

        print('======================= 项目运行结束 ========================')
        pass



