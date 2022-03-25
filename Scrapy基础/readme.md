<!--
 * @Author: your name
 * @Date: 2022-03-23 14:29:20
 * @LastEditTime: 2022-03-25 14:37:02
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: \python_study_2022\3-23-scrapy四块皮.md
-->
# scrapy基础操作
 scrapy:提取结构性数据的框架(比如一堆li标签的)
## 1、首先得从cmd创建项目
 指令为： scrapy startproject mySpider_xxxxxxxx 不能有中文

## 2、到项目文件下进入一个文件夹

## 3、在spider文件夹下创建一个爬虫文件
 路径格式为：cd mySpider_xxxxxxxx\mySpider_xxxxxxxx\spiders
 指令：scrapy genspider 需要另取文件名 https://www.baidu.com
 有时在vscode终端中运行，会报错 就到文件夹下，cmd窗口中执行。

## 4、运行爬虫
 指令 ：scrapy crawl mySpider_xxxxxxxx

# 调试工具scrapy shell
是一个scrapy终端程序,可交互,未启动spiders情况下调试爬取代码.本意是用来测试提取数据的xpath和css表达式.
同时也是个正常Python终端.
### 安装ipython
pip安装
如果安装了IPython ,scrapy将用其代替标准Python终端.

## 执行
在cmd中运行 scrpay shell www.baidu.com 才会运行成功, 而,如果去Python终端,或者ipython终端运行这句指令,则报错.
但是,
如果想看到一些高亮,或者自动补全的,那么就要安装ipython.


有了第一句指令后

接下来可以执行 如 :
response.bady 二进制源码数据,
response.text 页面源码,
response.url 返回url地址,
response.status 返回状态码,

举栗:
a = response.xpath('//input[@id="su"]/@value')
a # 打印a
a.extract_first()  # 获取列表中第一个数据


