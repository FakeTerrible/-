import requests

if __name__ == '__main__':
    try:
        url = 'https://www.bilibili.com/anime/?spm_id_from=333.1007.0.0'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'  
        }
        req = requests.get(url, headers=header)
        req.raise_for_status()
        print(req.text)
    except requests.RequestException as e:
        print(e)