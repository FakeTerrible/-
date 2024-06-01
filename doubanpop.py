import json
from Req.Get import getbody
import urllib.parse
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://m.douban.com/rexxar/api/v2/tv/recommend?refresh=0&start=0&count=20&selected_categories=%7B%7D&uncollect=false&tags=2024'
    headers = {
        "Host": "m.douban.com",
        "Origin": "https://movie.douban.com",
        "Referer": "https://movie.douban.com/tv/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    headers_1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    obj = json.loads(getbody(url, headers))
    for i in obj['items']:
        print("|++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")
        print("|+" + i['title'])
        print("|+" + i['card_subtitle'])
        print("|+" + "https://im1907.top/?jx=" + urllib.parse.quote(i['title']))
        urlson = 'https://movie.douban.com/subject/' + i['id'] + '/'
        soup = BeautifulSoup(getbody(urlson, headers_1), features='html.parser')
        report = soup.find('div', id='link-report-intra')
        print("|+" + report.text.strip())
