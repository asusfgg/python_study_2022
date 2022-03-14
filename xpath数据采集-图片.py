'''
Author: your name
Date: 2022-03-07 15:23:06
LastEditTime: 2022-03-14 10:58:47
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\三月xpath.py
'''
# 爬取站长素材,高清图片前十页
# post请求
# get请求
import urllib.request
import urllib.parse
from urllib import request
from lxml import etree


def create_request(page):
    if (page == 1):
        url = 'https://sc.chinaz.com/tupian/shanshuifengjing.html'
    else:
        url = 'https://sc.chinaz.com/tupian/shanshuifengjing_' + \
            str(page) + '.html'

    headres = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        # 模拟登陆必须要有cookie的值，否则直接干到登录页面，报错编码错误
        'Cookie': 'Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1646638262,1647224136; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1647224156',
        # 防盗链，判断当前路径是不是由上一个路径进来的，做图片防盗链
    }
    # data = {

    # }

    # # 模拟post请求(传递data字典)
    # # encoding：把一个Python对象编码转换成Json字符串
    # data = urllib.parse.urlencode(data).encode('utf-8')
    # # 模拟get请求（拼接data字典）
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
    # urllib.request.urlretrieve(url, filename=None, reporthook=None, data=None)
    # 根据网页源码来获取分析图片地址。
    # 解析数据用xpath
    # 首先 把源码变成tree对象
    tree = etree.HTML(content)
    # 通过xpath获取到所有的图片地址
    # //div[@id="container"]//a/img/@src
    name_list = tree.xpath('//div[@id="container"]//a/img/@alt')
    print(len(name_list))
    for name in name_list:
        print(name)

    # src2是懒加载，但是图片加载完成后，就变成src。but 使用时害的用src2
    name_src = tree.xpath('//div[@id="container"]//a/img/@src2')
    print(len(name_src))
    # 涉及到图片的网站，都会进行懒加载，
    for i in range(len(name_list)):
        # print(i)
        name = name_list[i]
        src = name_src[i]
        # print(name,src)
        # 拼接一个https
        url = 'https:' + src
        # print(name,url)
        # 开始下载
        urllib.request.urlretrieve(url, './images/' + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page, end_page+1):
        # print(page)
        # 请求对象定制
        request = create_request(page)
        # 获取网页源码
        content = get_content(request)
        # 下载
        down_load(content)
