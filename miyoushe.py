import requests

try:
    # 该api从手机app抓包获得
    url = 'https://api-takumi.mihoyo.com/event/luna/extra_award?act_id=e202311201442471&uid=108801741&region=cn_gf01&lang=zh-cn'
    headers = {  
        'Host': 'api-takumi.mihoyo.com',  
        'Connection': 'keep-alive',  
        'x-rpc-signgame': 'hk4e',  
        'Accept': 'application/json, text/plain, */*',  
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; 2206122SC Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 miHoYoBBS/2.68.1',  
        'Origin': 'https://act.mihoyo.com',  
        'X-Requested-With': 'com.mihoyo.hyperion',  
        'Sec-Fetch-Site': 'same-site',  
        'Sec-Fetch-Mode': 'cors',  
        'Sec-Fetch-Dest': 'empty',  
        'Referer': 'https://act.mihoyo.com/',  
        'Accept-Encoding': 'gzip, deflate',  
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',  
        'Cookie': '**'  
    }
    req = requests.get(url, headers=headers)
    req.raise_for_status()
    print(req.text)
except requests.RequestException as e:
    print(e)