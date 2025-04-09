import Joking
import translate
translator = translate.Translator(to_lang="ru")

print(translator.translate(Joking.animal_joke()))