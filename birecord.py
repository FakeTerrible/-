import json
import requests

try:
    url = 'https://api.bilibili.com/x/member/web/login/log?jsonp=jsonp&web_location=333.33'
    headers = {
        # 自己账号的cookie
        "Cookie":"*",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    req = requests.get(url, headers=headers)
    req.raise_for_status()
    obj = json.loads(req.text)
    data = obj['data']['list']
    for i in data:
        print(i['geo'])
        print(i['ip'])
        print(i['time_at'])
except requests.RequestException as e:
    print(e)