import uuid
import os
import speech_recognition as sr
import ctypes
import pyogg
import numpy as np
import wave
import telebot
import translate
from moviepy.audio.io.AudioFileClip import AudioFileClip

bot = telebot.TeleBot("7436369999:AAFq-oQbGakU048Fe6vxvvULCR52A9AK0Zk", parse_mode=None)
language = 'ru_RU'
r = sr.Recognizer()
translator = translate.Translator(to_lang="ru")

def recognise(filename):
    with sr.AudioFile(filename) as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text, language=language)
            print('Перевожу аудио в текст')
            print(text)
            return text
        except:
            print("Ошибка, попробуйте снова")
            return "Ошибка, попробуйте снова"

def convert_opus_to_wav(input_file, output_file):
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


def convert_mp4_to_wav(input_file, output_file):
    audio = AudioFileClip(input_file)
    audio.write_audiofile(output_file)


@bot.message_handler(commands=["start", "help"])
def command_reaponse(message):
    print(message.chat.username, ":", message.text)
    if message.text == "/start":
        bot.reply_to(message, "Привет, отправь или перешли мне голосовое сообщение и я его расшифрую")
    if message.text == "/help":
        bot.reply_to(message, "отправь или перешли мне голосовое сообщение")

@bot.message_handler(content_types=['text'])
def text_response(message):
    print(message.chat.username, ":", message.text)
    if message.text == "привет" or message.text == "Привет":
        bot.reply_to(message, "привет!Я телеграмм бот давай поговорим?)")
    elif message.text == "давай" or message.text == "Давай" in message.text:
        bot.reply_to(message, "о чем поговорим?)")
    if message.text == "не знаю" or message.text == "Не знаю":
        bot.reply_to(message, "как у тебя прошел день?)")
    elif message.text == "день у меня прошел отлично" or message.text == "День у меня прошел отлично" in message.text:
        bot.reply_to(message, "за этот день у тебя было что то новенькое?)")
    if message.text == "нет ничего нового" or message.text == "Нет ничего нового":
        bot.reply_to(message, "ну хорошо)")
    elif message.text == "ладно мне пора пока" or message.text == "Ладно мне пора пока" in message.text:
        bot.reply_to(message, "пока)")
        


@bot.message_handler(content_types=['voice'])
def voice_proc(message):
    filename = str(uuid.uuid4())
    file_name_full = filename + ".ogg"
    file_name_full_converted = filename + ".wav"
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open(file_name_full, 'wb') as new_file:
        new_file.write(downloaded_file)
        
    convert_opus_to_wav(file_name_full, file_name_full_converted)

    text = recognise(file_name_full_converted)
    bot.reply_to(message, text)
    os.remove(file_name_full)
    os.remove(file_name_full_converted)

@bot.message_handler(content_types=['video_note'])
def video_note_proccesing(message):
    filename = str(uuid.uuid4())
    file_name_full = filename + ".mp4"
    file_name_full_converted = filename + ".wav"
    file_info = bot.get_file(message.video_note.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open(file_name_full, 'wb') as new_file:
        new_file.write(downloaded_file)

    convert_mp4_to_wav(file_name_full, file_name_full_converted)

    text = recognise(file_name_full_converted)
    bot.reply_to(message, text)
    os.remove(file_name_full)
    os.remove(file_name_full_converted)


bot.infinity_polling()
