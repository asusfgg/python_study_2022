'''
Author: 千仞无锋
Date: 2022-02-07 13:47:11
LastEditors: 千仞无锋
LastEditTime: 2022-02-07 15:50:29
FilePath: \20220205HTML学习\序列化反序列化.py
'''
# 通过文件操作，我们可以将字符串写入到一个本地文件。但是，如果是一个对象(例如列表、字典、元组等)，就无
# 法直接写入到一个文件里，需要对这个对象进行序列化，然后才能写入到文件里。
# 设计一套协议，按照某种规则，把内存中的数据转换为字节序列，保存到文件，这就是序列化，反之，从文件的字
# 节序列恢复到内存中，就是反序列化。
# 对象---》字节序列 == = 序列化
# 字节序列--》对象 == =反序列化
# Python中提供了JSON这个模块用来实现数据的序列化和反序列化。
# JSON模块
# JSON(JavaScriptObjectNotation, JS对象简谱)是一种轻量级的数据交换标准。JSON的本质是字符串。
# 使用JSON实现序列化
# JSON提供了dump和dumps方法，将一个对象进行序列化。
# dumps方法的作用是把对象转换成为字符串，它本身不具备将数据写入到文件的功能。
from email import contentmanager
from fileinput import close
import json

file = open('names.txt', 'w')

# 列表对象
names = ['zhangsan', 'lisi', 'wangwu', 'jerry', 'henry', 'merry', 'chris']

# file.write(names) 出错，不能直接将列表写入到文件里 ， 不能往里面写对象
# write（）argument must be str  意为 write方法的参数必须是一个str字符串

# ------------------------ 序列化 开始 ---------------------------------
# 可以调用 json的dumps方法，传入一个对象参数
result = json.dumps(names)                  # ()传入的是个对象
# dumps 翻译 ：倾倒（抑郁）
# dumps 方法得到的结果是一个字符串

# ["zhangsan", "lisi", "wangwu", "jerry", "henry", "merry", "chris"]
# print(result)
# <class 'str'>
# print(type(result))


# 可以将字符串写入到文件里
file.write(result)
file.close()

# -------------- 另一种 dump方法 ------------------------------------
fp11 = open('b.txt', 'w', encoding="utf-8")

names11 = ['zhangsan', 'lisi', 'wangwu', 'jerry', 'henry', 'merry', 'chris']

json.dump(names11, fp11)  # ( 要写入谁 ， 写到哪里)

fp11.close()

# ------------------------ 序列化 结束 ---------------------------------


# ------------------------ 反序列化 开始 ---------------------------------
file1 = open('names.txt', 'r', encoding="utf-8")
content = file1.read()                 # content 翻译 ： 内容

# ["zhangsan", "lisi", "wangwu", "jerry", "henry", "merry", "chris"]
# print(content)
print(type(content))                # <class 'str'>

result1 = json.loads(content)

# ['zhangsan', 'lisi', 'wangwu', 'jerry', 'henry', 'merry', 'chris']
# print(result1)
print(type(result1))                # <class 'list'>


# --------- 嵌入一个序列化操作 ---------
result2 = json.dumps(result1)
# ["zhangsan", "lisi", "wangwu", "jerry", "henry", "merry", "chris"]
# print(result2)
print(type(result2))                # <class 'str'>
# --------- 嵌入一个序列化操作 ---------


file1.close()
file2 = open('names1.txt', 'w', encoding="utf-8")
file2.write(result2)
file2.close()


# 法二
#  同样 有个 load方法
file22 = open('c.txt', 'w', encoding="utf-8")
names22 = ['zhangsan', 'lisi', 'wangwu', 'jerry', 'henry', 'merry', 'chris']
json.dump(names22, file22)                      # （）里是文件

file22.close()

file22 = open('c.txt', 'r', encoding="utf-8")
result33 = json.load(file22)                    # （）里是数据
print('反序列后的类型为 %s' % type(result33))     # 所以上面那句话可以输出
file22.close()
# ------------------------ 反序列化 结束 ---------------------------------
