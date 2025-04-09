
import telebot
from g4f.client import Client

bot= telebot.TeleBot("7501274631:AAGnVIbKUox6ie9CwrghIeTuHxtvoAKfyWM")
client = Client()
@bot.message_handler(commands=["start", "help"])
def command_response(message):
    print(message.chat.username, ":",message.text)
    if message.text == "/start":
        bot.reply_to(message, "Привет")
    if message.text == "/help":
        bot.reply_to(message, "Щас подумаю как помочь")    

@bot.message_handler(content_types=['text'])
def text_response(message):
    usertext = message.text
    print(message.chat.username,":",message.text)
    
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": usertext },{"role": "system", "content": "Ты помошник по современному сленгу, ты должен объяснять значение сленговых слов которые тебе дают. Ответы должны быть только про русский сленг и быть написаны полностью на русском языке. Ответ должен быть коротким. Не отвечай на вопросы не касающиеся сленга. Всегда уточняй информацию в интернете желательно в русский источниках."}],
    web_search=True
    )

    bot.reply_to(message,response.choices[0].message.content)
bot.infinity_polling()