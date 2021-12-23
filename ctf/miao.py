import time

import requests

writer = open("flag3.txt", 'w')
for i in range(10, 100, 1):
    url = "http://202.38.93.111:10001"
    headers = {
        'Host': '202.38.93.111:10001',
        'Content-Length': '70',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://202.38.93.111:10001',
        'Referer': 'http://202.38.93.111:10001/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'session=eyJ0b2tlbiI6IjIyMDU6TUVRQ0lEMVdFYWNyWlhJbkpJdTlOcUU4OGhKcE9RYTdyUDYvL1MrOHAyT3lpZ1V4QWlCVHovL2NzSHNQbUdidkFKK0FJWmRQZmlROW5DeEJZK0t4b0xyWVhxZk9KZz09In0.YXgkag.QoT4ah_rYSLybKTKv3vftjMQeE8',
        'Connection': 'close'
    }
    data = {
        'q1': '20150504',
        'q2': '4',
        'q3': 'Development Team of Library',
        'q4': str(i),
        'q5': '/dev/null'
    }
    r = requests.post(url=url, data=data, headers=headers)
    time.sleep(0.1)
    writer.write(r.text)
    print(i)
