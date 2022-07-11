import requests

proxies = {'http': "http://192.168.1.6:10811",
           'https': "https://192.168.1.6:10811"}


def post():
    url = "http://165.227.106.113/header.php"
    headers = {
        'User-Agent': "Sup3rS3cr3tAg3nt",
        #come from "awesomesauce.com"
        'Referer': 'awesomesauce.com'
    }
    re = requests.get(url, headers=headers, proxies=proxies)
    print(re.text)


post()
