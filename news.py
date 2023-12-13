import requests
from bs4 import BeautifulSoup

base1 = 'https://www.ndrc.gov.cn/xwdt/'
base2 = 'https://www.ndrc.gov.cn/xwdt/szyw/'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

def main():
    try:
        req = requests.get(base1, headers=header)
        req.raise_for_status()
        req.encoding = "utf-8"
        soup = BeautifulSoup(req.text, 'html.parser')
        target = soup.find_all('div', class_='news')
        news = target[0].find_all('li')
        print("发改委热点新闻")
        for i in range(len(news)):
            new = news[i]
            print("top " + str(i))
            print("新闻标题：" + new.a['title'])
            print("新闻链接：https://www.ndrc.gov.cn/xwdt/" + new.a['href'][2:])
            print("发布日期" + new.span.text)
        print(" ___________________________________________________________ ")
        print("|                                                           |")
        print(" ########################################################### ")
        print("通知公告：")
        notes = target[1].find_all('li')
        for i in range(len(notes)):
            note = notes[i]
            print("top " + str(i))
            print("公告标题：" + note.a['title'])
            print("公告链接：https://www.ndrc.gov.cn/xwdt/" + note.a['href'][2:])
            print("发布日期" + note.span.text)
        print(" ___________________________________________________________ ")
        print("|                                                           |")
        print(" ########################################################### ")
        print("时政要闻：")
        req1 = requests.get(base2, headers=header)
        req1.raise_for_status()
        req1.encoding = 'utf-8'
        soup1 = BeautifulSoup(req1.text, 'html.parser')
        target1 = soup1.find_all('div', class_='list')
        curs = target1[0].find_all('li')
        for i in range(len(curs)):
            cur = curs[i]
            if cur.text == '':
                continue
            # print("top " + str(i))
            print("时政标题：" + cur.a['title'])
            print("时政链接：" + cur.a['href'])
            print("发布日期" + cur.span.text)
    except:
        print('error')
if __name__ == '__main__':
    main()