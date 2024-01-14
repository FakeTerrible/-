import json
import requests

if __name__ == '__main__':
    try:
        url = 'https://api.bilibili.com/pgc/web/timeline?types=1&before=6&after=6'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'  
        }
        req = requests.get(url, headers=header)
        req.raise_for_status()
        obj = json.loads(req.text)
        for i in obj['result']:
            print(i['date'])
            if i['episodes']:
                for j in i['episodes']:
                    print(j['title'])
                    print(j['pub_index'])
                    print(j['pub_time'])
    except requests.RequestException as e:
        print(e)