import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Скажите что-нибудь:")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language="ru-Ru")
    print("Вы сказали:", text)
except sr.UnknownValueError:
    print("Не могу понять")