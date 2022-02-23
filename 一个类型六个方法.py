'''
Author: 千仞无锋
Date: 2022-02-14 23:04:08
LastEditors: Please set LastEditors
LastEditTime: 2022-02-18 16:08:06
FilePath: \20220205Py学习\一个类型六个方法.py
'''
from email import contentmanager
from importlib.resources import contents
from ntpath import join
import urllib.request

url = 'https://www.vipglobal.hk/detail-1710620765-6918544641033750493.html'

# 模拟浏览器发送请求
response = urllib.request.urlopen(url)

# 一个类型HTTPResponse，六个方法read;readline;readlines;getcode;geturl;getheaders：

print(type(response))
# <class 'http.client.HTTPResponse'>
# 说明 response是HTTPresponse的类型

# 一个字节一个字节的读取
# content = response.read()

# 高效方法
# content = response.read(5) # 读5个字节
# content = response.readline() # 只读取了一行
# content = response.readlines() # 按行读取，直到读完

# 返回状态码：
print(response.getcode())
# 200证明逻辑无错误

# 返回URL地址
print(response.geturl())

# 输出状态信息
print(response.getheaders())

