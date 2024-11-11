# 7529393360:AAEuTPYQcALuckta2QfxMI7y8gW51mxHdLQ
import telebot

bot = telebot.TeleBot("7529393360:AAEuTPYQcALuckta2QfxMI7y8gW51mxHdLQ", parse_mode=None)

@bot.message_handler(commands=["start", "help", "a", 'b', 'c'])
def command_responce(message):
    print(message.chat.username, message.text)
    if message.text == "/start":
        bot.reply_to(message, "HI я не бот")


@bot.message_handler(content_types=('text'))
def text_responce(message):
    print(message.chat.username, message.text)
    bot.reply_to(message, message.text)

bot.infinity_polling()