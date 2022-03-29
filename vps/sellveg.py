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
    # with open('froster.txt', 'a') as f:
    # f.write(tmp + '\n')

    bot.reply_to(message, "Successfully added!")


@bot.message_handler(commands=['count'])
def count(message):
    db1 = sqlite3.connect('file.db')
    cursor1 = db1.cursor()
    b1 = cursor1.execute('SELECT * FROM Words')
    bot.reply_to(message, '已收集群友' + str(len(b1.fetchall())) + '条卖菜语录!')
    db1.commit()
    db1.close()


@bot.message_handler(commands=['sell'])
def sell(message):
    i = random.randint(0, len(a) - 1)
    bot.reply_to(message, a[i])
    # bot.reply_to(message, "Frankss is our best seller!")


@bot.message_handler(commands=['moew'])
def moew(message):
    i = ['Moew~', '喵喵喵', '真的要我Moew喵~']
    bot.reply_to(message, i[random.randint(0, 2)])
    # bot.reply_to(message, "Frankss is our best seller!")


@bot.message_handler(commands=['dgy'])
def moew(message):
    i = ['喵喵喵www', '喵喵喵', 'qaq', '呜呜呜', '呜呜呜ww', '喵ww', '您', '呜呜呜', '我菜菜', '呜呜呜']
    bot.reply_to(message, i[random.randint(0, 9)])


bot.infinity_polling()