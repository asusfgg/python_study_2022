'''
Author: your name
Date: 2022-03-03 15:21:19
LastEditTime: 2022-03-04 16:14:50
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\解析xpath.py
'''
from cgitb import handler
import urllib.request
import urllib.parse
import random
from lxml import etree
# url
# url = 'https://www.vipglobal.hk/detail-1710620765-6918544641033734109.html'
# 请求头
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
# }
# 请求对象定制
# request = urllib.request.Request(url, headers=headers)
# 发送请求
# response = urllib.request.urlopen(request)
# 代理ip池
# proxy_list = [
#     {'http': '111.59.199.58:8118'},
#     {'http': '101.34.214.152:8001'},
# ]
# handler
# handler = urllib.request.ProxyHandler(
#     proxy_list[random.randint(0, len(proxy_list) - 1)])
# opener
# opener = urllib.request.build_opener(handler)
# 发送请求
# response = opener.open(request)
# 获取响应内容
# content = response.read().decode('utf-8')
# print(content)
# 写入文件
# with open('vip.html', 'w', encoding='utf-8') as f:
#     f.write(content)
#     f.close()

# 解析xpath(严格遵守html标签，必须有结束标签)
# 1、解析本地文件
html_tree = etree.parse('供查找用.html', etree.HTMLParser())
# print(html_tree)
# <lxml.etree._ElementTree object at 0x0000000003A76840>
# tree.xpath('路径')
# 查找所有
list_1 = html_tree.xpath('//body//ul/li')
print(list_1)
# [<Element li at 0x3cd1b40>, <Element li at 0x3cd1ec0>, <Element li at 0x3cd1f00>, <Element li at 0x3cd1f40>]
print(len(list_1))
# 4
# 谓词查询
list_2 = html_tree.xpath('//body//ul/li[@id]/text()')
print(list_2)
#
print(len(list_2))
# 4
list_3 = html_tree.xpath('//body//ul/li[@id="1"]/text()')
print(list_3)
# 属性查询
li = html_tree.xpath('/ul[@id]/@class')
print(li)
# 查询id中包含数字的标签
list_4 = html_tree.xpath('//ul/li[contains(@id,"0")]/text()')
print(list_4)
# id以什么为开头
list_5 = html_tree.xpath('//ul/li[starts-with(@id,"1")]/text()')
# 逻辑运算
#  并且and
list_6 = html_tree.xpath(
    '//ul/li[starts-with(@id,"1") and contains(@class,"0")]/text()'
)
print(list_6)
# 或者or
list_7 = html_tree.xpath('//ul/li[starts-with(@id,"1") or contains(@class,"0")]/text()')
print(list_7)

# 属性运算
list_7 = html_tree.xpath('//ul/li[@id="1" or @id="2"]/text()')
print(list_7)




# 2、(常用)解析服务器响应内容 response.read().decode('utf-8')
# html = etree.HTML(content)
