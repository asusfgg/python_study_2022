'''
Author: your name
Date: 2022-03-24 10:18:08
LastEditTime: 2022-03-24 15:05:16
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\text_58city\text_58city\spiders\a58city.py
'''
import scrapy


class A58citySpider(scrapy.Spider):
    name = '58city'
    allowed_domains = [
        'https://xa.58.com/tech/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&final=1&jump=1&PGTID=0d300000-001e-345f-facb-94c283e9a907&ClickID=1']
    start_urls = [
        'https://xa.58.com/tech/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&final=1&jump=1&PGTID=0d300000-001e-345f-facb-94c283e9a907&ClickID=1']

    def parse(self, response):
        print('蛙哈哈哈哈哈哈哈哈哈哈!!!!!!!!!!')
        print('==================================================================')
        # 获取的是响应的字符串
        content = response.text
        # print(content)
        # 拿到了页面源码
        # print('==================================================================')
        # 拿到二进制的数据，就是那个b‘开头的html代码
        # content1 = response.body
        # print(content1)
        # print('==================================================================')
        # 直接使用xpath来解析response内容
        work_list = response.xpath(
            '//div[@class="main clearfix"]/div[@class="leftCon"]/ul/li/div/p[@class="job_require"]/span[@class="cate"]')
        # print(work_list.extract())
        print('==================================================================')
        # 提取seletor对象的data属性值
        # response.extract()
        print('==================================================================')
        # 提取seletor对象的列表的第一个数据
        # response.extract_first()
        print('==================================================================')
        pass
