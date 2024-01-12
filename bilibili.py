import json
import time
import requests

if __name__ == '__main__':
    try:
        wts = int(time.time())
        url = 'https://api.bilibili.com/x/web-interface/wbi/index/top/feed/rcmd?web_location=1430650&y_num=4&fresh_type=4&feed_version=V_FAVOR_WATCH_LATER&fresh_idx_1h=1&fetch_row=4&fresh_idx=1&brush=1&homepage_ver=1&ps=12&last_y_num=5&screen=1536-564&seo_info=&last_showlist=av_923258156,av_965806137,av_623621466,av_580804406,ad_5614,av_666025316,av_n_665943487,av_n_241094530,av_n_537653932,av_n_877818683&uniq_id=1394934220622&w_rid=e5a14a24cc7d6412df6fb423ec91bd93&wts={}'.format(str(wts))
        header = {
            "Cookie":"LIVE_BUVID=AUTO9915844200023499; i-wanna-go-back=-1; CURRENT_BLACKGAP=0; buvid_fp_plain=undefined; is-2022-channel=1; buvid4=38BEC549-9904-52F8-63AA-48C2DC1EC1E215362-022012709-AYi90B%2FUs1ZOrNiVf5WzKQ%3D%3D; DedeUserID=278789164; DedeUserID__ckMd5=2864e3e3f1e788fa; b_ut=5; CURRENT_QUALITY=120; buvid3=C6E2C9E6-16A3-341C-4925-51B4CF1DE82C92609infoc; b_nut=1679057092; header_theme_version=CLOSE; nostalgia_conf=-1; _uuid=B99E2103D-9145-9C86-12BA-3567F2AFEDAE01537infoc; CURRENT_PID=d53a9680-d2df-11ed-b68a-ef8cf278306e; FEED_LIVE_VERSION=V8; home_feed_column=5; enable_web_push=DISABLE; fingerprint=851bea542192a029d1f2fb4a6ae1ff61; buvid_fp=851bea542192a029d1f2fb4a6ae1ff61; PVID=1; rpdid=|(J|k~|Ylu|~0J'u~|RJ)~k||; innersign=0; b_lsid=24E91E24_18CF985DCC3; SESSDATA=f3cb4c9e%2C1720545350%2C45060%2A12CjC1gSgH6-jsalKUuhv4pgFI2_kloHL6OfA15_1L4yZ6M0OshuXhkouq1GNo57bPhXYSVm9lNGdhUDhyTC03T1NqQWhpamk5UC1mM2daMzBlWHFJcnIwY3o4MEFzQ0VBSEhDN1JHUHhOLU1vc21nZ2ZzaDkxOG44TEhpZktId1ZWNmhFWUN1VHJnIIEC; bili_jct=55a636702756165747a7c560a06a24b2; sid=7cidm9if; bp_video_offset_278789164=885378422582280200; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDUyNTI1NzUsImlhdCI6MTcwNDk5MzMxNSwicGx0IjotMX0.D5F_16Cuh9SWuZ7MmhS3zhy0BE7k2juYatr8u-Andy4; bili_ticket_expires=1705252515; CURRENT_FNVAL=16; browser_resolution=1536-564",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        req = requests.get(url, headers=header)
        req.raise_for_status()
        obj = json.loads(req.text)
        items = obj['data']['item']
        for i in items:
            print('------------------------------')
            print(i['title'])
            print(i['uri'])
    except requests.RequestException as e:
        print(e)