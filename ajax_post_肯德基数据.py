'''
Author: your name
Date: 2022-02-24 09:17:52
LastEditTime: 2022-03-14 16:12:25
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \20220205Py学习\ajax_post_肯德基数据.py
'''
# 导入工具包
from dataclasses import dataclass
import urllib.request
import json
import urllib.parse
# 需求：爬取肯德基官网
# 接口寻找
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
url1 = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
# 如何判断ajax：
# ajax核心对象 X-Requested-With: XMLHttpRequest
# post请求：


def down_load(page, content,location):
    with open(str(location)+'KFC门店地址_'+str(page)+'.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


def create_request(page, location):
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': location,
        'pid': '',
        'pageIndex': page,  # 区别在这里
        'pageSize': '10',
    }
    headers = {
        'Cookie': 'route-cell=ksa; ASP.NET_SessionId=2sqvg3rev014znlgtk5rtkqn; Hm_lvt_5fd8501a4e4e0eddf0c4596de7bd57ab=1645665623; Hm_lpvt_5fd8501a4e4e0eddf0c4596de7bd57ab=1645665635; SERVERID=83b58e85ddba4322790b382125ca179f|1645665815|1645665620',
        'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    }
    # 模拟Ajax请求/post请求，参数看需传递：三个，而且需要二次编码
    form_data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url=url, data=form_data, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

    # 这句是程序入口
if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))  # 返回的是字符串类型，利用int（）变成整形数据
    end_page = int(input('请输入终止页码'))
    location = input('输入市名: ')
    for page in range(start_page, end_page+1):
        # 每页都有自己的请求对象定制：
        request = create_request(page,location)
        # 第二步：获取响应数据：
        content = get_content(request)
        # 第三步：下载数据：
        down_load(page, content,location)



