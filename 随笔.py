'''
Author: your name
Date: 2022-02-22 12:22:09
LastEditTime: 2022-02-22 14:32:13
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \20220205Py学习\随笔.py
'''
from urllib import response
import urllib.request


def encodeing():
    user_input = input('输入关键词: ')
    keynames = urllib.parse.quote(user_input)
    url_old = 'https://www.baidu.com/s?w='
    url_new = url_old+keynames
    return(url_new)


TheEncode = encodeing()
data = {
    'wd': 'frf',
    'sex': 'male',
}

print(type(__init__))
# <class 'function'>
keywords = urllib.parse.urlencode(data)
print(keywords)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
request = urllib.request.Request(url=TheEncode, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)


