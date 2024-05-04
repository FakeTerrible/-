import json
import requests

try:
    url = 'https://so.toutiao.com/2/wap/search/extra/long_video/?query=%E7%94%B5%E8%A7%86%E5%89%A7&dvpf=pc&result_type=album_tag&count=200&offset=0&sort_type=year'
    req = requests.get(url)
    req.raise_for_status()
    req.encoding = 'utf-8'
    obj = json.loads(req.text)
    for i in obj['data']:
        info = i['album_group']
        actors = info['actor']
        title = info['title']
        area = info['area']
        year = info['year']
        director = info['director']
        summary = info['summary']
        print(title + ' ' + actors)
        print(director)
        print(area + ' ' + year)
        print(summary)
        print('--------------------------------------------------------------------------------------------')
except requests.RequestException as e:
    print(e)