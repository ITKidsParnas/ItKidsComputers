
import telebot
from telebot import types
bot = telebot.TeleBot("7744508372:AAH-lo4lugwXJo2riih4TRCZyMEhcYizVLQ", parse_mode=None)
language = 'ru_RU'
from g4f.client import Client

client = Client()

@bot.message_handler(commands=["start", "help"]) 
def command_response(message):
    print(message.chat.username, ":", message.text)
    if message.text == "/start":
        bot.reply_to(message, "отправь смайлик и попробуй понять что ответил человек") 
    if message.text == "/help":
        bot.reply_to(message, "отправь смайлик и попробуй понять что ответил человек") 
        
        
@bot.message_handler(content_types=['text']) #
def text_response(message):
    print(message.chat.username, ":", message.text)
    usertext= message.text
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": usertext}, {"role": "system", "content": "отвечай только в эмодзи"}],
    web_search=False
    )
    
    bot.reply_to(message, response.choices[0].message.content)


bot.infinity_polling()