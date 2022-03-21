import requests
import execjs
import random
import time

"""
1.通过抓包获取翻译功能对应的JS文件
2.观察post数据携带的参数
3.寻找参数生成方法，改写js文件
4.利用execjs方法生成参数
5.构造请求头
6.发送请求获取响应
7.解析数据
"""

e = str(input('请输入要翻译的内容'))

class Youdao:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'Cookie': '_ntes_nnid=c8bad5f7477cefb4197d6a33f262003f,1605013411011; OUTFOX_SEARCH_USER_ID_NCOO=917528036.0494087; OUTFOX_SEARCH_USER_ID="-1826158656@10.108.160.19"; fanyi-ad-id=305110; fanyi-ad-closed=1; JSESSIONID=aaa_ZVtz-_Ae3hOiEdQ_x; ___rl__test__cookies=1647825659039',
            'Referer': 'https://fanyi.youdao.com/'
        }

        self.url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.proxies = {'http': 'http://47.92.234.75:80'}

    def get_params(self):
        node = execjs.get()
        ctx = node.compile(open(("有道翻译.txt"),encoding='utf-8').read())
        lts = str(int(time.time() * 1000))
        salt = lts + str(random.randint(0, 9))
        func_sign = f'getSign("{e}","{salt}")'

        sign = str(ctx.eval(func_sign))
        # string = "fanyideskweb" + i + salt + "Y2FYu%TNSbMCxc3t2u^XT"
        # m = hashlib.md5()
        # m.update(string.encode())
        # sign = m.hexdigest()

        print(lts,salt,sign)
        return lts,salt,sign


    def get_data(self,lts,salt,sign):
        data = {
        'i': e,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': lts,
        'bv': 'fdac15c78f51b91dabd0a15d9a1b10f5',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
        }


        response = requests.post(self.url,headers = self.headers,data=data,proxies = self.proxies)
        print(response.content.decode())

    def run(self):
        lts, salt, sign = self.get_params()
        self.get_data(lts, salt, sign)

youdao = Youdao()
youdao.run()