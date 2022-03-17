'''
Author: 千仞无锋
Date: 2022-03-17 12:31:32
LastEditors: 千仞无锋
LastEditTime: 2022-03-17 17:02:35
FilePath: \python_study_2022\3-17-selenium-PhantomJS-无界面浏览器.py
'''
# phantomjs 和 chrome handless 前一个黄了。。。。哈哈哈哈
# 无界面浏览器：不显示UI界面的操作 不进行css和js渲染 省事

from selenium import webdriver
import time

# 仿真操作浏览器-自动化

path = 'H:\study-notes\python_study_2022\bin\phantomjs.exe'
# 报错了，因为最新的selenium版本没有这个方法
browser = webdriver.PhantomJS(executable_path=path)

url = "http://www.baidu.com"
browser.get(url)
# 拍个照
browser.save_screenshot('baidu.png')

time.sleep(2)

input = browser.find_element_by_id('kw')
input.send_keys(['python'])

time.sleep(2)

browser.save_screenshot('baidu_python.png')
