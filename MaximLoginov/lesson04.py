import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Скажите шо нибудь:")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language="ru-RU")
    print("Вы сказали:", text)
except sr.UnknownValueError:
    print("Не понял")