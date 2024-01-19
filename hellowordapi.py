import requests
import json

try:
    url = 'https://abroad.hellogithub.com/v1/?sort_by=last&tid=&page=1'
    req = requests.get(url)
    req.raise_for_status()
    obj = json.loads(req.text)
    data = obj['data']
    for i in data:
        print(i['title'])
        print(i['summary'])
        print('https://hellogithub.com/repository/' + i['item_id'])
except requests.RequestException as e:
    print(e)