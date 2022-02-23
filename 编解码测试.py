'''
Author: 千仞无锋
Date: 2022-02-16 23:03:51
LastEditors: Please set LastEditors
LastEditTime: 2022-02-22 11:13:28
FilePath: \20220205Py学习\编解码测试.py
'''
import urllib.request

# 定义一个转码函数：


def baidu():
    a = input('你想查点啥,输入: ')
    # 将汉字转为Unicode编码
    keynames = urllib.parse.quote(a)
    # https://www.baidu.com/s?w=%E5%94%AF%E5%93%81%E4%BC%9A
    url = 'https://www.baidu.com/s?w='
    url_new = url+keynames
    return(url_new)


# 调用转码函数：
i = baidu()
print(i)

# 初级请求四部曲：
# UA定制
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}
# 模拟请求
request = urllib.request.Request(url=i, headers=headers)
# 回传响应
response = urllib.request.urlopen(request)
# 内容编码存储

content = response.read().decode('utf-8')


# 打印输出：
print(content)

# 写入文本：


def writefile(contents):
    try:
        filename = input('文件名为: ')
        encode = input('编码为: ')
        fp = open(filename+'.html', 'w', encoding=encode)
        fp.write(contents)
        fp.close()
    except FileNotFoundError:
        print('文件未找到')
        pass


writefile(content)



