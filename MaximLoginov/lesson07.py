# 7530256897:AAGbOgdlYk-PblBlH1tjvqiD0YQ8gieO624

import telebot

bot = telebot.TeleBot("7530256897:AAGbOgdlYk-PblBlH1tjvqiD0YQ8gieO624", parse_mode=None)

@bot.message_handler(commands=["start", "help"])
def commandresponse(message):
    print(message.chat.username, ":",message.text)
    if message.text == "/start":
        bot.reply_to(message, "ПРИВЕТ Я КРУТОЙ БОТ В ТЕЛЕГРАММЕ")

@bot.message_handler(content_types=['text'])
def text_reponse(message):
    print(message.chat.username, ":", message.text)
    bot.reply_to(message, message.text)
bot.infinity_polling()s