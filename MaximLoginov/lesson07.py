import uuid
import os
import speech_recognition as sr
import ctypes
import pyogg
import numpy as np
import wave
import telebot
import translate

bot = telebot.TeleBot("7530256897:AAGbOgdlYk-PblBlH1tjvqiD0YQ8gieO624", parse_mode=None)
language = 'ru_RU'
r = sr.Recognizer()
translator = translate.Translator(to_lang="ru")

def recognise(filename):
    with sr.AudioFile(filename) as source:
        audio_text  = r.listen(source)
        try:
            text = r.recognize_google(audio_text, language=language)
            print('Перевожу...')
            print(text)
            return text
        except:
            print('Ничего не понял, но очень интересно')
            return 'НИЧЕГО НЕ ПОНЯЛ НО ОЧЕНЬ ИНТЕРЕСНО'

def convert_opus_to_waw(input_file, output_file):
    opus_file = pyogg.OpusFile(input_file)
    channels = opus_file.channels
    samplerate = opus_file.frequency
    buffer_length = opus_file.buffer_length
    buffer_ptr = opus_file.buffer

    pcm_data = np.ctypeslib.as_array((ctypes.c_short * buffer_length).from_address(ctypes.addressof(buffer_ptr.contents)))

    with wave.open(output_file, 'wb') as wav_file:
        wav_file.setnchannels(channels)
        wav_file.setsampwidth(2)
        wav_file.setframerate(samplerate)
        wav_file.writeframes(pcm_data.tobytes())



@bot.message_handler(commands=["start", "help"])
def commandresponse(message):
    print(message.chat.username, ":",message.text)
    if message.text == "/start":
        bot.reply_to(message, "Приветик, запиши мне голосовое, а я его преобразую в текст. Или напиши мне: переведи (и через пробел своё слово на другом языке кроме русского) и я его переведу на русский")   
    if message.text == "/help":
        bot.reply_to(message, "Запиши мне голосовое, я его преобразую в текст, Или напиши: переведи (и своё слово на другом языке кроме русского) и я переведу его на русский")       
     

@bot.message_handler(content_types=['text'])
def text_reponse(message):
    print(message.chat.username, ":", message.text)
    if "переведи" in message.text:
        text = message.text
        text.replace("переведи", "", 1)
        t_text = translator.translate(text)
        bot.reply_to(message, t_text)


@bot.message_handler(content_types=['voice'])
def voice_proc(message):
    filename = str(uuid.uuid4())
    file_name_full = filename + ".ogg"
    file_name_full_converted = filename + ".wav"
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open(file_name_full, 'wb') as new_file:
        new_file.write(downloaded_file)

    convert_opus_to_waw(file_name_full, file_name_full_converted)

    text = recognise(file_name_full_converted)
    bot.reply_to(message, text)
    os.remove(file_name_full)
    os.remove(file_name_full_converted)


bot.infinity_polling()