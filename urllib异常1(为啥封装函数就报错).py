'''
Author: your name
Date: 2022-02-24 16:45:34
LastEditTime: 2022-02-25 10:36:33
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\urllib异常1.py
'''
# post请求
import urllib.request
import urllib.parse
from calendar import c
from urllib import request


def create_request():
    url = 'https://blog.csdn.net/qq_44706619/article/details/105263199'
    headres = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        # 'Cookie': '',
    }
    # data = {

    # }
    # 模拟post请求(传递data字典)
    # encoding：把一个Python对象编码转换成Json字符串
    # data = urllib.parse.urlencode(data).encode('utf-8')
    # 模拟get请求（拼接data字典）
    # data1 = urllib.parse.urlencode(data)
    request = urllib.request.Request(url=url, headers=headres)
    print('create_request执行成功')
    return request


def get_content(request):
    try:
        response = urllib.request.urlopen(request)
        # decoding：把Json格式字符串解码转换成Python对象
        content = response.read().decode('utf-8')
        return content
    except urllib.error.URLError as e:
        print(e.reason)

        print('get_content执行成功')
        return None


def down_load(content):
    if content:
        with open('test.html', 'w', encoding='utf-8') as f:
            f.write(content)
            print('下载成功')
    else:
        print('下载失败')
    print('down_load执行成功')


if __name__ == '__main__':

    request = create_request()
    content = get_content(request)
    down_load(content)
