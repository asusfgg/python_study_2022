'''
Author: 千仞无锋
Date: 2022-02-07 00:33:30
LastEditors: 千仞无锋
LastEditTime: 2022-02-07 02:05:52
FilePath: \20220205HTML学习\字典-增删改查.py
'''
# 定义一个字典 有点向js的对象
from turtle import clear


person = {'name': 'fgg', 'age': 27}


# -------------------- 查询 ----------------------------
# 访问字典
print(person['name'])       # fgg
print(person['age'])        # 27 

# 若想用[]方式获取 字典中不存在的key值时
# print(person['sex'])        # 直接异常报错keyError

# 另一种方式获取 字典中不存在的key值时
# print(person.sex)           # 照样报错
# print(person.name)           # 报错，没这语法
print(person.get('name'))    # fgg
print(person.get('sex'))    # None 不报错了，但是是None
# -------------------- 查询 ----------------------------


# -------------------- 修改 ----------------------------
# 修改name
person['name'] = 'FengGG'
print('修改后为: %s' % person)  # 修改后为: {'name': 'FengGG', 'age': 27}
# -------------------- 修改 ----------------------------


# -------------------- 增加 ----------------------------
# 如果在使用 变量名['键'] = 数据 时，这个“键”在字典中，不存在，那么就会新增这个元素。
person['sex'] = 'Male'      # female 女性， male 男性
print(person.get('sex'))    # Male
person['name'] = '666'       #
print(person.get('name'))    # 666
# -------------------- 增加 ----------------------------


# -------------------- 删除 ----------------------------
# 对字典进行删除操作，有一下几种：
# del       删除指定元素；删库
# clear()   清空字典，但是保留字典对象

# 删除前的字典: {'name': '666', 'age': 27, 'sex': 'Male'}
print('删除前的字典: %s' % person)
del person['name']
# 删除之后字典: {'age': 27, 'sex': 'Male'}
print('删除之后字典: %s' % person)
person['name'] = 'FengGG'       #
print(person)                   # {'age': 27, 'sex': 'Male', 'name': 'FengGG'}
# 删库跑路：
del person
# print(person) # 报错，person未定义，好家伙，连根拔了

person0 = {'name': 'fgg', 'age': 27}
print('清空前的字典: %s' % person0)  # 清空前的字典: {'name': 'fgg', 'age': 27}
person0.clear()
print('清空之后字典: %s' % person0)  # 清空之后字典: {}
# -------------------- 删除 ----------------------------


# -------------------- 遍历 ----------------------------
person1 = {'name': 'fgg', 'age': 27, 'sex': 'Male'}

# 1、遍历key值  字典.keys()
for key in person1.keys():
    print(key)  # name age sex

# 2、遍历value值  字典.values()
for value in person1.values():
    print(value)  # fgg 27 Male

# 3、遍历key和value  items ：所有物品，项目，名目
for key, value in person1.items():
    print(key, value)   # name fgg   age 27   sex Male
for key in person1.items():
    print(key)          # ('name', 'fgg')   ('age', 27)  ('sex', 'Male') 项

# 4、遍历元素或项（以逗号隔开）
for item in person1.items():
    print(item)         # ('name', 'fgg')   ('age', 27)  ('sex', 'Male')

# -------------------- 遍历 ----------------------------
