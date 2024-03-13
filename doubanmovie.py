import json

from bs4 import BeautifulSoup
from Req.Get import getbody

if __name__ == '__main__':
    base = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    obj = json.loads(getbody(base, headers))
    subjects = obj['subjects']
    for i in subjects:
        print(i['title'])
        body = getbody(i['url'], headers)
        soup = BeautifulSoup(body, features='html.parser')
        content = soup.find('div', id='link-report-intra').text.strip()
        print(content)
