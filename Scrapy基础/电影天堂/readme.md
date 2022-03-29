<!--
 * @Author: your name
 * @Date: 2022-03-29 10:02:51
 * @LastEditTime: 2022-03-29 10:17:47
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: \python_study_2022\Scrapy基础\电影天堂\readme.md
-->
<!-- 电影天堂 -->
# 需求与业务逻辑
## 业务逻辑:
    爬取某页面的电影词条,并且点击词条,获取那一页的图片数据.
    要第一页的名字，和相应第二页的图片
## 操作基础:
### scrapy基础操作
 scrapy:提取结构性数据的框架(比如一堆li标签的)
#### 2、到项目文件下进入一个文件夹
#### 3、在spider文件夹下创建一个爬虫文件
 路径格式为：cd mySpider_xxxxxxxx\mySpider_xxxxxxxx\spiders
 指令：scrapy genspider 需要另取文件名 https://www.baidu.com
 有时在vscode终端中运行，会报错 就到文件夹下，cmd窗口中执行。
#### 4、运行爬虫
 指令 ：scrapy crawl mySpider_xxxxxxxx