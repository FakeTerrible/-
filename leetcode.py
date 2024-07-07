import json
import datetime
import requests

if __name__ == '__main__':
    try:
        url = 'https://leetcode.cn/graphql/'
        header = {
            'Connection': 'keep-alive',
            'Host': 'leetcode.cn',
            'Referer': 'https://leetcode.cn/problemset/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }

        q1 = {
            "query": "\n    query questionOfToday {\n  todayRecord {\n    date\n    userStatus\n    question {\n      questionId\n      frontendQuestionId: questionFrontendId\n      difficulty\n      title\n      titleCn: translatedTitle\n      titleSlug\n      paidOnly: isPaidOnly\n      freqBar\n      isFavor\n      acRate\n      status\n      solutionNum\n      hasVideoSolution\n      topicTags {\n        name\n        nameTranslated: translatedName\n        id\n      }\n      extra {\n        topCompanyTags {\n          imgUrl\n          slug\n          numSubscribed\n        }\n      }\n    }\n    lastSubmission {\n      id\n    }\n  }\n}\n    ",
            "variables": {},
            "operationName": "questionOfToday"
        }
        # data1 = json.dumps(q1)
        req1 = requests.post(url, headers=header, data=q1)
        req1.raise_for_status()
        # print(req1.headers['Set-Cookie'])
        # print(req1.cookies.items())
        # header['x-csrftoken'] = req1.cookies.get_dict()['csrftoken']
        # print(header)
        obj = json.loads(req1.text)
        # print(obj)
        question = obj['data']['todayRecord'][0]['question']
        titleSlug = question['titleSlug']
        q2 = {
            "query": "\n    query questionTranslations($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    translatedTitle\n    translatedContent\n  }\n}\n    ",
            "variables": {
                "titleSlug": titleSlug
            },
            "operationName": "questionTranslations"
        }

        # q2 = {
        #     "query": "\n    query abRecordName($abName: String!) {\n  abRecordName(abName: $abName)\n}\n    ",
        #     "variables": {
        #         "abName": "enableBindPhoneWeb"
        #     },
        #     "operationName": "abRecordName"
        # }

        data2 = json.dumps(q2)
        # print(type(data2))
        # header1 = {
        #     'Content-Type': 'application/json'
        # }
        # time.sleep(3)
        # print(req1.headers)
        # header1 = {}
        # t = req1.cookies.items()
        # cookie = t[0][0] + '=' + t[0][1]
        # print(cookie)
        # header1['Cookie'] = 'gr_user_id=a5d9589a-9bef-473f-8835-5fe6426a1cb1; a2873925c34ecbd2_gr_last_sent_cs1=feng-yan-7; __atuvc=3%7C16%2C0%7C17%2C1%7C18%2C4%7C19%2C1%7C20; _ga_RN3J7V8VS5=GS1.1.1690388051.110.0.1690388051.0; _bl_uid=h5lnUoahud38kOgd3ypLepp3dR9I; csrftoken=UU7pH3ZV3YMac3ezc646gpivGjXL5gtt2Gb2kztRyFVWEBPdgyjT9NjOtCTn8xiP; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTAxNTc4MyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjQ2OWM4YmE5MGUzYmJjOGYwNGI0ZjYxZTY3ZDhjYWQ2Y2NiOTg3Y2YwODcyYjQ3ZjQ2YjYyNDk5OTQ2YWQ0ZTUiLCJpZCI6MTAxNTc4MywiZW1haWwiOiIxMjU2MzI1OTcyQHFxLmNvbSIsInVzZXJuYW1lIjoiZmVuZy15YW4tNyIsInVzZXJfc2x1ZyI6ImZlbmcteWFuLTciLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jbi9hbGl5dW4tbGMtdXBsb2FkL3VzZXJzL2ZlbmcteWFuLTcvYXZhdGFyXzE1NzM5ODA5ODUucG5nIiwicGhvbmVfdmVyaWZpZWQiOnRydWUsIl90aW1lc3RhbXAiOjE3MDMwODA0MjMuMDAwNzM3NCwiZXhwaXJlZF90aW1lXyI6MTcwNTYwNDQwMCwidmVyc2lvbl9rZXlfIjozLCJsYXRlc3RfdGltZXN0YW1wXyI6MTcwNTIzODYzOX0.n5uE3Gm1CDEtpkwa7exIzCXaQYjUOkoFKPkZoGQ1eTk; _gid=GA1.2.1511045912.1705332163; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1704595139,1705160016,1705202899,1705427126; a2873925c34ecbd2_gr_session_id=c41ca8df-d69b-4a9a-acb1-7460901e377c; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=c41ca8df-d69b-4a9a-acb1-7460901e377c; a2873925c34ecbd2_gr_session_id_sent_vst=c41ca8df-d69b-4a9a-acb1-7460901e377c; Hm_lvt_f0faad39bcf8471e3ab3ef70125152c3=1705152661,1705332163,1705417957,1705497692; a2873925c34ecbd2_gr_cs1=feng-yan-7; Hm_lpvt_f0faad39bcf8471e3ab3ef70125152c3=1705500415; _ga=GA1.1.1922924449.1652451838; _ga_PDVPZYN3CW=GS1.1.1705497691.544.1.1705500415.40.0.0'
        # header1['X-Csrftoken'] = t[0][1]
        # header1['User-Agent'] = header['User-Agent']
        # header1['random-uuid'] = 'd741c9c3-0789-3d93-6e5b-f157bd2f1e7d'
        # header1['baggage'] = 'sentry-environment=production,sentry-release=61236e4e,sentry-transaction=%2Fproblems%2F%5Bslug%5D%2F%5B%5B...tab%5D%5D,sentry-public_key=1595090ae2f831f9e65978be5851f865,sentry-trace_id=a07d0d2c74114e0db579ac1b8b1d9d2a,sentry-sample_rate=0.03'
        # header1['Host'] = header['Host']
        header['Content-Type'] = 'application/json'
        header['Referer'] = 'https://leetcode.cn/problems/' + titleSlug + \
            '/?envType=daily-question&envId=' + str(datetime.date.today())
        # print(header)
        req2 = requests.post(url, headers=header, data=data2)
        req2.encoding = 'utf-8'
        req2.raise_for_status()
        content = json.loads(req2.text)
        print(content)
    except requests.RequestException as e:
        print(e)
