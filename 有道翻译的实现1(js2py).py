import time
import requests
import hashlib
import random
from jsonpath import jsonpath
import json
import js2py

"""
1.请求头
    1.url
    2.headers
    3.form表单
2.发送请求获取相应
3.提取数据
"""

#1.请求头
url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Cookie':'_ntes_nnid=c8bad5f7477cefb4197d6a33f262003f,1605013411011; OUTFOX_SEARCH_USER_ID_NCOO=917528036.0494087; OUTFOX_SEARCH_USER_ID="-1826158656@10.108.160.19"; JSESSIONID=aaab6rdzrJmIGhYq7fg6x; ___rl__test__cookies=1642927372587',
    'Referer': 'https://fanyi.youdao.com/'
}

e = str(input('请输入'))

# r = str(int(time.time() * 1000))
# i = r + str(random.randint(0,9))
# m = hashlib.md5()
# string = ("fanyideskweb" + e + i + "Y2FYu%TNSbMCxc3t2u^XT")
# m.update(string.encode())
# sign = m.hexdigest()
# lts = r

context = js2py.EvalJs     #创建js环境
fanyi_js = requests.get('https://shared.ydstatic.com/fanyi/newweb/v1.1.8/scripts/newweb/fanyi.min.js',headers=headers).content.decode()
context.execute(fanyi_js)




"""
t = n.md5(navigator.appVersion)
          , r = "" + (new Date).getTime()
          , i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "Y2FYu%TNSbMCxc3t2u^XT")
"""





form_data = {
'i': e,
'from': 'AUTO',
'to': 'AUTO',
'smartresult':'dict',
'client': 'fanyideskweb',
'salt': i,
'sign': sign,
'lts': lts,
'bv': 'fdac15c78f51b91dabd0a15d9a1b10f5',
'doctype': 'json',
'version': '2.1',
'keyfrom': 'fanyi.web',
'action': 'FY_BY_REALTlME'
}

response = requests.post(url,headers=headers,data=form_data).content.decode()
# print(response)
response_1 = json.loads(response)

translation = jsonpath(response_1,'$..tgt')
print(translation[0])