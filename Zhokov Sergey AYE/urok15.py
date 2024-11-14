#7826088357:AAEdQiSU5OE16CQQtJZTcstYoMKvWcIWv_4

import telebot

bot = telebot.TeleBot("7826088357:AAEdQiSU5OEl6CQQtJZTcstYoMKvWcIWv_4", parse_mode=None)

@bot.message_handler(commands=["start","help"])
def command_response(message):
    print(message.chat.username, ":", message.text)
    if message.text == "/start":
        bot.reply_to(message, " мандаринка")

@bot.message_handler(content_types=['text'])
def text_response(message):
    print(message.chat.username, ":", message.text)

bot.infinity_polling()s



