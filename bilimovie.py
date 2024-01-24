import json
import time
import requests

try:
    ts = str(int(time.time()))
    url = 'https://api.bilibili.com/pgc/season/rank/web/list?day=3&season_type=2&web_location=333.934&w_rid=a0d966d3c382d9201e75042690aa6fee&wts={}'.format(
        ts)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    req = requests.get(url, headers = header)
    req.raise_for_status()
    obj = json.loads(req.text)
    for i in obj['data']['list']:
        print(i['title'])
        print(i['url'])
except requests.RequestException as e:
    print(e)
