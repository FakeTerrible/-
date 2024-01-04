import requests
import json

try:
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    req = requests.get(url, headers = header)
    req.raise_for_status()
    obj = json.loads(req.text)
    subjects = obj['subjects']
    for i in subjects:
        print(i['title'])

except requests.RequestException as e:
    print(e)