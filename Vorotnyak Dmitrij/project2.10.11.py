# 7529393360:AAEuTPYQcALuckta2QfxMI7y8gW51mxHdLQ
import telebot

import uuid
import os
import speech_recognition as sr
import ctypes
import pyogg
import numpy as np
import wave
import translate
from moviepy.audio.io.AudioFileClip import AudioFileClip


bot = telebot.TeleBot("7529393360:AAEuTPYQcALuckta2QfxMI7y8gW51mxHdLQ", parse_mode=None)

language = 'ru_RU'
r = sr.Recognizer()
translator = translate.Translator(to_lang='ru')

def recognise(filename):
    with sr.AudioFile(filename) as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text, language = language)
            print('Перевожу ааудио в текст ._.')
            print(text)
            return text
        except:
            print("ошибаака, попробуйте снова")
            return 'ошибка, попропуйте снова`-`'
        

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


def convert_mp4_to_wav(input_file, output_file):
    audio = AudioFileClip(input_file)
    audio.write_audiofile(output_file)

    

@bot.message_handler(commands=["start", "help", 'poshlivminecraft' "a", 'b', 'c'])
def command_responce(message):
    print(message.chat.username, message.text)
    if message.text == "/start":
        bot.reply_to(message, "HI чтобы общаться дальше вы должны кинуть номер своей карточки")
    if message.text == "/help":
        bot.reply_to(message, 'Отправь или пришли гс')
    if message.text == "/poshlivminecraft":
        bot.reply_to(message, 'Размечтался')


@bot.message_handler(content_types=('text'))
def text_responce(message):
    print(message.chat.username, message.text)
    if 'переведи' or 'Переведи' in message.text:
        text = message.text
        text.replace('переведи', "", 1)
        t_text = translator.translate(text)
        bot.reply_to(message, t_text)

    bot.reply_to(message, message.text)


@bot.message_handler(content_types=['voice'])
def voice_proc(message):
    filename = str(uuid.uuid4())
    file_name_full = filename + '.ogg'
    file_name_full_converted = filename + '.wav'
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
    file_name_full = filename + '.mp4'
    file_name_full_converted = filename + '.wav'
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