import random
import sqlite3
import telebot

bot = telebot.TeleBot("5161002873:AAEHhFHkUAk-WCQI38h477HaD2YAflPPUkw")
db = sqlite3.connect('file.db')
cursor = db.cursor()
a = []
b = cursor.execute("SELECT Word FROM Words")
for row in b:
    a.append(row[0])

meow = open('meow.txt', 'r')
meow = meow.readlines()


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi there!\nHow much vegetables do you want to sell?")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "It's a bot telling you about selling vegetables.")


@bot.message_handler(commands=['add'])
def add(message):
    tmp = message.text.split(' ', 1)
    tmp = tmp[1]
    a.append(tmp)
    db1 = sqlite3.connect('file.db')
    cursor1 = db1.cursor()
    cursor1.execute("INSERT INTO Words(word) VALUES ('" + tmp + "')")
    db1.commit()
    db1.close()
    with open('countadd.txt', 'r') as f:
        countadd = int(f.read())
    countadd = countadd + 1
    with open('countadd.txt', 'w') as f:
        f.write(str(countadd))

    # with open('froster.txt', 'a') as f:
    # f.write(tmp + '\n')

    bot.reply_to(message, "Successfully added!")


@bot.message_handler(commands=['count'])
def count(message):
    db1 = sqlite3.connect('file.db')
    cursor1 = db1.cursor()
    b1 = cursor1.execute('SELECT * FROM Words')
    with open('countadd.txt', 'r') as f:
        countadd = int(f.read())
    with open('countsell.txt', 'r') as f:
        countsell = int(f.read())
    with open('countmoew.txt', 'r') as f:
        countmoew = int(f.read())
    with open('countdgy.txt', 'r') as f:
        countdgy = int(f.read())
    bot.reply_to(message, '已收集群友' + str(len(b1.fetchall())) + '条卖菜语录!'
                                                              '\n已卖出' + str(countsell) + '次菜'
                                                                                         '\n已添加' + str(countadd) + '条卖菜语录'
                    '\n已喵喵' + str(countmoew) + '次'
                                               '\n已回复' + str(countdgy) + '条dgy语录')
    db1.commit()
    db1.close()


@bot.message_handler(commands=['sell'])
def sell(message):
    i = random.randint(0, len(a) - 1)
    with open('countsell.txt', 'r') as f:
        countsell = int(f.read())
    countsell = countsell + 1
    with open('countsell.txt', 'w') as f:
        f.write(str(countsell))
    bot.reply_to(message, a[i])
    # bot.reply_to(message, "Frankss is our best seller!")


@bot.message_handler(commands=['moew'])
def moew(message):
    with open('countmoew.txt', 'r') as f:
        countmoew = int(f.read())
    countmoew = countmoew + 1
    with open('countmoew.txt', 'w') as f:
        f.write(str(countmoew))
    bot.reply_to(message, meow[random.randint(0, len(meow) - 1)])
    # bot.reply_to(message, "Frankss is our best seller!")


@bot.message_handler(commands=['dgy'])
def moew(message):
    i = ['喵喵喵www', '喵喵喵', 'qaq', '呜呜呜', '呜呜呜ww', '喵ww', '您', '呜呜呜', '我菜菜', '呜呜呜']
    with open('countdgy.txt', 'r') as f:
        countdgy = int(f.read())
    countdgy = countdgy + 1
    with open('countdgy.txt', 'w') as f:
        f.write(str(countdgy))
    bot.reply_to(message, i[random.randint(0, 9)])


bot.infinity_polling()
