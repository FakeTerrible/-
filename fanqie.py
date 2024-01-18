import requests
import brotli

try:
    url = 'https://fanqienovel.com/api/rank/category/list?app_id=1967&rank_list_type=3&offset=10&limit=10&category_id=24&rank_version=&gender=0&rankMold=2&msToken=GEPG0VecXQ6TCsgng9uTVcG2Ajo6ON1-Ix_G3TQq7a6L2FLu4PekuKSJU5mWEfEiHQurPPm9ZWcFSPtSjll2B1vUMFVLmZ68rq62WgR4PsP5MdeI837zVPFtwknsLw%3D%3D&a_bogus=x74QXO2hMsm1iEvS%2Fwkz9cUmAq80YW5YgZEz7j0oH0ou'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    req = requests.get(url, headers=header)
    req.raise_for_status()
    # # content = brotli.decompress(req.content)
    # res = req.content.decode('utf-8')
    print(req.content)
except requests.RequestException as e:
    print(e)
