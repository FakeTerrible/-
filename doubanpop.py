import json
import requests

try:
    url = 'https://m.douban.com/rexxar/api/v2/tv/recommend?refresh=0&start=0&count=20&selected_categories=%7B%7D&uncollect=false&tags=2024'
    headers = {
        "Host": "m.douban.com",
        "Origin": "https://movie.douban.com",
        "Referer": "https://movie.douban.com/tv/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    req = requests.get(url, headers=headers)
    req.raise_for_status()
    req.encoding = 'utf-8'
    obj = json.loads(req.text)
    for i in obj['items']:
        print("|++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")
        print("|+" + i['title'])
        print("|+" + i['card_subtitle'])
        print("|+" + "https://im1907.top/?jx=" + i['title'])
except requests.RequestException as e:
    print(e)