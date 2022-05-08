import random

import requests
import json
import _thread


def send_request():
    # cURL
    # POST http://10.26.212.174:8765/send/kongming

    try:
        response = requests.post(
            url="http://10.26.212.174:8765/send/kongming",
            headers={
                "Host": "10.26.212.174:8765",
                "Content-Length": "45",
                "Cache-Control": "max-age=0",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "type": "video",
                "content": "dgytest",
                "time": random.randint(0,12)
            })

        )
        if response.status_code != 200:
            print("Fail to send request")
        # print('Response HTTP Status Code: {status_code}'.format(
        #     status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(
        #     content=response.content))
    except requests.exceptions.RequestException:
        pass


if __name__ == '__main__':
    for i in range(10000):
        print(i)
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())
        _thread.start_new_thread(send_request, ())

