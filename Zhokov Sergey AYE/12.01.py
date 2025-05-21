import logging
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import telebot

# Настройки логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Загрузка предобученной модели и токенизатора
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Хранение истории диалога
chat_history_ids = None

# Создание экземпляра бота
API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

# Функция обработки команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, с которым можно пообщаться. Чем могу помочь?")

# Функция обработки текстовых сообщений
@bot.message_handler(func=lambda message: True)
def chat(message):
    global chat_history_ids

    user_input = message.text

    # Токенизация входного текста
    new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    # Объединяем с историей чата
    if chat_history_ids is not None:
        input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
    else:
        input_ids = new_user_input_ids

    # Генерация ответа
    chat_history_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # Декодирование модели и вывод
    bot_response = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    
    # Отправка бот-ответа
    bot.reply_to(message, bot_response)

if __name__ == '__main__':
    # Запуск бота
    bot.polling(none_stop=True)
