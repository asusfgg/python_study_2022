'''
Author: your name
Date: 2022-03-21 10:00:23
LastEditTime: 2022-03-21 15:59:37
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\3-21-requests-cookic-古诗文网.py
'''
# 需求：
# 古诗文网 干验证码 登陆
# 通过登陆进入到主界面
# 难点：
# 验证码 (绕过登录的绊脚石)
# 解题思路：
# 找登陆接口 （用错误密码去试探） login开头的 携带一大堆参数
# =============================================================================
# 这三是变化的：
# __VIEWSTATE: AH4XFKAiPLuvvunXw3J7I9zdt0fT82KvFJ5yunl/OSjh2YgF2o9F3oLejKgtnYkBganyMfJWua+KeL7EvdPDSDJ3g+eTcpYr5F0VkLcRlCFUdbz1pc122+xenXI=
# __VIEWSTATEGENERATOR: C93BE1AE
# code: KURE
# -----------------------------------------------------------------------------
# 这四个是固定的：
# from: http://so.gushiwen.cn/user/collect.aspx
# email: asusfgg@hotmail.com
# pwd: 10420449200
# denglu: 登录
# ==============================================================================


import urllib.request
from bs4 import BeautifulSoup
import requests


# 难点：
# 1、__VIEWSTATE:  __VIEWSTATEGENERATOR:
# 解析1：一般情况 network看不到数据包的时候，都是在页面的源码中。在源码中去搜索这俩参数
# 关键单词：hidden:隐藏域 表示页面不显示 但是页面存在。
# 思路1:获取登录页源码就可以把这两个参数的值 解析出来,就是说浏览器在加载页面时已经把这俩值获取好了,但是是隐藏域里的.
# 这是登录页面的url地址

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
# 访问url获取页面源码
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
content = response.text
# 打印
print(content)


# 解析页面源码
soup = BeautifulSoup(content, 'lxml')  # lxml是内核
# 获取view state
# id选择器 用#号 ，返回的是个列表，【0】用来取数据，.attrs获取属性，.get('value')得到value值
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
# 打印测试
print(viewstate, viewstategenerator)

# 2、验证码code
# 解析2：检查验证码，通过控制台，检查验证码图片所在代码行，检查对应元素：Current source:	https://so.gushiwen.cn/RandCode.ashx
# 来了个地址？？Current source:	https://so.gushiwen.cn/RandCode.ashx 那么，获取到图片就知道验证码是啥
# 因为本来的src跟的应该是图片的路径，但是现在是个/RandCode.ashx 一个参数 里面有个 url地址
# 思路2：获取验证码图片；通过id选择，通过src属性值来获取路径
code = soup.select('#imgCode')[0].attrs.get('src')
print(code)
# 发现/RandCode.ashx之前拼接了一个 https://so.gushiwen.cn
# 拼接一下：
code_url = 'https://so.gushiwen.cn'+code
print(code_url)
# 获取了验证码图片之后,下载到本地,人肉观察验证码,人肉输出验证码...不太聪明的样子
# ******** 有坑，因为一次请求一个图，第二次请求用上次的图，就不灵光了。 ********
# 头铁测试：
# 下载验证码图片
# urllib.request.urlretrieve(code_url, filename='code_last.jpg')

# ******** requests 方法 通过 其下的session（）方法，使得请求变成一个对象。 ********
session = requests.session()
# 取得验证码的url的内容.
response_code = session.get(url=code_url)
# ****** 此时不能用文本，要用二进制数据，因为是二进制数据 ******
content_code = response_code.content
with open('code.jpg', 'wb') as f:
    # wb 表示将二进制数据 写入到文件中。
    f.write(content_code)
    f.close()

code_name = input('请输入你的验证码:')
# 登陆
# 登陆接口：控制台选 preserive log 如果版本低，登陆后那个login开头那个接口就没了
login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': 'asusfgg@hotmail.com',
    'pwd': '1042044920',
    'code': code_name,
    'denglu': '登录',
}

# 访问request改为session
response_post = session.post(url=login_url, data=data_post, headers=headers)
content_post = response_post.text

with open('古诗文网.html', 'w', encoding='utf-8') as f:
    f.write(content_post)
    f.close()
