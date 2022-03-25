'''
Author: your name
Date: 2022-03-25 14:54:16
LastEditTime: 2022-03-25 15:43:23
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\Scrapy基础\当当网\scrapy_dangdang_3_25\scrapy_dangdang_3_25\spiders\dang.py
'''
import scrapy


class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['http://category.dangdang.com/cp01.62.00.00.00.00.html']
    start_urls = ['http://category.dangdang.com/cp01.62.00.00.00.00.html']

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
            alt = li.xpath('.//img/@alt').extract_first()
            price = li.xpath(
                './/p[@class="price"]/span[1]/text()').extract_first()
            print(src, alt, price)

        print('======================= 项目运行结束 ========================')
        pass
