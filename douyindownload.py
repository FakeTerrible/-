import os
import requests

if __name__ == '__main__':
    try:
        os.makedirs('./shipin/', exist_ok=True)
        url = 'https://v26-web.douyinvod.com/b4cb45dafef489f94e7162e879ceb0ee/65a56d39/video/tos/cn/tos-cn-ve-15/oEyxqCTpEj9gBhXAIudPXAAaMefwyDthPgtzJh/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=668&bt=668&cs=2&ds=3&ft=LjhJEL998xXdu4PmD0P5H4eaciDXtBQOk_QEejoi6SjD1Inz&mime_type=video_mp4&qs=15&rc=ZzY7ZTw1MzY3NTtpZTw3ZEBpM21wcjU6ZnF0cDMzNGkzM0A1XjUvYDZjNi8xMTYzXjUyYSNkL2FfcjRfNjRgLS1kLTBzcw%3D%3D&btag=e00008000&dy_q=1705336608&feature_id=7f4d8f8be65505495ee2bac95e186f16&l=20240116003647E585CE6B272AE035DB2C&__vid=7318249089613810984'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        req = requests.get(url, headers=header)
        req.raise_for_status()
        with open('./shipin/one.mp4', 'wb') as f:
            f.write(req.content)
        
    except requests.RequestException as e:
        print(e)