'''
Author: your name
Date: 2022-03-29 10:06:56
LastEditTime: 2022-03-29 16:33:34
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\Scrapy基础\电影天堂\scrapy_movie_net\scrapy_movie_net\pipelines.py
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import urllib.request


class ScrapyMovieNetPipeline:
    def open_spider(self, spider):
        self.file = open('mv.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(str(item))
        return item

    def close_spider(self, spider):
        self.file.close()


class MV_picture_Pipeline:
    def process_item(self, item, spider):
        # 判断是否下载成功
        urllib.request.urlretrieve(
            url=item.get('src'), filename='./mv_img/' + item.get('name') + '.jpg')
        if item['name']:
            print('下载成功')
        else:
            print('下载失败')
        return item
