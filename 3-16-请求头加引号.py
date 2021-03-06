'''
Author: 千仞无锋
Date: 2022-03-16 17:00:16
LastEditors: 千仞无锋
LastEditTime: 2022-03-16 17:07:27
FilePath: \python_study_2022\请求头加引号.py
'''
import re

request_headers = '''
    :authority: www.starbucks.com
    :method: GET
    :path: /menu
    :scheme: https
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    accept-encoding: gzip, deflate, br
    accept-language: zh-CN,zh;q=0.9
    cache-control: max-age=0
    cookie: AKA_A2=A; ux_exp_id=4f4ea721-d38a-4832-8933-570a99aad260; _gcl_au=1.1.2137732422.1647402354; _gid=GA1.2.986295488.1647402354; tiWQK2tY=A9lP1ZB_AQAAq4B9twxjhYfI2NDXmzQqCmJSm-NZpyoc7n29iNUKO1TTtgd2AWdhycKucpMswH8AAEB3AAAAAA|1|0|5a8d5a0209724b122a1aa1239a5c38e87a72144b; notice_behavior=implied,us; notice_gdpr_prefs=0,1,2:; notice_preferences=2:; cmapi_gtm_bl=; cmapi_cookie_privacy=permit 1,2,3; _ga_VMTHZW7WSM=GS1.1.1647402354.1.1.1647402374.0; _uetsid=a122e1f0a4db11ec82d83b8dd7fcde7c; _uetvid=a1233330a4db11ec9cb16794a05b063e; _ga=GA1.2.1682345083.1647402354; _gat_mpgaTracker1=1; RT="z=1&dm=www.starbucks.com&si=7833b58f-3397-4c5c-ae0e-614623b04466&ss=l0t0tqwz&sl=2&tt=4w0&rl=1&ld=1iyj&r=48wpdy16&ul=1iyj"
    dnt: 1
    referer: https://www.starbucks.com/menu
    sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"
    sec-ch-ua-mobile: ?0
    sec-ch-ua-platform: "Windows"
    sec-fetch-dest: document
    sec-fetch-mode: navigate
    sec-fetch-site: same-origin
    sec-fetch-user: ?1
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36
    '''

pattern = '^(.*?):[\s]*(.*?)$'
headers = ""
for line in request_headers.splitlines():
    headers += (re.sub(pattern, '\'\\1\': \'\\2\',', line)) + '\n'
print(headers)

with open('headers.json', 'w', encoding='utf-8') as f:
    f.write(headers)
    f.close()