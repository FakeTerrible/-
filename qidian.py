from bs4 import BeautifulSoup
import requests

base = 'https://www.qidian.com/rank/'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

if __name__ == '__main__':
    try:
        req = requests.get(base, headers=header)
        req.raise_for_status()
        soup = BeautifulSoup(req.text, 'html.parser')
        print(req.text)
        ranks = soup.find_all('div', class_='rank-list')
        for rank in ranks:
            title = rank.find('h3')
            print('+++++++++++++++++++++++++++++++++++++++++')
            print(title.text + '   https:' + title.a['href'])
            print('+++++++++++++++++++++++++++++++++++++++++')

            books = rank.find_all('li')
            for book in books:
                name = book.find('h2')
                data = book.find('a')
                print(name.text + '     https:' + data['href'])
    except:
        print('error')