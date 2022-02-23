'''
Author: 千仞无锋
Date: 2022-02-14 23:57:35
LastEditors: 千仞无锋
LastEditTime: 2022-02-15 00:47:48
FilePath: \20220205Py学习\下载.py
'''
import urllib.request

# 下载网页
url_page = 'https://www.vipglobal.hk/detail-1710620765-6918544641033750493.html'
# url路径，filename文件名
urllib.request.urlretrieve(url_page, 'vipglobal.html')

# 下载图片
url_img = 'https://a.vpimg2.com/upload/merchandise/pdcvis/2020/11/24/22/570d867b-215d-4e90-9b13-39e38e0f6203.jpg'

urllib.request.urlretrieve(url=url_img,filename='DW.jpg')

# 下载视频
url_video = 'https://1251962819.vod2.myqcloud.com/9fded1abvodgzp1251962819/d02d7500387702295358865355/2uppeb7THCEA.mp4'
urllib.request.urlretrieve(url=url_video,filename='DW.MP4')


