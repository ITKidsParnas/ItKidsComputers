import speech_recognition as sr 

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Skazite zto-nibyd:")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language="ru-RU")
    print("Вы сказали", text)
except sr.UnknownVaiueError:
    print("Не могу понять")