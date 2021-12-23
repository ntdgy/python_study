import requests


def post():
    url1 = "http://165.227.106.113/post.php"
    headers1 = {
        'Host': '165.227.106.113'
    }
    data = {
        'username': 'admin',
        'password': '71urlkufpsdnlkadsf'
    }
    r1 = requests.post(url=url1, data=data, headers=headers1)
    print(r1.text)


post()
