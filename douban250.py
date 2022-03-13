import requests
from lxml import etree
import csv

class Douban250:
    """
    1.构造请求头（UA、代理）
    2.发送请求，获取响应
    3.从响应中提取数据
        提取下一页url
        如果xpath存在则循环  不存在则返回None
    4.写入excel
    """
    with open('D:\douban250.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['movie', 'director', 'score'])

    def __init__(self):
        self.url = 'https://movie.douban.com/top250'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        self.proxies = {'http':'http://47.92.234.75:80'}

    #构造请求  发送请求获取响应
    def get_data(self,url):
        response = requests.get(url,headers = self.headers,proxies = self.proxies).content.decode()
        # print(response)
        return response

    #提取数据
    def parse_data(self,response):
        html = etree.HTML(response)
        movie_list = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
        director_list = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[1]/text()[1]')
        score_list = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]/text()')
        # print(movie_list,director_list,score_list)
        try:
            next_url = self.url + html.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href')[0]
        except:
            next_url = None
        # print(next_url)
        return movie_list,director_list,score_list,next_url

    def save_data(self,movie_list,director_list,score_list):
        # print(type(movie_list[0]))
        for movie in movie_list:
            i = movie_list.index(movie)
            director = director_list[i]
            score = score_list[i]
            # with open('D:\douban250.csv', 'a', newline='',encoding='utf-8') as f:
            #     writer = csv.writer(f)
            #     writer.writerow(['movie', 'director', 'score'])
            with open('D:\douban250.csv', 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([movie,director,score])

    def run(self):
        next_url = self.url
        while True:
            response = self.get_data(next_url)
            movie_list,director_list,score_list,next_url = self.parse_data(response)
            self.save_data(movie_list,director_list,score_list)

            if next_url == None:
                break

if __name__ == '__main__':
    douban = Douban250()
    douban.run()