'''
Author: your name
Date: 2022-04-01 13:46:10
LastEditTime: 2022-04-07 11:25:53
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\Scrapy基础\3-30-CrawlSpider\readbooks\readbooks\pipelines.py
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ReadbooksPipeline:

    def open(self, spider):
        self.fp = open('readbooks.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    def close(self, spider):
        self.fp.close()
