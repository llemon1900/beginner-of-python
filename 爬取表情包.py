import requests
import os
from lxml import etree
import csv

"""
构造请求头
发送请求，获取响应
提取名称、链接
创建文件夹，下载图片
"""

if not os.path.exists('表情包'):
    os.mkdir('表情包')

with open('biaoqingbao.csv', 'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name','link'])

class Biaoqingbao:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        # self.proxies = {
        #     'http': 'http://47.92.234.75:80'
        # }

    def get_data(self,url):
        response = requests.get(url,headers = self.headers).content.decode()
        return response

    def parse_data(self,response):
        html = etree.HTML(response)
        name_list = html.xpath('//*[@id="bqb"]/div[1]/div/a/@title')
        link_list = html.xpath('//*[@id="bqb"]/div[1]/div/a/img/@data-original')
        # print(link_list)
        # print(name_list)
        return name_list,link_list

    def save_data(self,name_list,link_list):
        for name in name_list:
            name_1 = name.replace('?','')
            i = name_list.index(name)
            link = link_list[i]
            j = link.rfind('.')
            houzhui = link[j::]
            img = requests.get(link,headers = self.headers).content
            with open('biaoqingbao.csv','a',newline='') as pic:
                writer = csv.writer(pic)
                writer.writerow([name,link])
            try:
                path = 'C:\\Users\\82754\\Desktop\\practice\\练习\\表情包\\' + name_1 + houzhui
                with open(path,'wb') as f:
                    f.write(img)
            except:
                pass

    def run(self):
        url = 'https://fabiaoqing.com/biaoqing'
        response = self.get_data(url)
        name_list, link_list = self.parse_data(response)
        self.save_data(name_list, link_list)


biaoqingbao = Biaoqingbao()
biaoqingbao.run()