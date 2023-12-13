import requests
import json

# 获取抖音热点内容链接
base_url = 'https://www.douyin.com/aweme/v1/web/hot/search/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&detail_list=1&source=6&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=118.0.0.0&browser_online=true&engine_name=Blink&engine_version=118.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7290068846450755127&msToken=thw-YD1_6xfkmgY2aVQK6rOmOKZN0y3e_lkC4utzParV-20q7MPjEdjAyR5E1EJPuJ5iLwUHOjeNv7_Kt872CkGpRH1vTBkzii3ZI_2KVEFA6K6m0o_n1vXzRMEOGD8=&X-Bogus=DFSzsdVO-ukANrNPtTt/tKXAIQ5Z'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Cookie': 'xgplayer_user_id=3938156158; __ac_signature=_02B4Z6wo00f01iO-XogAAIDDQLSe4edshRojmloAAO3SWCaQpJkDuDE8AePvP2aUVxavwElItCaJrNaTzS18jQQ603Z7Gqpiir-1eFTqQF340JGcOzYHRhsWoTw83Gv7fDdVyO9dBAWyUG.yaf; ttwid=1%7CpWhZ49mxkZb1TwNmEoQyhskZRLYjBbXaxC4X2SqYVn4%7C1697351436%7Ca367985d7038c24548efe00ffc1e798d9adf9c146270fc32f54ed60bb9d6a0fe; douyin.com; device_web_cpu_core=8; device_web_memory_size=8; architecture=amd64; webcast_local_quality=null; strategyABtestKey=%221697351441.801%22; passport_csrf_token=5f5b28897a565bb08ec287afb335c705; passport_csrf_token_default=5f5b28897a565bb08ec287afb335c705; s_v_web_id=verify_lnr382l5_R2Rugn9L_g9Sh_4K5T_A2Qc_B9rljLkCIeiM; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.6%7D; csrf_session_id=d0c0526ef09c37b248fc48e5b9656301; passport_assist_user=CkEdJNOwy15nA2eqsGCoJE4O4FuMjYv_x1tTpTARdjcpAxGGTiMYAHUklK_Gs-SYr_Y7tLiF3N9pSVUPxaZQj6MnXxpKCjzYPKBZUy5K-n4xjI1OYvEVu_7pI16AsLaZ5EjIZkWCA95-tfJ3TSzOMMQeMLWg2biUc-dOig0NbqwPewcQ6M--DRiJr9ZUIAEiAQMhZstl; n_mh=ERS1KWlVq1yqcoSqx8QS_d9rXXmcTCXg58yZImopLZY; sso_uid_tt=9ce80b160f40ae1c5a3352bf37c45130; sso_uid_tt_ss=9ce80b160f40ae1c5a3352bf37c45130; toutiao_sso_user=256421b72d48dd4c4650d6d4ee04b032; toutiao_sso_user_ss=256421b72d48dd4c4650d6d4ee04b032; sid_ucp_sso_v1=1.0.0-KDAwMzVhZjU2NDBkZjhmNGMwZmU4NTVmZGUxYWJiYjkyM2E4YmU5MWYKHwi-mcChlPXpAhDfjq6pBhjvMSAMMKyI0fQFOAZA9AcaAmxmIiAyNTY0MjFiNzJkNDhkZDRjNDY1MGQ2ZDRlZTA0YjAzMg; ssid_ucp_sso_v1=1.0.0-KDAwMzVhZjU2NDBkZjhmNGMwZmU4NTVmZGUxYWJiYjkyM2E4YmU5MWYKHwi-mcChlPXpAhDfjq6pBhjvMSAMMKyI0fQFOAZA9AcaAmxmIiAyNTY0MjFiNzJkNDhkZDRjNDY1MGQ2ZDRlZTA0YjAzMg; odin_tt=bfd4986bdad3cf94cd60c958fb5c1311ceac7e8a34b4976c163bc1307dce2c9a078d66e30b9a4ee2271464f4c429bd1527f89454e0b7289c8cd3730111f83dd7; passport_auth_status=a32a359a55a0b442cc2e0977374661de%2C; passport_auth_status_ss=a32a359a55a0b442cc2e0977374661de%2C; uid_tt=9478083036d023d6d368904d298930fc; uid_tt_ss=9478083036d023d6d368904d298930fc; sid_tt=05f79ee2f62db70e96a836e2eb0ce765; sessionid=05f79ee2f62db70e96a836e2eb0ce765; sessionid_ss=05f79ee2f62db70e96a836e2eb0ce765; publish_badge_show_info=%220%2C0%2C0%2C1697351528893%22; LOGIN_STATUS=1; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=a12ee7898787903ac591288efcb19a7e; __security_server_data_status=1; store-region=cn-js; store-region-src=uid; d_ticket=c37345d91ea0d3e157368beef0d22bbc902b8; sid_guard=05f79ee2f62db70e96a836e2eb0ce765%7C1697351549%7C5183974%7CThu%2C+14-Dec-2023+06%3A32%3A03+GMT; sid_ucp_v1=1.0.0-KDU2OTQxYmJkODg4NWNlYmQyZTA1OTRiY2Q0MTAwOGNhZmEzMGExZTIKGwi-mcChlPXpAhD9jq6pBhjvMSAMOAZA9AdIBBoCaGwiIDA1Zjc5ZWUyZjYyZGI3MGU5NmE4MzZlMmViMGNlNzY1; ssid_ucp_v1=1.0.0-KDU2OTQxYmJkODg4NWNlYmQyZTA1OTRiY2Q0MTAwOGNhZmEzMGExZTIKGwi-mcChlPXpAhD9jq6pBhjvMSAMOAZA9AdIBBoCaGwiIDA1Zjc5ZWUyZjYyZGI3MGU5NmE4MzZlMmViMGNlNzY1; passport_fe_beating_status=true; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1697956415386%2C%22type%22%3A1%7D; download_guide=%223%2F20231015%2F0%22; msToken=TFqX-xc5bY1q29Aje--1eb4Aeh03pb0Z3jSllLGX_OrlpemPnQ3NIVZ2Q0nFA1lofJCqnPWBFq7Y4ec35m9seBD4uYwf6Wjt2EnbPiFapKTYs8PT6RpwpWJwXaTQ8pM=; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; home_can_add_dy_2_desktop=%221%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAoavP0fj2eaEXfUhFlm0fYiY123xnRG047z69TMluUIraGOK0tiKhPuI_aMA2JMQm%2F1697385600000%2F0%2F0%2F1697352947779%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAoavP0fj2eaEXfUhFlm0fYiY123xnRG047z69TMluUIraGOK0tiKhPuI_aMA2JMQm%2F1697385600000%2F0%2F0%2F1697353547780%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCT25GazRUVDI4SlhJa004K0dkTjdwTkRDTHpCY0YwY3BoSGp0dTJzU0VIeDN2VkJqbkd1ZEkzaWFjYWcwOGZiYWZ3Uk9sS25EUnh6SU1PZ3l6U1ZLakU9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; tt_scid=9GF4WzwjXfVx2Rdw4CFiGHZG5yYj6SY-hAsPWhdd3uRUbr2wTHigvTRdyBroPvGudc17; pwa2=%220%7C0%7C2%7C0%22; msToken=rESYb86Hd_I039Xrdc0JRNw7KTgyoz5SupzPJ1_dvx9LK5lfhTi7pprIXv_F450otKNx333LxPsR-n5f-1un2tZeGfbvNdpe5FfPtcqgs3MoP8h4Ph9JJa-txzImdSyu; IsDouyinActive=false',
    'Referer':'https://www.douyin.com/hot'
}

try:
    req = requests.get(base_url, headers=header)
    req.raise_for_status()
    target = json.loads(req.text)
    data = target['data']
    # 处理实时上升数据
    print("实时上升话题：")
    trending = data['trending_list']
    for i in trending:
        print("https://www.douyin.com/search/" + i['word'])
        # print(i['group_id'])
    print(" ——————————————————————————————————————————————————————————————————————————————")
    print("|                                                                              |")
    print(" ******************************************************************************")
    print("热点话题：")
    word = data['word_list']
    for i in word:
        print("https://www.douyin.com/search/" + i['word'])

except:
    print(-1)