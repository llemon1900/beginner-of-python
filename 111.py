import requests
url = 'https://rbv01.ku6.com/wifi/o_1fs3tdmucn6dpklhtl19gj6qp'
response = requests.get(url)
with open('C:\\Users\\82754\\Desktop\\practice\\练习\\pic\\1.jpg','wb') as f:
    f.write(response.content)