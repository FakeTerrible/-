import json
from bs4 import BeautifulSoup
import requests

try:
    url = 'https://movie.douban.com/review/best/?start=0'
    headers = {
        "Host": "movie.douban.com",
        "Referer": "https://movie.douban.com/review/best/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    req = requests.get(url, headers=headers)
    req.raise_for_status()
    soup = BeautifulSoup(req.text, features="html.parser")
    father = soup.find('div', class_='review-list chart')
    items = father.findAll('div', class_='main review-item')
    for i in items:
        print("-------------------------------------------------------------------------------------")
        name = i.find('a', class_='name')
        print('作者：' + name.text)
        h2 = i.find('h2')
        print('标题：' + h2.text)
        id = i.find('div', class_='hidden')['id']
        url_obj = 'https://movie.douban.com/j/' + id.replace('_', '/')
        req1 = requests.get(url_obj, headers=headers)
        req1.raise_for_status()
        # print(req1.text)
        html = json.loads(req1.text)
        print(html['html'])
except requests.RequestException as e:
    print(e)