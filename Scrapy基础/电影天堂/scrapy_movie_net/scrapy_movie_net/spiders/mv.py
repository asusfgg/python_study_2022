'''
Author: your name
Date: 2022-03-29 10:11:39
LastEditTime: 2022-03-29 16:53:54
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\Scrapy基础\电影天堂\scrapy_movie_net\scrapy_movie_net\spiders\mv.py
'''
import scrapy
from scrapy_movie_net.items import ScrapyMovieNetItem

class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.dy2018.com']
    start_urls = ['http://www.dy2018.com/4/']

    def parse(self, response):
        print('=============== 第一步:检查是否有反爬 ================')
        print('=========== 成功输出表示可以进行下一步操作 ============')
        # 要第一页的名字，和相应第二页的图片
        # name = //div[@class="co_content8"]//td[2]//a[2]/text()
        # next_page_url = //div[@class="co_content8"]//td[2]//a[2]/@href
        # 因此，a_list是一个公共的xpath地址，可以复用的
        a_list = response.xpath(
            '//div[@class="co_content8"]//td[2]//a[2]')
        # next_page_url_list = response.xpath(
        #     '//div[@class="co_content8"]//td[2]//a[2]/@href').extract()
        # 对a_list进行遍历，可以生成每一个的name和href
        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            # print(name, href)
            # 次级页面地址
            next_page_url = 'http://www.dy2018.com' + href
            # print(next_page_url)
            # 对次级页面链接发起访问
            # 涉及到两个页面，要用mate参数传递参数
            yield scrapy.Request(url=next_page_url, callback=self.parse_next_page, meta={'name': name})

        pass

    def parse_next_page(self, response):
        # print('============= 调用parse next page 方法 ===============')
        # xpath地址： //div[@id="Zoom"]/img[1]/@src
        # 返回的是列表，提取数据用.extract_first()方法
        # span识别不了。。。。
        src = response.xpath('//div[@id="Zoom"]/img[1]/@src').extract_first()
        # print(src)
        # 接受请求的mate参数的name值
        name = response.meta['name']
        movie = ScrapyMovieNetItem(src=src, name=name)
        # movie返回给管道
        yield movie