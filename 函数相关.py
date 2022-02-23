'''
Author: 千仞无锋
Date: 2022-02-07 02:18:41
LastEditors: 千仞无锋
LastEditTime: 2022-02-07 04:08:46
FilePath: \20220205HTML学习\函数相关.py
'''
# 思考一个问题
from cgitb import text
from re import I


def buyIceCream():
    return '冰激凌'


buyIceCream()           # 啥也没有 因为没有东西去存放这个return过来的值
#  故 ，应该如下书写：
i = buyIceCream()  # 用一个变量去接收返回值
print(i)                # 冰激凌

# -------- 数值转化 ------------
# 函数 说明
# int(x) 将x转换为一个整数
# float(x) 将x转换为一个浮点数
# str(x) 将对象 x 转换为字符串
# bool(x) 将对象x转换成为布尔值
# -------- 数值转化 ------------


def calculator(a, b):
    a = int(a)
    b = int(b)
    i = a + b
    return i


i = calculator(1, 2)
print(i)  # 3

c = input('input c')
d = input('input d')
j = calculator(c, d)
print(j)  # 8


# 定义全局变量
a = 100


def test1():
    b = 50      # 局部变量
    print(a)    # 虽然没有定义变量a但是依然可以获取其数据


# def test2():
#     print(b)    # b无法获取到 name 'b' is not defined


# 调用函数
test1()         # 100


def test3():
    c = 40

    def test4():
        d = 30
        print(c)

    test4()

    # print(d) # 获取不到d
    print(c)


test3()  # 40 40

#  在满足条件的情况下，使用作用域最小的变量范围 