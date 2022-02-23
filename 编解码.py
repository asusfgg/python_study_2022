'''
Author: 千仞无锋
Date: 2022-02-15 22:44:33
LastEditors: 千仞无锋
LastEditTime: 2022-02-15 23:11:37
FilePath: \20220205Py学习\编解码.py
'''
# 原本url：https://www.baidu.com/s?wd=唯品会
# 复制进来后：https://www.baidu.com/s?wd=%E5%94%AF%E5%93%81%E4%BC%9A
# 这堆：%E5%94%AF%E5%93%81%E4%BC%9A 就是“唯品会”的编码
# Unicode编码 统一。
# 所以这堆 %E5%94%AF%E5%93%81%E4%BC%9A 就是“唯品会”的Unicode编码
from email import header
import urllib.request

# 汉字变成Unicode编码
# urllib.parse.quote()
# url = 'https://www.baidu.com/s?wd=%E5%94%AF%E5%93%81%E4%BC%9A'
name = urllib.parse.quote('唯品会')
print(name)
# %E5%94%AF%E5%93%81%E4%BC%9A
url = 'https://www.baidu.com/s?wd=name'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# print(content)

fp = open('baidu.txt','w',encoding="utf-8") 
fp.write(content)
fp.close()

urllib.request.urlretrieve(url,'baidu.html')


