import requests

def getbody(url, headers):
    try:
        req = requests.get(url, headers=headers)
        req.raise_for_status()
        print("请求结果：" + str(req.status_code))
        return req.text
    except requests.RequestException as e:
        print(e)
        return e