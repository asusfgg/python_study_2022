'''
Author: 千仞无锋
Date: 2022-02-15 00:48:04
LastEditors: 千仞无锋
LastEditTime: 2022-02-15 21:17:23
FilePath: \20220205Py学习\请求对象的定制.py
'''
import urllib.request

url = 'https://www.vipglobal.hk/detail-1710620765-6918544641033750493.html'

# url组成：6部分
# 协议：http 或者 https 区别在于安全度 ssl加密
# 主机：域名地址 www.vipglobal.hk
# 端口号： http 是80 ，https 是443 ，mysql 是3306，Oracle 是1521 ，Redis是6379 ，MongoDB 27017...
# 路径：s
# 参数：？后面的数据
# 锚点：#

response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
print(content)
# 输出结果不全，遇到反爬虫

# UA介绍：User Agent中文名为用户代理，简称 UA，它是一个特殊字符串头，使得服务器能够识别客户使用的操作系统及版本、CPU 类型、浏览器及版本。浏览器内核、浏览器渲染引擎、浏览器语言、浏览器插件等
# 查找本机UA : F12 网络 刷新 左侧名称中第一项 右边 标头 最底下 UA信息
# 语法：request = urllib.request.Request()

# 创建字典：
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}
# 请求对象的定制：
# 因为urlopen方法中 不能存储字典，所以headers不能传入
# 定制内容： url和headers都传递过去
request1 = urllib.request.Request(url=url,headers=headers) #这里面最好指定变量名和变量值
response1 = urllib.request.urlopen(request1)
content1 = response1.read().decode('utf-8')
print(content1)
# 输出结果完整了

