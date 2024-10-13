import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("скажи что-нибуть:")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio,language="ru-RU")
    print("Вы сказали:", text)
except sr.UnknownValueError:
    print("не могу понять")