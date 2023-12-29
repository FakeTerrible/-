import json
import requests
import os

if __name__ == '__main__':
    os.makedirs('./image/', exist_ok=True)
    s = input()
    base_url = 'https://api.huaban.com/search/file?text={}&sort=all&limit=40&page=1&position=search_pin&fields=pins:PIN,total,facets,split_words,relations,recommend_topics'.format(s)
    try:
        req = requests.get(base_url)
        req.raise_for_status()
        data_obj = json.loads(req.text)
        data_list = data_obj['pins']
        for i in data_list:
            title = i['board']['title'].strip()
            key = i['file']['key']
            print(title + ' ' + key)
            IMAGE_URL = 'https://gd-hbimg.huaban.com/{}_fw658webp'.format(key)
            r = requests.get(IMAGE_URL)
            with open('./image/{}.png'.format(title), 'wb') as f:
                f.write(r.content)
    except requests.RequestException as e:
        print(e)