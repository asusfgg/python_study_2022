'''
Author: 千仞无锋
Date: 2022-02-07 04:09:13
LastEditors: 千仞无锋
LastEditTime: 2022-02-07 13:18:27
FilePath: \20220205HTML学习\关于操作文件.py
'''
# 打开文件/创建文件：
# 在python，使用open函数，可以打开一个已经存在的文件，或者创建一个新文件。
# 语法 ： open(文件路径，访问模式)  模式：可读 or 可写

# 创建文件

from genericpath import exists
from importlib.resources import path
import os   # Python的os模块中的exists来判断目录是否存在
from re import I

# open('text.txt', 'w')

# 打开文件
fp = open('obj.txt', 'w')
fp.write('hello world.')  # 覆盖了源文件的内容
# 关闭文件
fp.close()



# --------------------- 创建文件夹 ----------------------------------
a = os.path.exists('demo.txt')  # exists 存在
print(a)  # False 如果目录或者是文件存在则os便会返回TRUE的结果。

# 获取的当前最外层调用的脚本路径，即getPath所在的目录也可描述为起始的执行目录，A调用B，起始的是A，那么获取的就是A所在的目录路径。 获取脚本路径所在的上层目录。
b = os.getcwd()
print(b)            # H:\study-notes\JavaScript-study-notes\20220205HTML学习

os.mkdir(b+'\\folder')      # 创建b路径下的一个文件夹folder

# 判断体：
# 1、判断路径存在否
dirs = 'H:\study-notes\JavaScript-study-notes\20220205HTML学习\新建文件夹'
if not os.path.exists(dirs):
    os.makedirs(dirs)       # makedirs 创建多级目录的意思
else:
    print('已存在')


# 2、判断文件夹存在否
# os.path.dirname()：去掉脚本的文件名，返回目录。返回脚本文件所在的目录路径
# path = os.path.dirname(os.getcwd())+'\\demo0\\'
# if not os.path.exists(path):
#     os.makedirs(path)
# else:
#     print('已存在')


# 2、判断文件是否存在   ---------- ？？？？？？？？ -------------------
# filename = 'H:\study-notes\JavaScript-study-notes\20220205HTML学习\folder\新建文件夹\the-new-file.txt'
# if not os.path.exists(filename):
#     # 完蛋玩意
#     # os.system(r'{} md'.format(path))  
#     # # 调用windows系统命令行来创建文件
#     # 安装命令 npm install touch-cli -g 不好使呀
#     os.mkdir(filename+'\\folder')
#     fp = open(filename, 'w')
# else:
#     print('已存在')

# --------------------- 创建文件夹 ----------------------------------
