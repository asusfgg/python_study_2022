<!--
 * @Author: your name
 * @Date: 2022-03-23 14:29:20
 * @LastEditTime: 2022-03-25 13:52:39
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: \python_study_2022\3-23-scrapy四块皮.md
-->
# scrapy
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
是一个scrapy终端程序,可交互,未启动spiders情况下调试爬取代码.本意是用来测试提取数据的代码.
同时也是个正常Python终端.