import urllib.request
import urllib.error
import urllib.parse
from calendar import c
from urllib import request


url = 'https://www.baidu.com/'
headres = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    # 'Cookie': '',
}

try:
    request = urllib.request.Request(url=url, headers=headres)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    with open('test.html', 'w', encoding='utf-8') as f:
        f.write(content)
        print('下载成功')
except urllib.error.URLError as e:
    print(e.reason)
    print('别瞅了,404啦')
except urllib.error.HTTPError as e:
    print(e.reason)
    print('我都说了,别瞅了,404啦')

