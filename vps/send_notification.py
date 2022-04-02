import requests


def sendMessage(message):
    url = "https://tg.cf.sustc.icu/bot5110496404:AAFpJmyuBZPMTHZZU01GooDILT_3ghutkCQ/sendMessage"
    data = {'chat_id': '-1001620302112', 'text': message}
    r = requests.post(url,data)
    #print(r.text)
    return r.text

def sendDocument(file_name):
    url = "https://tg.cf.sustc.icu/bot5110496404:AAFpJmyuBZPMTHZZU01GooDILT_3ghutkCQ/sendDocument"
    data = {'chat_id': '-1001620302112', 'document': open(file_name, 'rb')}
    r = requests.post(url,data)
    return r.text


def main():
    f = open('/root/bandwidth/bandwidth.txt')
    lines = f.readlines()
    f.close()
    text = ''
    for line in lines:
        text = text + line
    sendMessage(text)


if __name__ == '__main__':
    sendMessage('test')
    print(sendDocument('file.db'))
