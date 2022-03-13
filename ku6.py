import requests
from jsonpath import jsonpath
import csv
import json

class Ku6:
    """
    1.构造请求头（UA、代理）
    2.发送请求，获取响应
    3.从响应中提取数据

    4.写入excel,图片保存进入文件夹
    """

    with open('ku6.csv','w',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name','video_link','pic_link'])

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        self.proxies = {'http':'http://47.92.234.75:80'}

    #构造请求  发送请求获取响应
    def get_data(self,url):
        response = requests.get(url,headers = self.headers,proxies = self.proxies).content
        response_dict = json.loads(response)
        return response_dict

    #提取数据
    def parse_data(self,response_dict):
        name_list = jsonpath(response_dict,'$..title')
        video_list = jsonpath(response_dict,'$..picPath')
        pic_list = jsonpath(response_dict,'$..playUrl')
        return name_list,video_list,pic_list

    def save_data(self,name_list,video_list,pic_list,num):
        for name in name_list:
            i = name_list.index(name)
            video_link = video_list[i]
            pic_link = pic_list[i]
            with open('ku6.csv','a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow([name,video_link,pic_link])
            response = requests.get(pic_link)
            path = 'C:\\Users\\82754\\Desktop\\practice\\练习\\pic\\'+ str(num) + '-' +str(i)+'.jpg'
            with open(path,'wb',) as f:
                f.write(response.content)

    def run(self):
        for num in range(16):
            url = 'https://www.ku6.com/video/feed?pageNo=' + str(num) + '&pageSize=40&subjectId=70'
            response_dict = self.get_data(url)
            name_list,video_list,pic_list = self.parse_data(response_dict)
            self.save_data(name_list,video_list,pic_list,num)


if __name__ == '__main__':
    ku6 = Ku6()
    ku6.run()