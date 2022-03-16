'''
Author: 千仞无锋
Date: 2022-03-16 23:36:38
LastEditors: 千仞无锋
LastEditTime: 2022-03-16 23:59:02
FilePath: \python_study_2022\3-16-selenium自动化百度.py
'''
# 用selenium模拟浏览器访问
# 创建浏览器操作对象(路径填入)
from tkinter import Button
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(r"H:\study-notes\python_study_2022\msedgedriver-1153.exe")
driver = webdriver.Edge(service=s)
# 驱动浏览器访问网页
url = 'https://www.baidu.com/'
driver.get(url)
# 弹出的窗口 显示 受到自动测试软件的控制
content = driver.page_source
# print(content)
# with open('BD-3-16.html', 'w', encoding='utf-8') as f:
#     f.write(content)
# 根据id找到对象
button = driver.find_element_by_id('su')
print(button)
button = driver.find_element_by_name('wd')
print(button)
button = driver.find_elements_by_xpath("//input[@id='su']")
print(button)
button = driver.find_element_by_tag_name('input')
print(button)
# bs4语法
button = driver.find_element_by_css_selector('#su')
print(button)
# 链接文本，a标签文本 （报错）
# button = driver.find_element_by_link_text('百度一下')
# print(button)
