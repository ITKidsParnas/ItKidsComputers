import uuid
import os
import speech_recognition as sr
import ctypes
import pyogg
import numpy as np
import wave
import telebot
import translate

bot = telebot.TeleBot("7436369999:AAFq-oQbGakU048Fe6vxvvULCR52A9AK0Zk", parse_mode=None)
language = 'ru_RU'
r = sr.Recognizer()
translator = translate.Translator(to_lang="ru")

def recognise(filename):
    with sr.AudioFile(filename) as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text, language=language)
            print('перевожу аудио в текст')
            print(text)
            return text
        except:
            print("ошибка, попробуйте снова")
            return "ошибка,попробуйте снова"

def convert_opus_to_wav(input_file, output_file):
    opus_file = pyogg.OpusFile(input_file)
    channels = opus_file.channels
    samplerate = opus_file.frequency
    buffer_lenght = opus_file.buffer_length
    buffer_ptr = opus_file.buffer
    
    pcm_data = np.ctypeslib.as_array((ctypes.c_short * buffer_lenght).from_address(ctypes.addressof(buffer_ptr.contents)))

    with wave.open(output_file, 'wb') as wav_file:
        wav_file.setnchannels(channels)
        wav_file.setsampwidth(2)
        wav_file.setframerate(samplerate)
        wav_file.writeframes(pcm_data.tobytes())



@bot.message_handler(commands=["start", "help"])
def commandreaponse(message):
    print(message.chat.username, ":", message.text)
    if message.text == "/start":
        bot.reply_to(message, "Привет я телеграмм бот!^^,отправь или перешли мне голосовое сообщение и я это расшифрую")
    if message.text =="/help":
        bot.reply_to(message, "отправь или перешли мне голосовое сообщение")

@bot.message_handler(content_types=['text'])
def text_response(message):
    bot.reply_to(message,message.text)
    if "переведи" or "Переведи" in message. text:
        text = message.text
        text.replace("переведи", "", 1)
        t_text = translator.translate(text)
        bot.reply_to(message, t_text)


@bot.message_handler(content_types= ['voice'])
def voice_proc(message):
    filename = str(uuid.uuid4())
    file_name_full = filename + ".ogg"
    file_name_full_converted = filename = ".wav"
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name_full, 'wb') as new_file:
        new_file.write(downloaded_file)


    convert_opus_to_wav(file_name_full, file_name_full_converted)

    text = recognise(file_name_full_converted)
    bot.reply_to(message, text)
    os.remove(file_name_full)
    os.remove(file_name_full_converted)


bot.infinity_polling()