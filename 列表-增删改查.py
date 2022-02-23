'''
Author: 千仞无锋
Date: 2022-02-06 15:26:20
LastEditors: 千仞无锋
LastEditTime: 2022-02-06 23:11:02
FilePath: \20220205HTML学习\增删改查.py
'''
# --------- list增删改查 --------------


# --------- list增 -------------------
# 1、添加，追加（在list最后） append ：
foodList = ['铁锅炖大鹅', '酸菜五花肉', '小鸡炖蘑菇', '锅包肉']
foodList.append('再来一份 锦州大烧烤')
print(foodList)         # ['铁锅炖大鹅', '酸菜五花肉', '小鸡炖蘑菇', '锅包肉', '锦州大烧烤']

# ===========【Note：原队列插入，如果遇到none按照下面方法书写】===========

# 2、添加，插入（在list头部） insert ：
foodList1 = ['铁锅炖大鹅', '酸菜五花肉', '小鸡炖蘑菇', '锅包肉']
foodList1.insert(1, '酸菜大包砸')
print(foodList1)         # ['铁锅炖大鹅', '酸菜大包砸', '酸菜五花肉', '小鸡炖蘑菇', '锅包肉']
char_list = ['a', 'c', 'd']
char_list.insert(1, 'b')
print(char_list)         # ['a', 'b', 'c', 'd']

# 3、添加，继承  extend ：（self，iterable迭代（元组，列表））
number_list = [1, 2, 3]
number_list1 = [4, 5, 6]
number_list.extend(number_list1)
print(number_list)        # [1, 2, 3, 4, 5, 6]
# --------- list增 ------------------- 


# --------- list改 -------------------
# 1、修改
# 定义变量A，默认有3个元素
A = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
# ‐‐‐‐‐修改之前，列表A的数据‐‐‐‐‐A=['xiaoWang', 'xiaoZhang', 'xiaoHua']
print("‐‐‐‐‐修改之前，列表A的数据‐‐‐‐‐A=%s" % A)
# 修改元素
A[1] = 'xiaoLu'
# ‐‐‐‐‐修改之后，列表A的数据‐‐‐‐‐A=['xiaoWang', 'xiaoLu', 'xiaoHua']
print("‐‐‐‐‐修改之后，列表A的数据‐‐‐‐‐A=%s" % A)
# --------- list改 -------------------


# --------- 格式化出输 ----------------
# 在程序中，看到了%这样的操作符，这就是Python中格式化输出。
age = 18
name = "fgg"
# %s ：代表字符串缩写 spring ， %d ：代表的是data 【用的最多】
print("我的姓名是%s, 年龄是%d" % (name, age))  # 我的姓名是fgg, 年龄是18
# --------- 格式化出输 ----------------


# --------- list查 -------------------
# 1、判断下控制台输入的数据是否在此列表中

# definition


def LaCarteSystem():
    DBFood_list = ['锅包肉', '汆白肉', '乱炖']
    i = input('请点菜')
    if i in DBFood_list:
        print('二丫,上菜')
    else:
        print('不好意思,没有')


LaCarteSystem()

# 判断是否在列表中的函数


def JudgmentIsNotListed():
    ball_list = ['篮球', '台球']
    i = input('input ball name')
    if i not in ball_list:
        print('玩挺花啊')
    else:
        print('给你')


JudgmentIsNotListed()
# --------- list查 -------------------


# --------- list删 -------------------
# 列表元素的常用删除方法有：
# del：根据下标进行删除
# pop：删除最后一个元素
# remove：根据元素的值进行删除
DBdeliciousFood = ['铁锅炖大鹅', '酸菜五花肉', '小鸡炖蘑菇', '锅包肉', '汆白肉', '乱炖']
# 删除前['铁锅炖大鹅', '酸菜五花肉', '小鸡炖蘑菇', '锅包肉', '汆白肉', '乱炖']
print('删除前%s' % DBdeliciousFood)
del DBdeliciousFood[1]
# 删除后['铁锅炖大鹅', '小鸡炖蘑菇', '锅包肉', '汆白肉', '乱炖']
print('删除后%s' % DBdeliciousFood)


def Delfn():
    DBdeliciousFood = ['铁锅炖大鹅', '酸菜五花肉', '小鸡炖蘑菇', '锅包肉', '汆白肉', '乱炖']
    print('菜单展示%s' % DBdeliciousFood)
    i = input('输入菜名')
    if i in DBdeliciousFood:
        # 查找指定字符位置_查找列表中某个值的位置
        p = DBdeliciousFood.index(i)
        del DBdeliciousFood[p]
        print('删除后%s' % DBdeliciousFood)
    else:
        print('看清楚再动手啊')


Delfn()
# pop方法 删除最后一个元素
b_list = [1, 2, 3, 4, 5, 6]
b_list.pop()
print(b_list)  # [1, 2, 3, 4, 5]
# remove方法 根据元素的值进行删除 (传递列表参数进去)
c_list = ['a', 'b', 'c', 'd', 'e', 'f']
c_list.remove('a')  
print(c_list)  # ['b', 'c', 'd', 'e', 'f']

