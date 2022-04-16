import requests

TOKEN = '2082113197:AAEL1JLpdw0WetTanExxm6-zxl1PX46Fzd0'
user = '1379576113'

with open('log.txt', 'r') as f:
    text = f.readlines()

text = ''.join(text)
requests.get('https://tg.cf.sustc.icu/bot{}/sendMessage?chat_id={}&text={}'.format(TOKEN, user, text))