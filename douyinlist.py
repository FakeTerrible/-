import json
# import time
import requests

try:
    # ts = str(int(time.time()))
    url = 'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAFXWu1B65vQdDptt5-hD4qTjmgvUnvZ55eWtoQRWx7uM&max_cursor=1698639947000&locate_item_id=7327304602804686091&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=20&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=1.25&effective_type=3g&round_trip_time=400&webid=7290068846450755127&msToken=CqxEXsMTwfBOGf_iAXbhYGCuXXQdza78hosIY9thvQd9PG3iEBA0VSGu_2qiJXGx0uk6Ur6XklRGrCj7qZpR2jKMNfzUt9KoMpen3wdHoY5HfH4qPJnjRRA=&X-Bogus=DFSzsdVEjSJANrpTtE2ZqTSX1b2a'
    cookies = {
        'ttwid':'1%7CpWhZ49mxkZb1TwNmEoQyhskZRLYjBbXaxC4X2SqYVn4%7C1697351436%7Ca367985d7038c24548efe00ffc1e798d9adf9c146270fc32f54ed60bb9d6a0fe',
        'n_mh':'ERS1KWlVq1yqcoSqx8QS_d9rXXmcTCXg58yZImopLZY',
        'LOGIN_STATUS':'1',
        'store-region':'cn-js',
        'store-region-src':'uid',
        'd_ticket':'c37345d91ea0d3e157368beef0d22bbc902b8',
        'my_rd':'2',
        '__live_version__' : '%221.1.1.4522%22',
        'passport_csrf_token' : '8ee4a64a1cd2402c4f415246d4008e07',
        'passport_csrf_token_default' : '8ee4a64a1cd2402c4f415246d4008e07',
        's_v_web_id':'verify_lq8zoitl_wjYF3CWz_QsWU_4uQv_AznQ_IEIn8fcZsaNa',
        'bd_ticket_guard_client_web_domain':'2',
        'passport_assist_user':'CkFlT15qEvepd2RsqYrpervOe1c6klHymrVHfJBS2Ia4q7aDP6vPVF-WJiDA0z51W_QqEc3vf42q6P5MctvXUz2lXRpKCjz6IYzsaesYohS_G9F7SkpeZ_D2QxG4-gdLdh_o6lFKcMjBv2n4KHiCysCnrcTkrX8f6Mb6N4tPbQbGkDgQo57FDRiJr9ZUIAEiAQNc1CTD',
        'sso_uid_tt':'38da8840a18c1527adce6167f35e73bc',
        'sso_uid_tt_ss':'38da8840a18c1527adce6167f35e73bc',
        'toutiao_sso_user':'188b125095b58b5e5d8bbe7f98995223',
        'toutiao_sso_user_ss':'188b125095b58b5e5d8bbe7f98995223',
        'uid_tt':'42d41a83c30acb56f2285fcdde74865d',
        'uid_tt_ss':'42d41a83c30acb56f2285fcdde74865d',
        'sid_tt':'113e1dc3bc816caaec641dbdcc736aea',
        'sessionid':'113e1dc3bc816caaec641dbdcc736aea',
        'sessionid_ss':'113e1dc3bc816caaec641dbdcc736aea',
        '_bd_ticket_crypt_doamin':'2',
        '_bd_ticket_crypt_cookie':'7e0f4ce6915cd187de311ebee3d07344',
        '__security_server_data_status':'1',
        'dy_swidth':'1536',
        'dy_sheight':'864',
        'FOLLOW_NUMBER_YELLOW_POINT_INFO':'%22MS4wLjABAAAAoavP0fj2eaEXfUhFlm0fYiY123xnRG047z69TMluUIraGOK0tiKhPuI_aMA2JMQm%2F1705766400000%2F0%2F1705692481144%2F0%22',
        'publish_badge_show_info':'%220%2C0%2C0%2C1706024812372%22',
        'volume_info':'%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.6%7D',
        'sid_ucp_sso_v1':'1.0.0-KGUzZDE5MDA0ODI5ZDIxNDliY2MwMmMyOGMwYWI2NjViM2IzODg0NWEKIQi-mcChlPXpAhDqvr-tBhjvMSAMMKyI0fQFOAVA-wdIAxoCaGwiIDE4OGIxMjUwOTViNThiNWU1ZDhiYmU3Zjk4OTk1MjIz',
        'ssid_ucp_sso_v1':'1.0.0-KGUzZDE5MDA0ODI5ZDIxNDliY2MwMmMyOGMwYWI2NjViM2IzODg0NWEKIQi-mcChlPXpAhDqvr-tBhjvMSAMMKyI0fQFOAVA-wdIAxoCaGwiIDE4OGIxMjUwOTViNThiNWU1ZDhiYmU3Zjk4OTk1MjIz',
        'sid_guard':'113e1dc3bc816caaec641dbdcc736aea%7C1706024811%7C5184000%7CSat%2C+23-Mar-2024+15%3A46%3A51+GMT',
        'sid_ucp_v1':'1.0.0-KGViYzlkY2U2MjM3ZjY4MzM0YjRiNzNlMjk5NmZhODJhY2EwZTYxMzAKGwi-mcChlPXpAhDrvr-tBhjvMSAMOAVA-wdIBBoCbHEiIDExM2UxZGMzYmM4MTZjYWFlYzY0MWRiZGNjNzM2YWVh',
        'ssid_ucp_v1':'1.0.0-KGViYzlkY2U2MjM3ZjY4MzM0YjRiNzNlMjk5NmZhODJhY2EwZTYxMzAKGwi-mcChlPXpAhDrvr-tBhjvMSAMOAVA-wdIBBoCbHEiIDExM2UxZGMzYmM4MTZjYWFlYzY0MWRiZGNjNzM2YWVh',
        '__ac_nonce':'065b283ca00439295f89a',
        '__ac_signature':'_02B4Z6wo00f01bB3tYAAAIDAulFuK5BeTN2wU7EAAAmwlL87bZZiiYWtdXq7Vqh4-ARqMbdchCpRQ-vsL1sYyEwMbOcPdDG8pO-7yrnTMvdfCz2OwsZuon6cgtByW9jkAQmm7I.y18KImX.H48',
        # 'douyin.com',
        'device_web_cpu_core':'8',
        'device_web_memory_size':'8', 
        'architecture':'amd64',
        'IsDouyinActive':'true',
        'stream_recommend_feed_params':'%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A1.25%2C%5C%22effective_type%5C%22%3A%5C%223g%5C%22%2C%5C%22round_trip_time%5C%22%3A400%7D%22',
        'csrf_session_id':'404858b0e87f3b75a81a36ee12b3fbbc',
        'FOLLOW_LIVE_POINT_INFO':'%22MS4wLjABAAAAoavP0fj2eaEXfUhFlm0fYiY123xnRG047z69TMluUIraGOK0tiKhPuI_aMA2JMQm%2F1706198400000%2F0%2F1706197970524%2F0%22',
        'strategyABtestKey':'%221706197970.872%22',
        'bd_ticket_guard_client_data':'eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCT25GazRUVDI4SlhJa004K0dkTjdwTkRDTHpCY0YwY3BoSGp0dTJzU0VIeDN2VkJqbkd1ZEkzaWFjYWcwOGZiYWZ3Uk9sS25EUnh6SU1PZ3l6U1ZLakU9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJz"aW9uIjoxfQ%3D%3D; passport_fe_beating_status=true; home_can_add_dy_2_desktop=%221%22; odin_tt=780a3ec75b85f0f337388e932fae64fd1c076eda4656238e52b2a795f5ac5b5cd5ce23d51aec94a7ca14bd1a3e4ebe64; msToken=Pc0sCOhbTxWnGbetcCJMSuoIPzlWSmb1lduzb1FZ4-1jO44aLgSXhKx2uVjC-88QZVfgVcr68FNElcuVKGAqd48f6sRlE-s0h_Cn8NjQMRA99bvKdTwHvQA=; tt_scid=gjohaBqbw4lxj4aTt-qgi8h-k1lVrHddc1Gntf5pKEGM4BAGsRHtCW0vJI6qzorveaf2; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A1%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; msToken=tY1vBjAEx5pYHAlix0LuFa0B6ffCo9DrFDfPg4UIWhwEenPDj8PCh5poZD_XJmi2_ob390AKA2LvPEz4LdbUT3JeeI6XIA3GHfHDmou5wp_eoe4BCMj4Iu0=',
        'xg_device_score':'7.554258647749727'
    }

    headers = {
        'authority': 'www.douyin.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'ttwid=1%7CvQ6QCiLyIG9SJypBIXRtIfGPJXv6br9a79NgmLfR-U4%7C1697436889%7C0ea69e384e5deb1dc65f4200190d8d2f33f9c4ca6c30e10208ee46af29a5015d; xgplayer_user_id=905282558930; live_use_vvc=%22false%22; bd_ticket_guard_client_web_domain=2; s_v_web_id=verify_lqb0qvhc_0iBmLw3t_sd2W_46Bf_9Mcf_68rowVA3IeLv; passport_csrf_token=200d4853a5fd758c92f83d148e5a6655; passport_csrf_token_default=200d4853a5fd758c92f83d148e5a6655; n_mh=k9zkCfOQfFegoa7kc0V7SXvDVdHwnUROJ967U1dUUI0; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=ee202c92a742381a4b3088235c965832; __security_server_data_status=1; store-region=cn-bj; store-region-src=uid; LOGIN_STATUS=0; dy_swidth=1728; dy_sheight=1117; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.314%7D; odin_tt=20343b08ecb1611a4b04324c1a697f7e92e68e324e4606b2c80abadd3210987dc5b78518a2b0b6e221726782326016937e13203155c45a3b6a704d48ceb7e65e7f250011dbd98cd56711807de5cccdf0; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20240122%2F0%22; pwa2=%220%7C0%7C3%7C0%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; __ac_nonce=065afa15400ef3673f1ab; __ac_signature=_02B4Z6wo00f012jlk1gAAIDAOhqzQKoWZrdoxZfAAL-iqJci2ZpglkK6M7yKIwliOzfNMYPqrKO.vuP0wT0vQT7a2PJDE6YD4Ay8vsvJo0BaiNeB-WiQrnKtEPSVe3-wGkOxq1t1gYLod2Ro14; csrf_session_id=b03ca9c6fb9b4ef4d85efd46128ba9de; strategyABtestKey=%221706008917.986%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQnNtWm5qUEJ6SExwVlpzZjhzV1BoYWlOQzJZM0ZNNk9iTnNoOGRQMzFmRFVtOVdDLzhXWHJ4NVFDTXZvTWZLdFNuMVlKU2ZvclVETmZ6SEkrUkF5MVE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; tt_scid=YGv8c2oqhsh25YyltzHqh1S9m0yykWythr.t-x6hPh8pknuFsZTspYcKKHrLRlFw371e; IsDouyinActive=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1728%2C%5C%22screen_height%5C%22%3A1117%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A10%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A150%7D%22; home_can_add_dy_2_desktop=%221%22; msToken=_vjXTFXg1qnycSDdQcVu4ao-RjLHYr360C_Mi5plElthGniJuBQhDGgbj25Ncskr8S-Vb3LYE6kHoUScjl01v1VOhDyBI_aqKpjtYhlA2lkmF63DpwtUy0s_P5B3DA==; msToken=4vtKfjALRZz-4wLsSKNCxUShqEfmp8_tiY55saliOmnGo4e_adJhsS5hSUSewB19It4MrqasbgcY75oIFaMgIGHv2-8lXKQx4whBno5G3oKX5N3J8d8HskZxLoebXA==',
        'pragma': 'no-cache',
        'referer': 'https://www.douyin.com/user/MS4wLjABAAAA0HwZJN6-JDCSTjxiMk-czhyZWxes8XIDEjppFXExauK8-kQTLMEH9ZdfIXxnl9tS',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    req = requests.get(url, cookies=cookies, headers=headers)
    req.raise_for_status()
    # print(req.text)
    obj = json.loads(req.text)
    aweme_list = obj['aweme_list']
    # print(len(aweme_list))
    for i in aweme_list:
        print(i['preview_title'])
        # print(i['desc'])
        for j in i['video']['play_addr']['url_list']:
            print(j)
except requests.RequestException as e:
    print(e)
