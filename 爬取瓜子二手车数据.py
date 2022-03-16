"""
1.构造请求头
2.分析pclist(xhr)url的生成规律（page不一样）
3.发送请求获取相应
4.解析数据
5.保存数据
"""

import requests
import re

class Guazi:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'referer': 'https://www.guazi.com/'
        }
        self.proxies = {'http':'http://47.92.234.75:80'}

    def get_data(self,params):
        url = 'https://mapi.guazi.com/car-source/carList/pcList'
        response = requests.get(url,headers = self.headers,proxies = self.proxies,params=params).content.decode()
        print(response)
        return response

    def parse_data(self,response):
        title_list = re.findall('"title":"(.*?)","puid":',response,re.S)
        price_list = re.findall('"buyOutPrice.*?"(.*?)",',response,re.S)
        print(title_list,price_list)



    def run(self):
        # for i in range(16):
            params = {
            'minor': 'bmw',
            'tag': '-1',
            'priceRange': '0, -1',
            'page': 1,
            'pageSize': '20',
            'city_filter': '12',
            'city': '12',
            'guazi_city': '12',
            'versionId': '0.0.0.0',
            'osv': 'Unknown',
            'platfromSource': 'wap',
            }
            response = self.get_data(params)
            self.parse_data(response)


guazi = Guazi()
guazi.run()