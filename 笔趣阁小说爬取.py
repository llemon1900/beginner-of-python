import requests
from lxml import etree
import json

"""
1.构造请求头
2.获取目录页数据（目录、各章链接）
3.分别进入每一个章节，获取正文数据
4.保存数据
"""

url = 'https://www.xbiquge.la/'

class Xianni:
    def __init__(self):
        self.headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

        self.proxies = {'http':'http://47.92.234.75:80'}

    def cata_data(self,url_1):
        response_1 = requests.get(url_1,headers = self.headers,proxies = self.proxies).content
        html = etree.HTML(response_1)
        chapter_list = html.xpath('//*[@id="list"]/dl/dd/a/text()')
        link_list = html.xpath('//*[@id="list"]/dl/dd/a/@href')
        # with open('仙逆.txt','w',encoding='gbk')as f:
        #     for chapter in chapter_list:
        #         f.write(chapter+'\n')
        return link_list

    def content_data(self,link_list):
        for link in link_list:
            response_2 = requests.get(url+link,headers = self.headers,proxies = self.proxies).content
            heml = etree.HTML(response_2)
            name = heml.xpath('//*[@class="bookname"]/h1/text()')[0]
            text_list = heml.xpath('//*[@id="content"]/text()')
            print(text_list)
            with open('仙逆.txt','a',encoding='utf-8')as f:
                f.write(name+'\n')
                for text in text_list:
                    f.write(text+'\n')

    def run(self):
        url_1 = url+'/6/6819/index.html'
        link_list = self.cata_data(url_1)
        self.content_data(link_list)

xianni = Xianni()
xianni.run()



