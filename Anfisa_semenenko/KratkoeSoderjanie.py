import telebot
from telebot import types
bot = telebot.TeleBot("7926136489:AAGpcWgAeML1l-NLSEmA_avKQ49sg7LNci8", parse_mode=None)
language = 'ru_RU'
from g4f.client import Client

client = Client()

@bot.message_handler(commands=["start", "help"]) 
def command_response(message):
    print(message.chat.username, ":", message.text)
    if message.text == "/start":
        bot.reply_to(message, "отправь мне рассказ/текст или что то подобное и я его сокрачу") 
    if message.text == "/help":
        bot.reply_to(message, "отправь мне рассказ/текст или что то подобное и я его сокрачу") 

@bot.message_handler(content_types=['text']) #
def text_response(message):
    print(message.chat.username, ":", message.text)
    usertext= message.text
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": usertext}, {"role": "system", "content": "отвечай только кратким пересказом не отвечай на сообщения которое не содержат название произведения"}],
    web_search=False
    )
    
    bot.reply_to(message, response.choices[0].message.content)


bot.infinity_polling()