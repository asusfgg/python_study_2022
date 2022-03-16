'''
Author: 千仞无锋
Date: 2022-03-16 11:43:12
LastEditors: 千仞无锋
LastEditTime: 2022-03-16 17:35:04
FilePath: \python_study_2022\3-16-bs4解析练习.py
'''
# 星巴克 产品图片和名称 并且对应保存在本地
import urllib.request
import re
from bs4 import BeautifulSoup

url = 'https://www.starbucks.com/menu'


def create_request():
    url = 'https://www.starbucks.com.cn/menu/'
    headers = {
        # ':authority': 'www.starbucks.com',
        # ':method': 'GET',
        # ':path': '/menu',
        # ':scheme': 'https',
        'accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'accept-encoding': 'gzip, deflate, br',
        'accept-language':
        'zh-CN,zh;q=0.9',
        'cache-control':
        'max-age=0',
        'cookie':
        'AKA_A2=A; ux_exp_id=4f4ea721-d38a-4832-8933-570a99aad260; _gcl_au=1.1.2137732422.1647402354; _gid=GA1.2.986295488.1647402354; tiWQK2tY=A9lP1ZB_AQAAq4B9twxjhYfI2NDXmzQqCmJSm-NZpyoc7n29iNUKO1TTtgd2AWdhycKucpMswH8AAEB3AAAAAA|1|0|5a8d5a0209724b122a1aa1239a5c38e87a72144b; notice_behavior=implied,us; notice_gdpr_prefs=0,1,2:; notice_preferences=2:; cmapi_gtm_bl=; cmapi_cookie_privacy=permit 1,2,3; _ga_VMTHZW7WSM=GS1.1.1647402354.1.1.1647402374.0; _uetsid=a122e1f0a4db11ec82d83b8dd7fcde7c; _uetvid=a1233330a4db11ec9cb16794a05b063e; _ga=GA1.2.1682345083.1647402354; _gat_mpgaTracker1=1; RT="z=1&dm=www.starbucks.com&si=7833b58f-3397-4c5c-ae0e-614623b04466&ss=l0t0tqwz&sl=2&tt=4w0&rl=1&ld=1iyj&r=48wpdy16&ul=1iyj"',
        'dnt':
        '1',
        'referer':
        'https://www.starbucks.com/menu',
        'sec-ch-ua':
        '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile':
        '?0',
        'sec-ch-ua-platform':
        '"Windows"',
        'sec-fetch-dest':
        'document',
        'sec-fetch-mode':
        'navigate',
        'sec-fetch-site':
        'same-origin',
        'sec-fetch-user':
        '?1',
        'upgrade-insecure-requests':
        '1',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    try:
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        # 切片
        # content = content.split('(')[1].split(')')[0]
        return content
    except urllib.error.URLError as e:
        print(e.reason)
        return None


def down_load(content):
    if content:
        with open('星巴克.html', 'w', encoding='utf-8') as f:
            f.write(content)
            print('下载成功')
            f.close()
    else:
        print('下载失败')


if __name__ == '__main__':
    request = create_request()
    content = get_content(request)
    down_load(content)
    # （一） 解析网络回传数据
    # soup = BeautifulSoup(content, 'lxml')
    # 经过分析，要的是ul标签 grid padded-3 product这个类 ， 下的 strong标签里的内容
    # xpath语法：//ul[@class="grid padded-3 product"] 显示有22个
    # 再向下：//ul[@class="grid padded-3 product"]//strong/text()
    
    # （二） 解析本地数据
    soup = BeautifulSoup(open('星巴克.html', encoding='utf-8'), 'lxml')
    # 方法一
    # name_list = soup.select('.grid.padded-3.product strong')
    # 方法二
    name_list = soup.select('ul[class="grid padded-3 product"] strong')
    # print(name_list)
    for name in name_list:
        # 得到产品名列表
        print(name.get_text())
