'''
Author: 千仞无锋
Date: 2022-02-06 02:38:40
LastEditors: 千仞无锋
LastEditTime: 2022-02-06 15:37:07
FilePath: \20220205HTML学习\重拾python的第一天.py
'''
from ast import NotIn
from calendar import c
from gettext import find
from ntpath import join
import this
import turtle

# 特别注意：Python这语言特别注重缩进，以缩进判断各种代码段
# -------------------------------------
# 单行注释 。 note：注释要写在代码上面 2022-02 习惯更改。
 

print('hello world')
# 多行注释
'''
这是多行注释
'''
# -------------------------------------
# 变量：
# 语法：变量名 = 变量值
weather = "定义了一个叫天气的变量"
print(weather)
# ---------if语法--------------
# if 判断条件 ：
i = 0
if i < 10:
    print(weather)
# ---------if语法--------------

# ---------for语法--------------
# for 变量 in 要遍历的数据 ： 方法体
# 1、遍历字符串
s = 'china'

# ---------字符串方法--------------
# 判断s长度
print(len(s))                # 5
# 查找
print(s.find('c'))           # 0
# 判断开头结尾
print(s.startswith('c'))     # true
print(s.endswith('c'))       # false
# 计算出现次数
print(s.count('c'))          # 1
# 替换
print(s.replace('c', 'C'))   # China
# 切割
s0 = 'c-h-i-n-a'
print(s0.split('-'))     # ['c', 'h', 'i', 'n', 'a']
# 大小写转换
print(s.upper())         # CHINA
i = s.upper()
print(i.lower())         # china
# 去空格
s1 = '   a aa aa   '
print(len(s1))           # 13
i = s1.strip()
print(len(i))            # 7 字符串中间的空格不去掉
# 拼接
print(join(s0, s1))      # c-h-i-n-a\   a aa aa  灵魂写法 需要导入头函数才能执行
s9 = 'a'
print(s9.join('hello'))  # haealalaod 基础教程中安全写法
# ---------字符串方法--------------


# ---------for语法----------------
for i in s:
    print(i)              # 遍历输出china
# 2、循环
# range(起始值，结束值，步长值) 注意左闭右开区间，取不到右边的端点值
for i in range(2):
    if i < 2:
        print('来2个循环出输')

for i in range(3):
    print(i)               # 0 1 2 左闭右开区间
# ---------for语法----------------


# ---------while循环--------------
j = 1
while j <= 4:
    if j <= 3:
        print('循环')
    else:
        print('gg')
    j = j+1
# --------------------------------------


# 3、遍历列表下标
a_list = ['a', 'b', 'c']
# 方法调用是 ： 方法名（对象）
for i in range(len(a_list)):
    print(i)

