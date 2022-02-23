'''
Author: 千仞无锋
Date: 2022-02-14 20:43:05
LastEditors: 千仞无锋
LastEditTime: 2022-02-14 23:07:10
FilePath: \20220205Py学习\库.py
'''
from email import contentmanager
# urllib.request.urlopen()模拟浏览器向服务器发送请求
import urllib.request

# 1、定义一个url：
url = 'https://www.vipglobal.hk/detail-1710620765-6918544641033750493.html'

# 2、模拟浏览器向服务器发送请求：
# 拿个变量储存一下 response 响应
response = urllib.request.urlopen(url)

# 3、获取响应中的页面源码
# 整个变量存储一下 content 内容
# content = response.read()

# 4、打印数据
# print(content)
# 搞不好没中文内容 因为返回的是字节形式的二进制数据
# 输出中 有个 b' 源于read方法 ，表示这是字节数据

# 5、解码-数据转换（二进制转字符串）decode(‘编码格式’)
# 关键词在数据中的 head-mate-content-charset后面的值，就是编码格式
content = response.read().decode('utf-8')
print(content)

# 6、存到文本文件里（以字符串形式）
fp = open('content.txt', 'w', encoding='utf-8')
# 这个 encoding='utf-8' 一定要写，因为windows下的文本编辑器默认是gbk编码，会导致写入错误
# 防止乱码
fp.write(content)
# 带个小换行
fp.close()
