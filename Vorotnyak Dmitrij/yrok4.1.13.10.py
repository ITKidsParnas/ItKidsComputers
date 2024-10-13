import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print('скажите ваывыфупеп')
    audio = recognizer.listen(source)


try:
    text = recognizer.recognize_google(audio, language="ru-Ru")
    print("вы сказали:", text)
except sr.UnknownValueError:
    print("не могу поy\yночь")