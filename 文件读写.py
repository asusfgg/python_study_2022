'''
Author: 千仞无锋
Date: 2022-02-07 13:19:16
LastEditors: 千仞无锋
LastEditTime: 2022-02-07 13:45:49
FilePath: \20220205HTML学习\文件读写.py
'''
# 覆盖式读写w (如果文件存在，先清空再写入)
from email import contentmanager


fp = open('a.txt', 'w', encoding="utf-8")       # 防止乱码
fp.write('这是第一次写入的内容 \n' * 5)           # 带个小换行
fp.close()

# 追加数据 a方法
fp = open('a.txt', 'a', encoding="utf-8")
fp.write('这是第二次写入的 \n' * 10)
fp.close()

# 读取数据
fp = open('a.txt', 'r', encoding="utf-8")
# 默认下，read（）是按照字节读取，效率低
# content = fp.read()
# print(content)

# 按照行读取
# content = fp.readline()
# 这是第一次写入的内容   只读取到一行
# print(content)

# 读取所有行 （列表返回，元素为行内容）
content = fp.readlines()
# ['这是第一次写入的内容 \n',....       读取到所有 但是，是个列表
print(content)

