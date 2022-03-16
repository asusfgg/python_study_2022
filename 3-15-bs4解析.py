'''
Author: 千仞无锋
Date: 2022-03-15 22:06:54
LastEditors: 千仞无锋
LastEditTime: 2022-03-16 11:42:57
FilePath: \python_study_2022\3-15-bs4解析.py
'''
from turtle import title
from bs4 import BeautifulSoup
# 解析本地文件，将bs4基础语法讲解
# 供查找用.html
# 加载本地文件
soup = BeautifulSoup(open('供查找用.html', encoding='utf-8'), 'lxml')
# print(soup) #错误，gbk编码
# print(soup.ul.name) # ul
# print(soup.ul.attrs) # {'class': ['list-group'], 'id': 'list-group'}    # 属性
# print(soup.find('ul')) # <ul class="list-group" id="list-group"> # 查找第一个
# print(soup.find('a',title="a2")) # <a href="http://www.baidu.com" title="a2">a2</a>
# # class不能直接用，应改为class_
# print(soup.find('a',class_="bd")) # <a href="http://www.baidu.com" class="bd">a1</a>

# 返回所有相关标签
# print(soup.find_all('a'))
# 放在列表里
# print(soup.find_all(['a','li']))
# print(soup.find_all('li',limit=2)) # 查找前两个

# # 选择器select
# print(soup.select('ul li')) # 查找所有li标签
# # 返回的是一个列表
# print(soup.select('.a1')) # 查找所有class为a1的标签
print(soup.select('#l3'))  # 查找所有id为3的标签
# print(soup.select('#0'))  # Note：id为0的标签不存在,不能把id写成纯数字

# 属性选择
print(soup.select('li[id="0"]'))  # 查找所有id为0的li标签

# 层级选择
# 后代选择器
print(soup.select('div li'))
# 子代选择器
# 某标签的第一级子标签
print(soup.select('div > ul'))  # 查找div标签的第一级子标签
print(soup.select('div > ul > li'))  # 查找div标签的第一级子标签的第一级子标签
print(soup.select('li,a'))

# 节点信息
# 获取节点内容
obj = soup.select('#d1')  #返回的是列表 列表没有string属性
obj = soup.select('#d1')[0]
# 如果标签对象中只有内容，那么string和get_text()方法都可以获取内容
# 如果标签对象中还有标签，那么string就获取不到标签的内容，而get_text()方法可以获取内容
print(obj.get_text())  # 获取节点内容
print(obj.string)  # 获取节点内容

# 节点属性
obj1=soup.select('#p1')[0] 
# name是标签的名字
print(obj.name)
# 属性值作为字典返回
print(obj.attrs)
# 节点类型
obj2 = soup.select('#p1')[0]
print(obj2.attrs.get('class'))
print(obj2.get('class'))
print(obj2['class']) #容易报错，如果没找到的话
