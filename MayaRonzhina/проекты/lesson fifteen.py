import pyttsx3
#создает объект воспроизведения 
engine = pyttsx3.init()
engine.setProperty("rate", 1)
engine.say("привет")
engine.runAndWait()