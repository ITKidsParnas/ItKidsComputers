#7436369999:AAFq-oQbGakU048Fe6vxvvULCR52A9AK0Zk

import telebot

bot = telebot.TeleBot("7436369999:AAFq-oQbGakU048Fe6vxvvULCR52A9AK0Zk", parse_mode=None)

@bot.message_handler(commands=["start", "help"])
def commandreaponse(message):
    print(message.chat.username, ":", message.text)
    if message.text == "/start":
        bot.reply_to(message, "Привет я телеграмм бот!^^")

@bot.message_handler(content_types=['text'])
def text_response(message):
    bot.reply_to(message,message.text)
bot.infinity_polling()