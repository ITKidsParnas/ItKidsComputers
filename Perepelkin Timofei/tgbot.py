#7822693975:AAFuiQOa2CknRC_7nIPG8Sj0eSIIve0vEBQ

import telebot

bot = telebot.TeleBot("7822693975:AAFuiQOa2CknRC_7nIPG8Sj0eSIIve0vEBQ", parse_mode=None)

@bot.message_handler(commands=["start", "help"])
def commandresponse(message):
    print (message.chat.username, ":", message.text)
    if message.text == "/start":
        bot.reply_to(message, "Привет, я бот, приятно познакомиться!")

@bot.message_handler(content_types=['text'])
def text_reponse(message):
    bot.reply_to(message,message.text)
bot.infinity_polling()