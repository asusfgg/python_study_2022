'''
Author: your name
Date: 2022-03-03 15:10:06
LastEditTime: 2022-03-03 15:20:43
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\代理池.py
'''
from cgitb import handler
from urllib import response
import urllib.request
import urllib.parse
import random


proxies_pool = [
    # 全部不好使，免费的果然不好用
    {'http': '61.216.156.222:60808'},
    {'http': '183.247.207.225:30001'},
    {'http': '115.218.2.108:9000'},
]
# 随机出来的代理ip
proxies = random.choice(proxies_pool)
print(proxies)

url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=ip'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
# 请求对象定制
request = urllib.request.Request(url=url,headers=headers)
# 模拟浏览器访问服务器
# response = urllib.request.urlopen(request)
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
# 获取响应信息
content = response.read().decode('utf-8')
# 保存
with open('daili.html','w',encoding='utf-8')as fp:
    fp.write(content)
    fp.close
