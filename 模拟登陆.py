'''
Author: your name
Date: 2022-02-25 14:44:06
LastEditTime: 2022-02-25 15:49:43
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\模拟登陆.py
'''
# post请求
import urllib.request
import urllib.parse
from urllib import request



def create_request():
    url = 'https://weibo.cn/'
    headres = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        # 模拟登陆必须要有cookie的值，否则直接干到登录页面，报错编码错误
        'Cookie': '_T_WM=a3c389e1fbda65bfac27b7f968debfd2; SUB=_2A25PHPPxDeRhGeFN41EU9ivPzzqIHXVs_p25rDV6PUJbktCOLUKtkW1NQ95aXCi1q-NtbmnwFrMMKZud1z2VjYWO; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFwsxWOPBwkWN6EmxN90Yej5NHD95QNe0n0SKqfe0BcWs4DqcjLi--fiK.ci-zfi--fi-2Xi-2Ni--fiK.Ni-zNPEH8SbHFeCHWBBtt; SSOLoginState=1645773729',
        # 防盗链，判断当前路径是不是由上一个路径进来的，做图片防盗链
        'referer': 'https://passport.weibo.cn/'
    }
    # data = {

    # }

    # 模拟post请求(传递data字典)
# encoding：把一个Python对象编码转换成Json字符串
    # data = urllib.parse.urlencode(data).encode('utf-8')
    # 模拟get请求（拼接data字典）
    # data1 = urllib.parse.urlencode(data)
    request = urllib.request.Request(url=url, headers=headres)
    return request



def get_content(request):
    try:
        response = urllib.request.urlopen(request)
# decoding：把Json格式字符串解码转换成Python对象
        content = response.read().decode('utf-8')
        return content
    except urllib.error.URLError as e:
        print(e.reason)
        return None



def down_load(content):
    if content:
        with open('weibo.html', 'w', encoding='utf-8') as f:
            f.write(content)
            print('下载成功')
    else:
        print('下载失败')


if __name__ == '__main__':

    request = create_request()
    content = get_content(request)
    down_load(content)