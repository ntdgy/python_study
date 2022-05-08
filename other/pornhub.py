import re

import requests

#https://hls-hw.xvideos-cdn.com/videos_new/hls/26/ec/90/26ec90a70a45cfa1300243369777d81b/hls-1080p-a006a.m3u8?e=1650622719&l=0&h=ed3d542b43e84d1a9d62a90f6cbb79dc


def get():
    url = 'https://dirpy.com/download'
    headers = {
        'Host': 'dirpy.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Sec-C':''
    }


# def get():
#     url = 'https://cn.pornhub.com/view_video.php?viewkey=ph624ad59e141a4'
#     headers = {
#         'Host': 'cn.pornhub.com',
#         'Sec-Ch-Ua': '"Chromium";v="91", " Not;A Brand";v="99"',
#         'Sec-Ch-Ua-Mobile': '?0',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'Sec-Fetch-Site': 'none',
#         'Sec-Fetch-Mode': 'navigate',
#         'Sec-Fetch-User': '?1',
#         'Sec-Fetch-Dest': 'document',
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept-Language': 'zh-CN,zh;q=0.9',
#         'Connection': 'close',
#     }
#     proxy = {'http': 'socks5h://127.0.0.1:10808','https': 'socks5h://127.0.0.1:10808'}
#     response = requests.get(url, headers=headers, proxies=proxy, verify=False)
#     url = re.findall('videoUrl":"h.*?phncdn.*?mp4.*?"', response.text)
#     if url[0]:
#         print(url[0])
#     return response.text


def test():
    url = 'https://ipinfo.io/ip'
    proxy = {'http': 'socks5h://127.0.0.1:10808','https': 'socks5h://127.0.0.1:10808'}
    response = requests.get(url, proxies=proxy, verify=False)
    print(response.status_code)
    print(response.text)


r = get()
# print(r)

# test()
