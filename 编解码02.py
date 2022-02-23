'''
Author: your name
Date: 2022-02-16 10:46:41
LastEditTime: 2022-02-22 12:09:04
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \20220205Py学习\编解码02.py
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

# 新的转码函数（针对多参数）
# https://www.baidu.com/s?wd=冯若凡&sex=男

# 定义一个字典
data = {
    'wd': 'frf',
    'sex': 'male',
    'location': 'shanxi'
}

# urlencode方法会转码后，将字典拼接起来。
a = urllib.parse.urlencode(data)
print(a)
# wd=%E5%86%AF%E8%8B%A5%E5%87%A1&sex=%E7%94%B7&location=%E9%99%95%E8%A5%BF




# 初级请求四部曲：
# UA设置
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
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

# 下载html源文件：
# urllib.request.urlretrieve (url_new,'vip1.html') #不太好使。
