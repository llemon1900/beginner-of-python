import requests
import execjs

url = 'https://mp.weixin.qq.com/cgi-bin/bizlogin?action=startlogin'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'referer': 'https://mp.weixin.qq.com/'
}

node = execjs.get()
ctx = node.compile(open('C:\\Users\\82754\\Desktop\\practice\\练习\\get_pwd js.txt',encoding='utf-8').read())

password = 'loukailun'
func = f'get_pwd("{password}")'
pwd = ctx.eval(func)

print(pwd)

data = {
'username': '23@qq.com',
'pwd':pwd,
'f': 'json',
'userlang': 'zh_CN',
'lang': 'zh_CN',
'ajax': '1',
}

# response = requests.post(url,headers = headers,data=data)
# print(response.content.decode())
