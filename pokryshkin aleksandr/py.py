import speech_recognition as sr
from gtts import gTTS
import os
import time

# Функция, которая будет произносить слово
def say_word(word):
    tts = gTTS(text=word, lang='ru')
    tts.save("word.mp3")
    os.system("start word.mp3")  # Для Windows, на Linux используйте 'mpg123 word.mp3'
    time.sleep(1)  # Задержка, чтобы слово успело произнесено

# Функция для получения перевода
def translate(word):
    translations = {}
        "кот": "cat",
        "собака": "dog",
        "человек": "man",
        "машина": "car",
        "игра": "game",
    
        # Добавьте другие слова и их переводы
    
    sreturn translations.get(word, "Нет перевода")

# Основной цикл программы
while True:
    word = input("Введите слово (или 'выход' для завершения): ")
    if word.lower() == 'выход':
        break

    say_word(word)
    translation = translate(word)
    print(f'Перевод слова "{word}": {translation}')










































































































































































