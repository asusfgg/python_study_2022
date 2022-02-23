'''
Author: your name
Date: 2022-02-23 10:11:10
LastEditTime: 2022-02-23 15:42:55
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \20220205Py学习\豆瓣.py
'''
from importlib import import_module
from urllib import response
import urllib.request
from email import header
# 抓接口：
url = 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100:90&action=&start=0&limit=20'
headers = {
    # 'Accept': ' */*',
    # 'Accept-Encoding': ' gzip, deflate, br', 这行高低给干掉
    # 'Accept-Language': ' zh-CN,zh;q=0.9',
    # 'Connection': ' keep-alive',
    'Cookie': ' ll="118378"; bid=rmuzZP9uilo; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1645585436%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DnsdCzK0ZvBDdu0ShhH-HLiceq-9awUnk6tPtZrNfPamMMBGDN3UdqFy3uzPP3tHH%26wd%3D%26eqid%3Dd4a69b4d000038f0000000066215a3dd%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1358641776.1645582330.1645582330.1645585436.2; __utmb=30149280.0.10.1645585436; __utmc=30149280; __utmz=30149280.1645585436.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1014032229.1645582330.1645582330.1645585436.2; __utmb=223695111.0.10.1645585436; __utmc=223695111; __utmz=223695111.1645585436.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_id.100001.4cf6=f74601e2726bc47f.1645582331.2.1645585492.1645582779.',
    # 'DNT': ' 1',
    # 'Host': ' movie.douban.com',
    # 'Referer: https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100': '90&action=',
    # 'sec-ch-ua': ' " Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    # 'sec-ch-ua-mobile': ' ?0',
    # 'sec-ch-ua-platform': ' "Windows"',
    # 'Sec-Fetch-Dest': ' empty',
    # 'Sec-Fetch-Mode': ' cors',
    # 'Sec-Fetch-Site': ' same-origin',
    'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    # 'X-Requested-With': ' XMLHttpRequest',
}
data = {
    'type': ' 17',
    'interval_id: 100': '90',
    'action': ' ',
    'start': ' 0',
    'limit': ' 20',
}
# 获取排行榜 保存
# 第一步：请求对象定制
request = urllib.request.Request(url=url,headers=headers)
# 第二步：获取响应数据
response = urllib.request.urlopen(request)
# 第三步：存储数据
content = response.read().decode('utf-8')
print(content)
# 第四步：下载数据
# open方法默认gbk编码，若有汉字，需要encodeing为utf-8
# fp = open('douban.json','w',encoding='utf-8')
# fp.write(content)
# fp.close()
with open('douban1.json','w',encoding='utf-8') as fp:
    fp.write(content)
