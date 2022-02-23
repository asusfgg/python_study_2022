'''
Author: your name
Date: 2022-02-22 14:32:29
LastEditTime: 2022-02-22 15:09:40
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \20220205Py学习\post请求方法.py
'''
from base64 import encode
from email.base64mime import header_length
from re import U
import urllib.request
# request method 请求方式 ， 为post方式
# kw = ''
# 找接口 lengdatect 就是接口
url='https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
# post请求参数放置位置：
data={
    'kw':'spider'
}
# post请求的参数必须要进行编码(第二次编码)
data=urllib.parse.urlencode(data).encode('utf-8')
print(data)
# b'kw=spider'

# post请求的参数是不会拼接到url的后面的,而是放在请求对象定制的参数中（区别于get请求）
request=urllib.request.Request(url=url,data=data,headers=headers)
# 模拟浏览器发送请求
response = urllib.request.urlopen(request)
print(response) # 报错了
# POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.
# <http.client.HTTPResponse object at 0x0000000003A61A30>

content = response.read().decode('utf-8')
print(content)
# {"errno":1000,"errmsg":"\u672a\u77e5\u9519\u8bef"}
# {"errno":0,"data":[{"k":"spider","v":"n. \u8718\u86db; \u661f\u5f62\u8f6e\uff0c\u5341\u5b57\u53c9; \u5e26\u67c4\u4e09\u811a\u5e73\u5e95\u9505; \u4e09\u811a\u67b6"},{"k":"Spider","v":"[\u7535\u5f71]\u8718\u86db"},{"k":"SPIDER","v":"abbr. SEMATECH process induced damage effect revea"},{"k":"spiders","v":"n. \u8718\u86db( spider\u7684\u540d\u8bcd\u590d\u6570 )"},{"k":"spidery","v":"adj. \u50cf\u8718\u86db\u817f\u4e00\u822c\u7ec6\u957f\u7684; \u8c61\u8718\u86db\u7f51\u7684\uff0c\u5341\u5206\u7cbe\u81f4\u7684"}]}

# s= u'\u672a\u77e5\u9519\u8bef'
# print(s) # 未知错误

# json数据
import json
obj = json.loads(content)
print(obj)
# {'errno': 1000, 'errmsg': '未知错误'} 错误是接口找错了
# {'errno': 0, 'data': [{'k': 'spider', 'v': 'n. 蜘蛛; 星形轮，十字叉; 带柄三脚平底锅; 三脚架'}, {'k': 'Spider', 'v': '[电影]蜘蛛'}, {'k': 'SPIDER', 'v': 'abbr. SEMATECH process induced damage effect revea'}, {'k': 'spiders', 'v': 'n. 蜘蛛( spider的名词复数 )'}, {'k': 'spidery', 'v': 'adj. 像蜘蛛腿一般细长的; 象蜘蛛网的，十分精致的'}]}