'''
Author: your name
Date: 2022-02-23 15:21:34
LastEditTime: 2022-02-23 16:53:08
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \20220205Py学习\ajax的get-豆瓣前十页.py
'''
# 导入包，用来拼接data字典
import urllib.parse
# 导入包，用来请求数据
import urllib.request
# ajax 实现根据滑动一直加载
# 找接口：


# 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100:90&action=&start=40&limit=20'
# 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100:90&action=&start=60&limit=20'
# start是0起步，limit是每页几条数据
# page 1    2   3   4
# start 0   20  40  60
# 根据等差数列：start = （page-1）*20

# 需求：下载豆瓣电影前十页的数据

# 第一步：请求对象定制：（思考：这是个动态的url）用循环？
# 封装函数：


def create_request(page):
    # 难点：url每一页不同，如何动态替换里面的参数值
    base_url = 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100:90&action=&'
    # 利用设定一个字典来完成多参数修改拼接
    # 这里的data字典只是用来拼接的
    data = {
        'start': (page-1)*20,
        'limit': '20',
    }
    # 拼接
    data = urllib.parse.urlencode(data)
    new_url = base_url+data
    # print(new_url)
    headers = {
        'Cookie': ' ll="118378"; bid=rmuzZP9uilo; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1645585436%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DnsdCzK0ZvBDdu0ShhH-HLiceq-9awUnk6tPtZrNfPamMMBGDN3UdqFy3uzPP3tHH%26wd%3D%26eqid%3Dd4a69b4d000038f0000000066215a3dd%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1358641776.1645582330.1645582330.1645585436.2; __utmb=30149280.0.10.1645585436; __utmc=30149280; __utmz=30149280.1645585436.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1014032229.1645582330.1645582330.1645585436.2; __utmb=223695111.0.10.1645585436; __utmc=223695111; __utmz=223695111.1645585436.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_id.100001.4cf6=f74601e2726bc47f.1645582331.2.1645585492.1645582779.',
        'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    }
    # 模拟Ajax请求/get请求，参数里没有data，只有url和headers，post
    request = urllib.request.Request(url=new_url, headers=headers)
    return request  # 调用时找个变量接收一下就好


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content  # 调用时找个变量接收一下就好


def down_load(page, content):
    # 一个小技巧，多文件生成时：
    # 如果要和字符串拼接，+号两端要全部是字符串
    with open('douban_'+str(page)+'.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


# 这句是程序入口
if __name__ == '__main__':
    # 输入参数
    start_page = int(input('请输入起始页码'))  # 返回的是字符串类型，利用int（）变成整形数据
    end_page = int(input('请输入终止页码'))
    # 开始处理
    # 遍历一下
    for page in range(start_page, end_page+1):  # 注意左闭右开区间
        # print(page)
        # 每页都有自己的请求对象定制：
        request = create_request(page)  # request用来接收调用函数的返回值
        # 第二步：获取响应数据：
        content = get_content(request)
        # 第三步：下载数据：
        down_load(page, content)
