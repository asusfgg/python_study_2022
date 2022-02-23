'''
Author: 千仞无锋
Date: 2022-02-07 15:52:37
LastEditors: 千仞无锋
LastEditTime: 2022-02-07 15:58:23
FilePath: \20220205HTML学习\异常.py
'''
# 异常
# 程序在运行过程中，由于我们的编码不规范，或者其他原因一些客观原因，导致我们的程序无法继续运行，此时，
# 程序就会出现异常。如果我们不对异常进行处理，程序可能会由于异常直接中断掉。为了保证程序的健壮性，我们
# 在程序设计里提出了异常处理这个概念。

# 整一个异常出来 用于实验
# fp = open('hahaha.txt','r',encoding="utf-8")
# fp.read()
# fp.close()
# [Errno 2] No such file or directory: 'hahaha.txt'

# 处理异常信息
# try:
#     # （可能出现的异常代码）
# except #（异常的类型）
#   
# fp = open  # （再来个友好提示）
try:
    fp = open('hahaha.txt', 'r', encoding="utf-8")
except FileNotFoundError:
    print('文件未找到')
    pass
