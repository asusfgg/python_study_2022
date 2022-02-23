'''
Author: your name
Date: 2022-02-22 15:11:33
LastEditTime: 2022-02-23 09:40:07
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \20220205Py学习\post详细翻译接口.py
'''
import json
import urllib.request
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers = {'Accept': ' */*',
           #    接受的编码格式（一个大坑）：给丫的注释掉
           #    'Accept-Encoding': ' gzip, deflate, br',
           #    剩下的按照要求给出就好
           #    'Accept-Language': ' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
           #    'Connection': ' keep-alive',
           #    'Content-Length': ' 134',
           #    'Content-Type': ' application/x-www-form-urlencoded; charset=UTF-8',
           'Cookie': 'PSTM=1645405196; BAIDUID=6D9BE8D5B07A0294167DB81F68985D00:FG=1; __yjs_duid=1_606229eac07d274704be80afd0de83481645413753352; BIDUPSID=902303ED2CF7E16CAC667F47846B3FB9; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_10_0_2=1; H_PS_PSSID=35106_31660_35762_35488_35865_34584_35491_35872_35931_35956_35320_26350_35943; BA_HECTOR=al8k24a0ak048lakm61h192pk0r; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1645511828,1645511923,1645513531,1645513910; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1645513910; ab_sr=1.0.1_ODIyNTRjOTI5NmMwZWFlMGRiYmVmMWY2NGQ5MjY1YjdmMTg0MjlkY2IzNWM5YzY5MTRkM2M3ZTAzMDJmZWM5OGEwNGRiYjBhODk2ZTAxMWEzN2U4OWE0NGI4N2UxMDk3NDAzZDI0NmRiZjVjN2U3MmFmN2ZmZTc2ZDA2ODFkOTlhN2IyOTA0ZDI3NGNlYzUzZWQ3ODVlNTk2MDA0NTAzOQ==',
           #    'DNT': ' 1',
           #    'Host': ' fanyi.baidu.com',
           #    'Origin: https': '//fanyi.baidu.com',
           #    'Referer: https': '//fanyi.baidu.com/',
           #    'sec-ch-ua': ' " Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
           #    'sec-ch-ua-mobile': ' ?0',
           #    'sec-ch-ua-platform': ' "Windows"',
           #    'Sec-Fetch-Dest': ' empty',
           #    'Sec-Fetch-Mode': ' cors',
           #    'Sec-Fetch-Site': ' same-origin',
           'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
           #    'X-Requested-With': ' XMLHttpRequest',
           }
data = {
    # 来源为 payload标签页面
    'from': 'en',
    'to': 'zh',
    'query': 'fix',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '110152.347513',
    'token': 'ec8deb72e475a9a3254298718294376e',
    'domain': 'common',
}
data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)
# 有个报错信息：无效的头名称b'Cookie:Pstm=1645405196；Baiduid=6D9Be8D5B07A0294167Db81F68985D00'
# 检查cookie信息格式和内容
content = response.read().decode('utf-8')
print(content)
obj = json.loads(content)
print(obj)
