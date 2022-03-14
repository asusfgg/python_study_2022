'''
Author: your name
Date: 2022-03-14 14:39:09
LastEditTime: 2022-03-14 16:00:54
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\json解析.py
'''
import json
import jsonpath

obj = json.load(open('3-14-jsonpath解析.json', 'r', encoding='utf-8'))
# print(obj)
# 爬取store里的书的作者author
# jsonpath语法：$.store.book[*].author  解释为：根元素下的store下的book下的author
author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
# print(author_list)


# 所有的作者可能含有除了book以外的类目
author_list1 = jsonpath.jsonpath(obj, '$..author')
# print(author_list1)

# store下的所有的元素
tag_list = jsonpath.jsonpath(obj, '$.store.*')
# print(tag_list)

# stroe下的所有的pric
price_list = jsonpath.jsonpath(obj, '$..price')
price_list1 = jsonpath.jsonpath(obj, '$.store..price')
# print(price_list)
# print(price_list1)

# 第三本书
book = jsonpath.jsonpath(obj, '$..book[3]')
# print(book)

# 最后一本书
last_book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
# print(last_book)

# 前两本书
first_two_books = jsonpath.jsonpath(obj, '$..book[0:2]')
# print(first_two_books)

# 过滤出所有包含版本号isbn的书
have_isbn = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')  # [？（这里面是约束条件）]
# print(have_isbn)

# 价格超过十元的书
price_more_than_the_10 = jsonpath.jsonpath(obj, '$..book[?(@.price>10)]')
print(price_more_than_the_10)
