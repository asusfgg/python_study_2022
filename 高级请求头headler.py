'''
Author: your name
Date: 2022-02-25 16:11:45
LastEditTime: 2022-03-01 11:06:53
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\高级请求头headler.py
'''
# 这个头的用处就在于代理ip
from cgitb import handler
import urllib.request
import urllib.parse

# handler处理器使用
# 需求使用handler访问百度，获取源码
url = 'https://www.baidu.com'
# 请求头hearders
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
# 请求对象定制
request=urllib.request.Request(url=url,headers=headers)
# handler
# 获取handle对象
handler = urllib.request.HTTPHandler()
# build_opener
# 通过handler获取opener对象
opener = urllib.request.build_opener(handler)
# open
# 调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)

