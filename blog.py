import json
import requests

try:
    url = 'https://www.hello-algo.com/search/search_index.json'
    req = requests.get(url)
    req.raise_for_status()
    req.encoding = 'utf-8'
    # obj = json.loads(req.text)
    # docs = obj['docs']
    with open('./web/blog.json', 'wb') as f:
        f.write(req.content)
except requests.RequestException as e:
    print(e)