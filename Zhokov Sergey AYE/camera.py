
import cv2
import numpy as np
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

# Загрузка предобученной модели для обнаружения лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Используйте команду /detect для начала обнаружения лиц.')

def detect_faces(update: Update, context: CallbackContext) -> None:
    # Захват видео с камеры
    cap = cv2.VideoCapture(1)

    while True:
        ret, frame = cap.read()
        if not ret:
            update.message.reply_text("Не удалось получить кадр.")
            break

        # Преобразование в оттенки серого для улучшения производительности
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Обнаружение лиц
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Отображение прямоугольников вокруг обнаруженных лиц
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Сохранение изображения в файл
        output_file = "output.jpg"
        cv2.imwrite(output_file, frame)

        # Отправка изображения в Telegram
        with open(output_file, 'rb') as f:
            update.message.reply_photo(photo=f)

        # Освобождение ресурсов
        cap.release()
        cv2.destroyAllWindows()
        break  # Завершить цикл после одного кадра

def main() -> None:
    # Вставьте свой токен бота
    updater = Updater("7855515358:AAH2SfG5mKd7VAurxATFhuugG5C05sOJvw0")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("detect", detect_faces))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()