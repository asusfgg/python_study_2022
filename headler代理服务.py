'''
Author: your name
Date: 2022-03-02 16:09:46
LastEditTime: 2022-03-02 16:35:21
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\headler代理服务.py
'''
url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=ip'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
from cgitb import handler
from urllib import response
import urllib.request
import urllib.parse
# 请求对象定制
request = urllib.request.Request(url=url,headers=headers)
# 模拟浏览器访问服务器
# response = urllib.request.urlopen(request)
# handler build_opener  open
# 代理ip池，以字典形式存在
proxies = {
    # 'http': '121.232.148.243:9000',
    # 'http':'117.114.149.66:55443',
    'http':'117.114.149.66:55443',
    # 'http':'58.20.234.243:9091',
}
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
# 获取响应信息
content = response.read().decode('utf-8')
# 保存
with open('daili.html','w',encoding='utf-8')as fp:
    fp.write(content)
    fp.close

