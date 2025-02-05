import logging
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

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

# Функция обработки команд /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я бот, с которым можно пообщаться. Чем могу помочь?")

# Функция обработки текстовых сообщений
def chat(update: Update, context: CallbackContext) -> None:
    global chat_history_ids

    user_input = update.message.text

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
    
    update.message.reply_text(bot_response)

def main():
    # Создаем объект Updater и получаем диспетчер для регистрации обработчиков
    updater = Updater("7826088357:AAEdQiSU5OEl6CQQtJZTcstYoMKvWcIWv_4")

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Обработчики команд
    dp.add_handler(CommandHandler("start", start))

    # Обработчик текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))

    # Запускаем бот
    updater.start_polling()

    # Бот будет работать до нажатия Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()