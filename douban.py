import time
import urllib.parse

import requests
from bs4 import BeautifulSoup

base_url = 'https://movie.douban.com/chart'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}


def GetBody(url, header):
    try:
        req = requests.get(url, headers=header)
        req.raise_for_status()
        return req.text
    except:
        return -1

# print(GetBody(base_url, header))
soup = BeautifulSoup(GetBody(base_url, header), features='html.parser')

target_list = soup.find_all('div', class_='pl2')
count = 0
print('豆瓣电影排行\n')
for i in target_list:
    count += 1
    print('\033[1;31;40mtop ' + str(count)+'\033[0m\n')
    title_lsit = i.a.text.strip().replace('\n', '').split('/')
    title = title_lsit[0].strip()
    print('电影名称： ' + title + '\t' + 'https://im1907.top/?jx=' + urllib.parse.quote(title))
    # print('\n')
    time.sleep(1)
    body_soup = BeautifulSoup(GetBody(i.a['href'], header), features='html.parser')
    info = body_soup.find(id='info')
    print(info.text.strip())
    target = body_soup.find_all(id='link-report-intra')[0]
    target_list = target.text.strip().replace(' ', '').replace('<br/>', '').split('\n')
    # print(target_list)
    print('简介：')
    for j in target_list:
        if j == ''or j == '©豆瓣':
            continue
        print('\033[1;32;40m' + j.strip()+'\033[0m')
    print('------------------------------------------------------------------------')
    # print('电影时间/导演/演员：' + i.p.text + '\n')


