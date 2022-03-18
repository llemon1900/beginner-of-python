from selenium import webdriver
import time
from lxml import etree
import re
import requests
import os

driver = webdriver.Chrome()

url = 'https://www.douyin.com/user/MS4wLjABAAAA8Nl-RLXjSF0kleaBbiP5bkEtuck5xzhr5mFCL_ybKTBv6NGM_wDbOS-Q8m5hsLAh'

driver.get(url)
driver.maximize_window()

js = 'window.scrollTo(0,100000)'
#因为不会js语法  所以只能先这么写了  下去再补一下js语法
driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)
# driver.execute_script(js)
# time.sleep(3)

driver.execute_script(js)


response = driver.page_source
# print(response)

html = etree.HTML(response)

href_list = html.xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div[1]/div[2]/ul/li/a/@href')
# print(href_list)

if not os.path.exists('抖音视频'):
    os.mkdir('抖音视频')

for href in href_list:
    i = href_list.index(href)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',

            'cookie': 'douyin.com; __ac_referer=__ac_blank; ttwid=1%7CUqE9Az5SQzwuJbaIeb-x9mTe9dbnwWQioS6uL3jXVts%7C1647504791%7C6dc686fe96ea19e0f99d4c5f48df64004af89630796119ecba710eadd577a89b; ttcid=1d1539cdb2a94560baa8b2c205aaf05036; MONITOR_WEB_ID=2ef2072b-517a-43d9-9bb7-9b5f2402b694; MONITOR_DEVICE_ID=c4e94b29-57b8-4a96-9e28-0bd04552a264; _tea_utm_cache_6383=undefined; passport_csrf_token=0c0d1aeb5b7d8d5836ab88cf975ed797; passport_csrf_token_default=0c0d1aeb5b7d8d5836ab88cf975ed797; _tea_utm_cache_1300=undefined; MONITOR_WEB_ID=3bfe5bc7-ff7c-48ab-9cee-a9167516e6b1; THEME_STAY_TIME=299502; IS_HIDE_THEME_CHANGE=1; _tea_utm_cache_2285=undefined; pwa_guide_count=3; odin_tt=fc981533df64c85832951ad3d3b1db22cf51590901654b17b11d72110fb2d2aea3cea3522ff38469e8346529978dde1e6d68a31494f9de7a6296112d4b9ef98b; _tea_utm_cache_2018=undefined; strategyABtestKey=1647566853.391; AB_LOGIN_GUIDE_TIMESTAMP=1647566853025; __ac_signature=_02B4Z6wo00f01FgHR8wAAIDA2AW9jZd5GgxYJ0NAAHQ5YtWLS-TqImdMcvgDk8gUue2P-w7hvwl8m5UxsIe.r6T0k.5GikI.ZmDsEgtcpfz0jflGXnXnmzAa5vyESORZTJyCsb2cLr6mubpYa1; douyin.com; msToken=Sq0zfOvbYSp1vIO8qCN_HmNMhNHJHzyLarASw8K7_ugjxsVmE1HmZOX15P6V4hmXksUBQ-nM-eqpFt5PQ4VXh_77hvZUPHVj3YE2zYQElUYeNUVi4pEBYA==; __ac_nonce=06233ef43004ef0508444; s_v_web_id=verify_1e4da7ecff5a1f9001ea71cd0f402c48; msToken=POITWJGXVAkbqYM4DUfNC79uFbiWNjgYb7QLkaPYUjJjcGhj3prkdPzu887y8FEOO9fVfFczh4n6U2idsj-TsUjeysV_4FE--tdXKqL_Dae8BJxE3FN9Xek=; tt_scid=J05pEZL5YOCFmluwpxjJxY84nk.B4c8K796k3nN04wr-ONY2m0ufNAybAUnZaN2A34bd; home_can_add_dy_2_desktop=0',

    'referer': 'https://www.douyin.com/video/7075544392555040032?previous_page=others_homepage&modeFrom=userPost&cursor=0&count=10&secUid=MS4wLjABAAAA8Nl-RLXjSF0kleaBbiP5bkEtuck5xzhr5mFCL_ybKTBv6NGM_wDbOS-Q8m5hsLAh&enter_method=post'}

    response = requests.get(url='https:'+href,headers=headers)
    # print(response.text)
    # print()
    # print()
    # print()

    src = re.findall('src(.*?)vr%3D%22%7D%2C%7B%22',response.text,re.S)[1]
    # src_ = re.findall('src(.*?)vr%3D%22%7D%2C%7B%22',response.text,re.S)
    # print(src)

    video_src = requests.utils.unquote(src)[3::]
    # print(video_src)

    headers_1 = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',

               'Referer': 'https://www.douyin.com/'}


    real_url = 'https:'+video_src
    response_1 = requests.get(real_url,headers=headers)
    with open(f'C:\\Users\\82754\\Desktop\\practice\\练习\\抖音视频\\{i}.mp4','wb')as f:
        f.write(response_1.content)
