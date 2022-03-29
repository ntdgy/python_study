import random

import telebot

bot = telebot.TeleBot("5161002873:AAEHhFHkUAk-WCQI38h477HaD2YAflPPUkw")
with open('froster.txt', 'r') as f:
    a = f.readlines()
print(a)


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
    with open('froster.txt', 'a') as f:
        f.write(tmp + '\n')
    bot.reply_to(message, "Successfully added!")


@bot.message_handler(commands=['sell'])
def sell(message):
    i = random.randint(0, len(a) - 1)
    bot.reply_to(message, a[i])
    # bot.reply_to(message, "Frankss is our best seller!")


bot.infinity_polling()
