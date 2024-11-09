import pyjokes
import Joking
import translate
translator = translate.Translator(to_lang="ru")

print(pyjokes.get_joke("ru", "neutral"))
print(translator.translate(Joking.random_joke()))