<!--
 * @Author: your name
 * @Date: 2022-03-30 16:08:12
 * @LastEditTime: 2022-04-07 10:39:00
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: \python_study_2022\Scrapy基础\3-30-CrawlSpider\readme.md
-->
# crawl spider

## 数据库基础

### mysql

    下载: 官网
    root key : 1042044920

### pymysql

    下载: pip
    使用:
        pymsql.connect(host,port,password,db,charset)
        conn.cursor()
        cursor.execute()

### crawl spider

    继承 scrapy.spider
    链接提取,再提交.
    举个栗子:
        读书网,对页码右键,检查,所有a标签,中的href值,都是类似的.
        把当前页面所有符合规则的链接提取出来,解析
    链接提取器:
        scrapy.linkextrators.LinkExtractor()
        ()
        allow = ()正则用法
            \d+ d表示数字 +表示一到多个数字
            举栗:
                scrapy shell下
                link = LinkExtractor(allow = r'/book/1001_\d+\.html')
        <!-- deny = () -->
        <!-- allow_domains = () -->
        <!-- deny_domains = () -->
        restrict_xpaths = ()xpath用法
            举栗:

        restrict_css = ()
    simulation:
        正则:links1 = LinkEctractor(allow=r'list_23_\d+\.html')
        xpath:link2 = LinkEctractor(restrict_xpaths=r'//div[@class="x"]')
        css:link3 = LinkEctractor(restrict_css='.x')
    链接提取:
        link.extract_lists(response)

### 步骤

###
