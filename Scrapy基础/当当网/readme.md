<!--
 * @Author: your name
 * @Date: 2022-03-25 14:46:22
 * @LastEditTime: 2022-03-25 15:22:52
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: \python_study_2022\Scrapy基础\当当网\readme.md
-->
# <练习任务>
## 需求:
爬取一百页数据.
## 学习目标:
1 yield函数 //
2 管道封装 //
3 多管道下载 //
4 多页数据下载 //
### 框架:
scrapy
### 逻辑:
note: 有点难

#### 管道 pipeline 
用来下载数据的
#### item
定义数据结构的

#### 思路
去定义item数据结构，在item文件中 \
找xpath路径 \
src = //ul[@id="component_59"]/li//img/@src \
ale = //ul[@id="component_59"]/li//img/@alt \
price = //ul[@id="component_59"]/li//p[@class="price"]/span[1]/text() \
一页60个，一百页6000个 ， 好家伙 \
规律： \
以上仨 共享li标签，都是li的子标签 \