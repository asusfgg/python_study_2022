'''
Author: your name
Date: 2022-03-14 16:02:21
LastEditTime: 2022-03-14 17:03:27
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\3-14-jsonpath解析淘票票.py
'''
# 拿到淘票票的json数据，然后解析出所需要的数据
import json
import jsonpath
import urllib.request
import urllib.parse


def create_request():
    url = 'https://dianying.taobao.com/showAction.json?_ksTS=1647245108982_64&jsoncallback=jsonp65&action=showAction&n_s=new&event_submit_doGetSoon=true'
    headres = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        # 模拟登陆必须要有cookie的值，否则直接干到登录页面，报错编码错误
        'Cookie': 'cna=AF6oGi8ralYCAXUn55fcqq+6; t=734623426191768d4a2f11fc03f533f6; cookie2=1a93ff0f2956297326e3d8da2a1bbfec; v=0; _tb_token_=33935a75eeeeb; xlly_s=1; tfstk=c_U5B0A0dLvW-4sez71VzrTpf9gCwq8jiED4NkziTLju5A1mzFk1_AhWh2lKG; l=eBLYDuzILEc6-UB6BOfwourza77OSIRAguPzaNbMiOCP_85p5NnPW6meCNT9C3GVhsQ2R3R68gDTBeYBqn4rGiUYaxom40kmn; isg=BIyMWkt4AvEVbBaC-cJmKa6xXeq-xTBvhl7QxOZNmDfacSx7DtUA_4LHEXnJOWjH',
        # 防盗链，判断当前路径是不是由上一个路径进来的，做图片防盗链
    }
    data = {
        # ':authority': ' dianying.taobao.com',
        # ':method': ' GET',
        # ':path': ' /showAction.json?_ksTS=1647245108982_64&jsoncallback=jsonp65&action=showAction&n_s=new&event_submit_doGetSoon=true',
        # ':scheme': ' https',
        'accept': ' text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'accept-encoding': ' gzip, deflate, br',
        'accept-language': ' zh-CN,zh;q=0.9',
        'cookie': ' cna=AF6oGi8ralYCAXUn55fcqq+6; t=734623426191768d4a2f11fc03f533f6; cookie2=1a93ff0f2956297326e3d8da2a1bbfec; v=0; _tb_token_=33935a75eeeeb; xlly_s=1; tfstk=c_U5B0A0dLvW-4sez71VzrTpf9gCwq8jiED4NkziTLju5A1mzFk1_AhWh2lKG; l=eBLYDuzILEc6-UB6BOfwourza77OSIRAguPzaNbMiOCP_85p5NnPW6meCNT9C3GVhsQ2R3R68gDTBeYBqn4rGiUYaxom40kmn; isg=BIyMWkt4AvEVbBaC-cJmKa6xXeq-xTBvhl7QxOZNmDfacSx7DtUA_4LHEXnJOWjH',
        'dnt': ' 1',
        'referer: https': '//dianying.taobao.com/',
        'sec-ch-ua': ' " Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': ' ?0',
        'sec-ch-ua-platform': ' "Windows"',
        'sec-fetch-dest': ' empty',
        'sec-fetch-mode': ' cors',
        'sec-fetch-site': ' same-origin',
        'user-agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'x-requested-with': ' XMLHttpRequest',
        # 知识点： 默认情况下，默认情况下只支持
    }

    # 模拟post请求(传递data字典)
    # encoding：把一个Python对象编码转换成Json字符串
    data = urllib.parse.urlencode(data).encode('utf-8')
    # 模拟get请求（拼接data字典）
    # data1 = urllib.parse.urlencode(data)
    request = urllib.request.Request(url=url, data=data, headers=headres)
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
        with open('淘票票.html', 'w', encoding='utf-8') as f:
            f.write(content)
            print('下载成功')
    else:
        print('下载失败')


if __name__ == '__main__':

    request = create_request()
    content = get_content(request)
    down_load(content)
