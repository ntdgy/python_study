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
    if len(tmp) == 2:
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
        bot.reply_to(message, "Successfully added!")
    else:
        bot.reply_to(message, "请输入信息")


@bot.message_handler(commands=['count'])
def count(message):
    db1 = sqlite3.connect('file.db')
    cursor1 = db1.cursor()
    b1 = cursor1.execute('SELECT * FROM Words')
    with open('countadd.txt', 'r') as f:
        countadd = int(f.read())
    with open('countsell.txt', 'r') as f:
        countsell = int(f.read())
    with open('countmeow.txt', 'r') as f:
        countmeow = int(f.read())
    with open('countdgy.txt', 'r') as f:
        countdgy = int(f.read())
    bot.reply_to(message, '已收集群友' + str(len(b1.fetchall())) + '条卖菜语录!'
                                                              '\n已卖出' + str(countsell) + '次菜'
                                                                                         '\n已添加' + str(countadd) + '条卖菜语录'
                    '\n已喵喵' + str(countmeow) + '次'
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


@bot.message_handler(commands=['meow'])
def meow1(message):
    with open('countmeow.txt', 'r') as f:
        countmeow = int(f.read())
    countmeow = countmeow + 1
    with open('countmeow.txt', 'w') as f:
        f.write(str(countmeow))
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


@bot.message_handler(commands=['record'])
def record1(message):
    tmp = message.text.split(' ', 1)
    if len(tmp) == 2:
        tmp = tmp[1]
        db1 = sqlite3.connect('file.db')
        cursor1 = db1.cursor()
        cursor1.execute("INSERT INTO jichou(record) VALUES ('" + tmp + "')")
        db1.commit()
        db1.close()
        with open('history.txt', 'a') as f:
            f.write(tmp + '\n')
        with open('countjichou.txt', 'r') as f:
            countadd = int(f.read())
        countadd = countadd + 1
        with open('countjichou.txt', 'w') as f:
            f.write(str(countadd))
        bot.reply_to(message, "Successfully added!")
    else:
        bot.reply_to(message, "请输入信息")

@bot.message_handler(commands=['getrecord'])
def getrecord1(message):
    db1 = sqlite3.connect('file.db')
    cursor1 = db1.cursor()
    cursor1.execute("select * from jichou")
    db1.commit()
    message1 = ''
    i = 1
    for row in cursor1.fetchall():
        message1 = message1 + str(row[0]) + '. ' + row[1] + '\n'
    if message1 == '':
        bot.reply_to(message,'暂无记录')
    else:
        bot.reply_to(message, message1)
    db1.close()

@bot.message_handler(commands=['delrecord'])
def getrecord1(message):
    tmp = message.text.split(' ',1)
    tmp = tmp[1]
    if tmp.isdigit():
        db1 = sqlite3.connect('file.db')
        cursor1 = db1.cursor()
        cursor1.execute("delete from jichou where id = " + tmp)
        db1.commit()
        if cursor1.rowcount == 1:
            bot.reply_to(message, "Successfully deleted!")
        else:
            bot.reply_to(message, "No such record!")

        db1.close()
    else:
        bot.reply_to(message, "待删除的记录序号必须为数字!")

@bot.message_handler(commands=['resetrecord'])
def getrecord1(message):
    db1 = sqlite3.connect('file.db')
    cursor1 = db1.cursor()
    cursor1.execute("select * from jichou")
    db1.commit()
    message1 = ''
    i = 1
    for row in cursor1.fetchall():
        message1 = message1 + str(row[0]) + '. ' + row[1] + '\n'
    if message1 != '':
        bot.reply_to(message, '数据库不为空，无法执行清空操作')
    else:
        cursor1.execute("drop table jichou")
        db1.commit()
        cursor1.execute('CREATE TABLE jichou( id INTEGER PRIMARY KEY, record TEXT)')
        db1.commit()
        bot.reply_to(message, '数据库已清空')
    db1.close()


bot.infinity_polling()
