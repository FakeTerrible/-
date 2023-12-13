from bs4 import BeautifulSoup
import requests

# 获取网页内容

def Ser(url, header):
    try:
        req = requests.get(url, headers=header)
        req.raise_for_status()
        soup = BeautifulSoup(req.text, features = 'html.parser')
        target = soup.find_all("tr", class_ = 'item')
        for i in target:
            title = i.find('div', class_ = 'pl2').a['title']
            author = i.find('p', class_ = 'pl').text
            quote = ''
            if i.find('span', class_ = 'inq'):
               quote = i.find('span', class_ = 'inq').text
            # print('+++')
            print('书名：' + title)
            print('作者：' + author)
            print('评语：' + quote)
            print('---------------------------------------------')
            # print('+++')

    except:
        print('error')


if __name__ == '__main__':
    base_url = 'https://book.douban.com/top250?start='
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    for i in range(10):
        url = base_url + str(i * 25)
        Ser(url, header)

