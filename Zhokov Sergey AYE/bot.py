import telebot
bot.message_handler(commands=["start","help"])
def command_response(message):
    print(message.chat.username, ":", message.text)
    if message.text == "/start":
        bot.reply_to(message, "я тупой ботиха авовововоов.")ыыыыыыы