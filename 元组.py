'''
Author: 千仞无锋
Date: 2022-02-06 23:11:15
LastEditors: 千仞无锋
LastEditTime: 2022-02-06 23:51:48
FilePath: \20220205HTML学习\元组.py
'''
# Python的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号。
# python中不允许修改元组的数据，包括不能删除其中的元素。
# tuple 元组
aTuple = ('et', 77, 99.9)
print(type(aTuple))  # <class 'tuple'>
print(aTuple[0])  # et

aList = ['et', 77, 99.9]
print(aList[0])  # et
aList[1] = 66
print('aList is %s' % aList)  # aList is ['et', 66, 99.9]

bTuple = (5)
print(type(bTuple))  # <class 'int'> 整形类型？ 
# 非要变成元组 ：
bTuple1 = (5,)
print(type(bTuple1))  # <class 'tuple'>

