"""
1.构造请求头
2.发送请求获取响应
3.对数据进行解析
4.保存数据
"""

import requests
from lxml import etree

class Jingdong():
    #1.构造请求头
    def __init__(self):
        self.url = 'https://search.jd.com/Search?keyword=%E5%8E%86%E5%8F%B2&wq=%E5%8E%86%E5%8F%B2&shop=1&click=1'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'referer': 'https://book.jd.com/'
        }

    #2.发送请求获取响应
    def get_data(self):
        response = requests.get(self.url,headers =self.headers )
        return response.content.decode()

    #3.进行数据解析
    def parse_data(self,data):
        html = etree.HTML(data)
        book_name = html.xpath('//*[@id="J_goodsList"]/ul/li/div/div[3]/a/em/text()[1]')
        book_price = html.xpath('//*[@id="J_goodsList"]/ul/li/div/div[2]/strong/i/text()')
        return book_name,book_price

    #4.保存数据
    def save_data(self,book_name,book_price):
        for book in book_name:
            i = book_name.index(book)
            with open('jingdong.doc','a+') as f:
                f.write(book +'\n')
                f.write(book_price[i] + '\n')
                f.write('\n')


    def run(self):
        data = self.get_data()
        book_name,book_price = self.parse_data(data)
        self.save_data(book_name,book_price)


jingdong = Jingdong()
jingdong.run()