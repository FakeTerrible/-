import json
import requests


def GetBody(url, header, data=None):
    try:
        if data:
            req = requests.post(url, headers=header, data=data)
            req.raise_for_status()
            return req.text
        else:
            req = requests.get(url, headers=header)
            req.raise_for_status()
            return req.text

    except Exception as e:
        return e


# 稀土掘进自动签到
# data中的数据自己找寻 
url = 'https://api.juejin.cn/growth_api/v1/check_in'
# _signature 要找到签到的接口，在标头里面能看到，有些接口是没有_signature参数的，注意区分
data3 = {
    'aid': '',
    'uuid': '',
    '_signature': ''
}

header2 = {
    "cookie": ''
}

# r = requests.post(url, data, headers=header)
r = GetBody(url, header2, data3)
res = json.loads(r)
print(res['err_msg'])

urlD = 'https://api.juejin.cn/growth_api/v1/lottery/draw'
dataD = {
    'aid': '',
    'uuid': '',
}
# r1 = requests.post(urlD, dataD, headers=header)
r1 = GetBody(urlD, header2, dataD)
res1 = json.loads(r1)
print(res1['data']['lottery_name'])
