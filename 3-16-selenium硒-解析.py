'''
Author: 千仞无锋
Date: 2022-03-16 17:40:18
LastEditors: 千仞无锋
LastEditTime: 2022-03-16 19:56:58
FilePath: \python_study_2022\3-16-selenium硒-解析.py
'''
# selenium用于web程序测试的工具
# 测试直接运行于浏览器中，就像真正的用户再操作一样(不是模拟请求，而是真正的操作)
# 支持无界面浏览器操作
# 支持通过各种dirver驱动真实的浏览器完成测试

# 导入
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import urllib.request

# 爬下京东首页，秒杀数据
url1 = 'https://www.jd.com/'
# 访问
response1 = urllib.request.urlopen(url1)
content1 = response1.read().decode('utf-8')
# print(content1) # 打印网页内容
# 没有获取到关键数据 因为是模拟浏览器

# 用selenium模拟浏览器访问
# 创建浏览器操作对象(路径填入)
# path = 'msedgedriver-1153.exe'
s = Service(r"H:\study-notes\python_study_2022\msedgedriver-1153.exe")
# 参数 executable_path可执行路径 为 刚才的 path
# browser = webdriver.Edge(path)
driver = webdriver.Edge(service=s)
# 驱动浏览器访问网页
url = 'https://www.jd.com/'
driver.get(url)
# 弹出的窗口 显示 受到自动测试软件的控制

content = driver.page_source
print(content)
