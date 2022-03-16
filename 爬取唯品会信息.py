"""
抓包分析发现是一个动态页面，ajax异步加载  然而xhr文件中没有数据  数据在js文件v2中
js文件需要使用get获取数据，url中包含商品代号数据   在js文件rank中找到了全部的商品代号
因此思路为：获取rank的响应，解析所有商品代号，将代号套入v2中获取数据
1.构造请求头
2.发送请求，获取rank的响应，提取商品代号
3.发送请求，获取v2响应，提取商品信息
4.保存信息
"""

import time

import requests

import re

now = int(time.time() * 1000)

class Weipinhui:
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            "referer": 'https://category.vip.com/'
        }
        self.proxies = {'http':'http://47.92.234.75:80'}

    def rank_data(self):

        params = {
        'callback': 'getMerchandiseIds',
        'app_name': 'shop_pc',
        'app_version': '4.0',
        'warehouse': 'VIP_NH',
        'fdc_area_id': '104104101',
        'client': 'pc',
        'mobile_platform': '1',
        'province_id': '104104',
        'api_key': '70f71280d5d547b2a7bb370a529aeea1',
        'mars_cid': '1647241871608_a587dd1fc1f0d16c319a6cdc20a9eb1c',
        'wap_consumer': 'a',
        'standby_id': 'nature',
        'keyword': 'pad',
        'sort': '0',
        'pageOffset': '0',
        'channelId': '1',
        'gPlatform': 'PC',
        'batchSize': '120',
        '_':now
        }

        url_rank = f'https://mapi.vip.com/vips-mobile/rest/shopping/pc/search/product/rank?callback=getMerchandiseIds&app_name=shop_pc&app_version=4.0&warehouse=VIP_NH&fdc_area_id=104104101&client=pc&mobile_platform=1&province_id=104104&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1647241871608_a587dd1fc1f0d16c319a6cdc20a9eb1c&wap_consumer=a&standby_id=nature&keyword=pad&lv3CatIds=&lv2CatIds=&lv1CatIds=&brandStoreSns=&props=&priceMin=&priceMax=&vipService=&sort=0&pageOffset=0&channelId=1&gPlatform=PC&batchSize=120&_={now}'
        response = requests.get(url_rank,headers = self.headers,proxies = self.proxies,params=params)
        # print(response.text)
        ids = re.findall('"pid":"(\d+)"',response.text,re.S)
        ids_1 = ids[:50]
        ids_2 = ids[51:100]
        ids_3 = ids[101:120]
        IDS_1 = ','.join(ids_1)
        IDS_2 = ','.join(ids_2)
        IDS_3 = ','.join(ids_3)
        return  IDS_1,IDS_2,IDS_3

    def v2_data(self,IDS_1,IDS_2,IDS_3):
        params_1 = {
        'callback': 'getMerchandiseDroplets1',
        'app_name': 'shop_pc',
        'app_version': '4.0',
        'warehouse': 'VIP_NH',
        'fdc_area_id': '104104101',
        'client': 'pc',
        'mobile_platform': '1',
        'province_id': '104104',
        'api_key': '70f71280d5d547b2a7bb370a529aeea1',
        'mars_cid': '1647241871608_a587dd1fc1f0d16c319a6cdc20a9eb1c',
        'wap_consumer': 'a',
        'productIds':IDS_1,
        'scene': 'search',
        'standby_id':'nature',
        'extParams': '{"stdSizeVids": "", "preheatTipsVer": "3", "couponVer": "v2", "exclusivePrice": "1","iconSpec": "2x", "ic2label": 1}',
        '_':now
        }

        params_2 = {
            'callback': 'getMerchandiseDroplets1',
            'app_name': 'shop_pc',
            'app_version': '4.0',
            'warehouse': 'VIP_NH',
            'fdc_area_id': '104104101',
            'client': 'pc',
            'mobile_platform': '1',
            'province_id': '104104',
            'api_key': '70f71280d5d547b2a7bb370a529aeea1',
            'mars_cid': '1647241871608_a587dd1fc1f0d16c319a6cdc20a9eb1c',
            'wap_consumer': 'a',
            'productIds': IDS_2,
            'scene': 'search',
            'standby_id': 'nature',
            'extParams': '{"stdSizeVids": "", "preheatTipsVer": "3", "couponVer": "v2", "exclusivePrice": "1","iconSpec": "2x", "ic2label": 1}',
            '_': now
        }

        params_3 = {
            'callback': 'getMerchandiseDroplets1',
            'app_name': 'shop_pc',
            'app_version': '4.0',
            'warehouse': 'VIP_NH',
            'fdc_area_id': '104104101',
            'client': 'pc',
            'mobile_platform': '1',
            'province_id': '104104',
            'api_key': '70f71280d5d547b2a7bb370a529aeea1',
            'mars_cid': '1647241871608_a587dd1fc1f0d16c319a6cdc20a9eb1c',
            'wap_consumer': 'a',
            'productIds': IDS_3,
            'scene': 'search',
            'standby_id': 'nature',
            'extParams': '{"stdSizeVids": "", "preheatTipsVer": "3", "couponVer": "v2", "exclusivePrice": "1","iconSpec": "2x", "ic2label": 1}',
            '_': now
        }

        response_1 = requests.get('https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/module/list/v2',headers =self.headers,params=params_1,proxies =self.proxies  )
        response_2 = requests.get('https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/module/list/v2',headers =self.headers,params=params_2,proxies =self.proxies  )
        response_3 = requests.get('https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/module/list/v2',headers =self.headers,params=params_3,proxies =self.proxies  )

        title_1 = re.findall('"title":"(.*?)","brandShowName"', response_1.text, re.S)
        title_2 = re.findall('"title":"(.*?)","brandShowName"', response_2.text, re.S)
        title_3 = re.findall('"title":"(.*?)","brandShowName"', response_3.text, re.S)
        # print(response_1.content.decode())
        print(title_1)
        print('\n')
        print(title_2)
        print('\n')
        print(title_3)

    def run(self):
        IDS_1,IDS_2,IDS_3 = self.rank_data()
        self.v2_data(IDS_1,IDS_2,IDS_3)


weipinhui = Weipinhui()
weipinhui.run()