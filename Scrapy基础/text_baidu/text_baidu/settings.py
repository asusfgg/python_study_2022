'''
Author: your name
Date: 2022-03-24 09:32:32
LastEditTime: 2022-03-24 09:58:22
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\text_baidu\text_baidu\settings.py
'''
# Scrapy settings for text_baidu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:

# text_baidu项目的scrapy设置
# 为简单起见，此文件仅包含重要的设置或常用。 您可以查阅文档找到更多设置：
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'text_baidu'

SPIDER_MODULES = ['text_baidu.spiders']
NEWSPIDER_MODULE = 'text_baidu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 通过在用户代理上识别您自己（和您的网站）来负责任地爬行
#USER_AGENT = 'text_baidu (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 遵守 robots.txt 规则
ROBOTSTXT_OBEY = False

#
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# 配置 Scrapy 执行的最大并发请求数（默认值：16）
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 另请参阅自动油门设置和文档
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# 下载延迟设置将仅支持以下之一：
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 禁用 cookie（默认启用）
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# 禁用 Telnet 控制台（默认启用）
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'text_baidu.middlewares.TextBaiduSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'text_baidu.middlewares.TextBaiduDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'text_baidu.pipelines.TextBaiduPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
