'''
Author: your name
Date: 2022-03-04 16:15:21
LastEditTime: 2022-03-07 14:46:41
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\xpath练习.py
'''
# 解析百度
# 获取网页源码
# 解析源码 etree.HTML
# 打印结果
from lxml import etree
import urllib.request
url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# print(content)
# with open('baidu首页.html', 'w', encoding='utf-8') as f:
#     f.write(content)
#     f.close()
tree = etree.HTML(content)
# print(tree)
result = tree.xpath('//input[@id="su"]/@value')
print(result)
# 