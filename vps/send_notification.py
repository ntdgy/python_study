import requests


def sendMessage(message):
    url = "https://tg.cf.sustc.icu/bot5110496404:AAFpJmyuBZPMTHZZU01GooDILT_3ghutkCQ/sendMessage?chat_id=-1001740652895&text="
    r = requests.post(url + message)
    print(r.text)

def main():
    f = open('/root/bandwidth/bandwidth.txt')
    lines = f.readlines()
    f.close()
    text = ''
    for line in lines:
        text = text + line
    sendMessage(text)


if __name__ == '__main__':
    main()
