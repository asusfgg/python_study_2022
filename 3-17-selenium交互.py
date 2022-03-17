'''
Author: 千仞无锋
Date: 2022-03-17 00:03:55
LastEditors: 千仞无锋
LastEditTime: 2022-03-17 11:23:26
FilePath: \python_study_2022\3-17-selenium交互.py
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 仿真操作浏览器-自动化

s = Service(r"H:\study-notes\python_study_2022\msedgedriver-1153.exe")
browser = webdriver.Edge(service=s)

url = "http://www.baidu.com"
browser.get(url)

import time

time.sleep(2)

# 获取对象 文本框
input = browser.find_element_by_id("kw")
# 给文本框输入
input.send_keys("selenium")

time.sleep(2)

# 获取百度一下按钮
button = browser.find_element_by_id("su")

# 点击按钮
button.click()

time.sleep(2)

# 滑动页面
js_bottom = "document.documentElement.scrollTop=10000"
browser.execute_script(js_bottom)

time.sleep(2)

# 下一页
next_page = browser.find_element_by_xpath("//a[@class='n']")

# 点击按钮
next_page.click()

time.sleep(2)

# 回退上一页
browser.back()

time.sleep(2)

# 前进下一页
browser.forward()

time.sleep(10)

# 退出
browser.quit()

