import requests
import json
import re
import os
import time


class LOL:
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            "referer": 'https://lol.qq.com/'
        }
        self.proxies = {'http':'http://47.92.234.75:80'}

    def get_id(self):
        response_1 = requests.get('https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?v=33',headers = self.headers,proxies = self.proxies).text.encode('utf-8').decode('unicode_escape')
        response = str(json.loads(response_1,strict =False))
        # print(response)
        heroid_list = re.findall('\'heroId\': \'(.*?)\', \'name\'',response,re.S)
        name_list = re.findall('\'name\': \'(.*?)\', \'alias\'',response,re.S)
        print(heroid_list,name_list)
        return heroid_list,name_list

    def get_picture(self,heroid_list,name_list):
        if not os.path.exists('C:\\Users\\82754\\Desktop\\practice\\练习\\英雄联盟壁纸'):
            os.mkdir('C:\\Users\\82754\\Desktop\\practice\\练习\\英雄联盟壁纸')
        for name in name_list:
            os.mkdir(f'C:\\Users\\82754\\Desktop\\practice\\练习\\英雄联盟壁纸\\{name}')
            j = name_list.index(name)
            for i in range(0,30):
                n = str(i).zfill(3)
                url = 'https://game.gtimg.cn/images/lol/act/img/skin/big'+str(heroid_list[j])+str(n)+'.jpg'
                response = requests.get(url,headers = self.headers,proxies = self.proxies,timeout = 2)
                if response.status_code ==200:
                    try:
                        with open(f'C:\\Users\\82754\\Desktop\\practice\\练习\\英雄联盟壁纸\\{name}\\{i}.jpg','wb') as f:
                            f.write(response.content)
                    except:
                        print('出现问题')


    def run(self):
        heroid_list,name_list = self.get_id()
        self.get_picture(heroid_list,name_list)

lol = LOL()
lol.run()