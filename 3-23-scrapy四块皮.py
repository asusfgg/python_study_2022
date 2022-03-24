'''
Author: your name
Date: 2022-03-23 14:29:20
LastEditTime: 2022-03-24 10:19:20
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\Chaojiying_Python\chaojiying_Python\3-23-scrapy四块皮.py
'''
# scrapy:提取结构性数据的框架(比如一堆li标签的)
# 1、首先得从cmd创建项目
# 指令为： scrapy startproject mySpider_xxxxxxxx 不能有中文

# 2、到项目文件下进入一个文件夹

# 3、在spider文件夹下创建一个爬虫文件
# 路径格式为：cd mySpider_xxxxxxxx\mySpider_xxxxxxxx\spiders
# 指令：scrapy genspider 需要另取文件名 https://www.baidu.com
# 有时在vscode终端中运行，会报错 就到文件夹下，cmd窗口中执行。

# 4、运行爬虫
# 指令 ：scrapy crawl mySpider_xxxxxxxx
