'''
Author: your name
Date: 2022-03-23 09:55:56
LastEditTime: 2022-03-23 14:28:34
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_study_2022\Chaojiying_Python\chaojiying_Python\chaojiying.py
'''
# coding:utf-8

import requests
from hashlib import md5


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """g
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php',
                          data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post(
            'http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


if __name__ == '__main__':
    # 用户中心>>软件ID 生成一个替换 96001
    chaojiying = Chaojiying_Client('fengge', '1042044920', '930564')
    # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    im = open(r'C:\Users\Feng-DevWork\Desktop\Python20220224爬虫\python_study_2022\Chaojiying_Python\chaojiying_Python\a.jpg', 'rb').read()
    # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    # print(chaojiying.PostPic(im, 1902))
    print(chaojiying.PostPic(im,1902).get('pic_str')+'老子充钱了!')
    # 无可用提分 没交钱不好使，，， 钞能力 啊 。。。
    if chaojiying.PostPic(im, 1902).get('pic_str') == '':
        print('哦吼,空值,说明调用成功,但是没交钱,哈哈哈哈')
